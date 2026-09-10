import itertools
from src.util import Timeline
from .note import Note
from src.util import Block
from src.util import BlockGroup
from src.util import falling_block_calculate
from src.util import DatapackManager
import random
import os
from .displayer import get_displayer_timeline
from src.piano.note import midi_parse
from src.piano.note import MidiFile
from src.piano.config import PianoConfig
from src.util import Logger
import time

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
    logger.log_info("正在计算方块动画实体...")

    for note in note_list:
        current_note_index += 1
        logger.set_progress(current_note_index / note_list_len)
        output_timeline.add_command(note.mc_tick, config.playsound_tpl.format(sound=note.sound_id, vol=note.volume))
        output_timeline.add_command(note.mc_tick, config.scoreboard_tpl.format(note_num=note.midi_number, tick_len=int(note.ingame_duration*20)))

        if len(block_list_split) > current_block_index and config.block_painting == 1:
            start_x = config.note_pos[note.midi_number][0]
            start_y = config.note_pos[note.midi_number][1]
            start_z = config.note_pos[note.midi_number][2]
            motion_val = config.motion_y + random.random() * config.motion_y_random
            chunk_blocks = block_list_split[current_block_index]

            for block in chunk_blocks:
                block_tag_number += 1
                output_timeline.merge_absolute(falling_block_calculate(start_x,start_y,start_z, block, motion_val, note.mc_tick, block_tag_number))
            current_block_index += 1

    if config.displayer == 1:
        output_timeline.merge_absolute(get_displayer_timeline(note_list, config))
    logger.log_success("完成!")
    return output_timeline

def write_datapack(datapack: DatapackManager, scoreboard_name: str, config:PianoConfig):
    # reset.mcfunction
    reset_lines = [
        f"scoreboard players set @e[type=marker,tag={config.marker_tag},limit=1,sort=nearest] {scoreboard_name} 0",
        f"execute at @e[type=marker,tag={config.marker_tag},limit=1,sort=nearest] positioned ~2 ~-2 ~-2 run kill @e[tag=piano_displayer,{config.displayer_kill_area}]",
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

    logger.log_info("钢琴键盘预设已加载!")
    logger.set_progress(0)

    block_list = BlockGroup(None, None)
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

    if cfg.block_splits > note_list_len:
        logger.log_error("方块抛射波数({})大于音符总数({}), 部分方块可能无法生成, 请尝试降低方块抛射波数!".format(cfg.block_splits, note_list_len))
    else:
        logger.log_success("方块抛射波数({})小于音符总数({}), 所有方块均可被生成.".format(cfg.block_splits, note_list_len))

    try:
        block_list = BlockGroup(cfg.block_path, cfg.painting_base_pos)
        block_list.sort_by_axis("y")
    except Exception as e:
        logger.log_error(f"加载方块文件时出现错误: {str(e)}")

    block_num = len(block_list.get_list())
    if block_num > 0:
        logger.log_success(f"方块文件加载已加载, 总方块数: {block_num}.")
    else:
        logger.log_warn(f"加载的方块列表为空, 可能是加载时出现异常.")
    
    max_error, avg_error = get_error(note_list)
    logger.log_warn("音符时间误差:".format(max_error,avg_error))
    logger.log_warn("   最大误差: {:.6f}ms".format(max_error))
    logger.log_warn("   平均误差: {:.6f}ms".format(avg_error))

    piano_timeline = get_timeline(note_list, block_list, cfg, logger)
    datapack = DatapackManager(cfg.datapack_name, cfg.datapack_version)
    piano_timeline.write_datapack(datapack, cfg.datapack_name + "_timer", logger)
    write_datapack(datapack, cfg.datapack_name + "_timer", cfg)
    logger.log_success(f"数据包已生成! 位置: output/" + cfg.datapack_name)
