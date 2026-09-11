import itertools
from src.util import Timeline
from .note import Note
from src.util import Block
from src.util import BlockGroup
from src.util import get_falling_block_command
from src.util import DatapackManager
import random
from .displayer import get_displayer_timeline
from src.piano.note import midi_parse
from src.piano.note import MidiFile
from src.piano.config import PianoConfig
from src.util import Logger
from src.piano.waterfall import get_waterfall_timeline
from src.util import MCUUIDManager

def split_list(lst: list[Block], x: int):
    it = iter(lst)
    n = len(lst)
    part_size = (n + x -1)//x
    return [list(itertools.islice(it, part_size)) for _ in range(x)]

def get_timeline(note_list: list[Note], block_list: BlockGroup, config: PianoConfig, logger: Logger) -> Timeline:
    note_list.sort(key=lambda x: x.start_second)
    block_list_split = split_list(block_list.get_list(), config.block_splits)
    output_timeline = Timeline({})
    current_block_index = 0
    current_note_index = 0
    block_tag_number = 0
    note_list_len = len(note_list)
    logger.log_info("正在生成命令...")

    for note in note_list:
        current_note_index += 1
        logger.set_progress(current_note_index / note_list_len)
        output_timeline.add_command(note.mc_tick, config.playsound_tpl.format(sound=note.sound_id, vol=note.volume))
        output_timeline.add_command(note.mc_tick, config.scoreboard_tpl.format(note_num=note.midi_number, tick_len=int(note.ingame_duration*20)))

        if len(block_list_split) > current_block_index and config.block_painting:
            start_x = config.note_pos[note.midi_number][0]
            start_y = config.note_pos[note.midi_number][1]
            start_z = config.note_pos[note.midi_number][2]
            motion_val = config.motion_y + random.random() * config.motion_y_random
            chunk_blocks = block_list_split[current_block_index]

            for block in chunk_blocks:
                block_tag_number += 1
                output_timeline.merge_absolute(get_falling_block_command(start_x,start_y,start_z, block, motion_val, note.mc_tick, block_tag_number))
            current_block_index += 1

    if config.displayer:
        output_timeline.merge_absolute(get_displayer_timeline(note_list, config))
    logger.log_success("所有命令已生成!")
    return output_timeline

def write_datapack(datapack: DatapackManager, scoreboard_name: str, config:PianoConfig):
    # reset.mcfunction
    reset_lines = [
        f"scoreboard players set @e[type=marker,tag={config.marker_tag},limit=1,sort=nearest] {scoreboard_name} 0",
        f"execute at @e[type=marker,tag={config.marker_tag},limit=1,sort=nearest] positioned ~2 ~-2 ~-2 run kill @e[tag=piano_displayer,{config.displayer_kill_area}]",
        f"execute at @e[type=marker,tag={config.marker_tag},limit=1,sort=nearest] positioned ~2 ~-2 ~-2 run kill @e[tag=piano_waterfall]",
    ]
    for n in range(21, 109):
        reset_lines.append(
            f"scoreboard players set @e[type=marker,tag={config.marker_tag},limit=1,sort=nearest] note_{n} 0"
        )
    datapack.write_function_file("reset.mcfunction", reset_lines)
    # start.mcfunction
    start_lines = [
        f"scoreboard players set @e[type=marker,tag={config.marker_tag},limit=1,sort=nearest] {scoreboard_name} 1",
    ]
    datapack.write_function_file("start.mcfunction", start_lines)
    # tick.mcfunction
    datapack.write_function_file(
        "tick.mcfunction",
        f"execute as @e[type=marker,tag={config.marker_tag}] if score @s {scoreboard_name} matches 1.. at @s run function {datapack.datapack_name}:loop"
    )

def get_error(note_list:list[Note]):
    max_error = 0
    avg_error = 0
    length = len(note_list)
    for note in note_list:
        max_error = max(note.error_time,max_error)
        avg_error += note.error_time / length
    return max_error,avg_error

def piano_main(cfg:PianoConfig, logger: Logger):

    logger.log("\n")
    logger.log_info("钢琴键盘预设已加载!")
    logger.set_progress(0)

    uuid_manager = MCUUIDManager()

    try:
        note_list = midi_parse(MidiFile(cfg.midi_path),cfg)
        note_list_len = len(note_list)
        logger.log_success("已加载Midi文件: {} (音符总数: {})".format(cfg.midi_path,str(note_list_len)))
    except FileNotFoundError:
        logger.log_error("Midi文件({})不存在!".format(cfg.midi_path))
        return
    except Exception as e:
        logger.log_error("Midi文件({})读取失败: {}".format(cfg.midi_path, str(e)))
        return

    block_list = BlockGroup(None, None)
    if cfg.block_painting:
        try:
            block_list = BlockGroup(cfg.block_path, cfg.painting_base_pos)
            block_list.sort_by_axis("y")
            block_num = len(block_list.get_list())
            if block_num > 0:
                logger.log_success(f"方块文件加载已加载, 总方块数: {block_num}.")
            else:
                logger.log_warn(f"加载的方块列表为空, 可能是加载时出现异常.")
        except Exception as e:
            logger.log_error(f"加载方块文件时出现错误: {str(e)}")

        if cfg.block_splits > note_list_len:
            logger.log_error("方块抛射波数({})大于音符总数({}), 部分方块可能无法生成, 请尝试降低方块抛射波数!".format(cfg.block_splits, note_list_len))
        else:
            logger.log_success("方块抛射波数({})小于音符总数({}), 所有方块均可被生成.".format(cfg.block_splits, note_list_len))
    else:
        logger.log_warn(f"未启用方块抛射绘画, 将跳过方块文件加载.")

    
    max_error, avg_error = get_error(note_list)
    logger.log_warn("音符时间误差:".format(max_error,avg_error))
    logger.log_warn("   最大误差: {:.6f}ms".format(max_error))
    logger.log_warn("   平均误差: {:.6f}ms".format(avg_error))

    piano_timeline = get_timeline(note_list, block_list, cfg, logger)

    waterfall_tick_shift = 0
    if cfg.waterfall:
        try:
            waterfall_tick_shift = note_list[0].mc_tick - cfg.waterfall_tick
            waterfall_timeline = get_waterfall_timeline(note_list, cfg, uuid_manager)
            piano_timeline.merge_absolute(waterfall_timeline)
            logger.log_success(f"已生成瀑布流命令!")
            if waterfall_tick_shift <= 0:
                piano_timeline.shift_time(1 - waterfall_tick_shift)
                logger.log_warn(f"瀑布流命令最小执行时刻 ({waterfall_tick_shift}) 小于0, 部分瀑布流命令无法被执行, 已自动调整音乐播放起始时刻使所有瀑布流命令都可以被执行.")
        except Exception as e:
            logger.log_error(f"生成瀑布流命令时出现错误: {str(e)}")
    else:
        logger.log_warn(f"未启用瀑布流, 将跳过瀑布流命令生成.")

    datapack = DatapackManager(cfg.datapack_name, cfg.datapack_version, logger)
    if datapack.is_backuped == False:
        return
    piano_timeline.write_datapack(datapack, cfg.datapack_name + "_timer", logger)
    write_datapack(datapack, cfg.datapack_name + "_timer", cfg)
    logger.log_success(f"数据包已生成! 位置: output/" + cfg.datapack_name)
