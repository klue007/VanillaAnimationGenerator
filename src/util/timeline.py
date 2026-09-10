
import copy

import os

from .logger import Logger
from .datapack_manager import DatapackManager

class Timeline():
    """
    This class stores all tick events for a single animated mechanism.

    Attributes:
        timeline_diction : dict
            Stores tick-scheduled events, formatted as:
            {tick1: ["command1", "command2", ...], ...}
    """

    def __init__(self, timeline_diction: dict[int, list[str]]):
        self.timeline_diction = timeline_diction


    def merge_absolute(self, target_timeline: Timeline):
        """
        Merge another timeline into this one.

        Commands from events occurring at the same tick will be appended to that tick's existing command set.

        Args:
            target_timeline : (Timeline)
                Source timeline to merge into the current instance.
        """
        for key, value in target_timeline.timeline_diction.items():
            if key in self.timeline_diction:
                self.timeline_diction[key].extend(value)
            else:
                self.timeline_diction[key] = value.copy()



    def merge_relative(self, target_timeline: Timeline, start_tick: int):
        """
        Merge another timeline into this one using relative time offset.

        The target timeline's tick events will be offset by start_tick.
        Commands from events occurring at the same tick will be appended to that tick's existing command set.

        Args:
            target_timeline : (Timeline)
                Source timeline to merge into the current instance.

            start_tick : (int)
                The time offset.
        """
        target_timeline_backup = copy.deepcopy(target_timeline)
        target_timeline_backup.shift_time(start_tick)
        self.merge_absolute(target_timeline_backup)



    def shift_time(self, delta_tick: int):
        """
        Offset all event ticks in the timeline by a given tick delta.

        Args:
            delta_tick : (int)
                Tick offset added to every existing event tick. Positive values shift forward, negative values shift backward.
        """
        new_diction = {}

        for key, value in self.timeline_diction.items():
            new_diction[key + delta_tick] = value

        self.timeline_diction = new_diction




    def len(self):
        """
        Get the amount of tick events.
        """
        return len(self.timeline_diction)



    def get_command(self, tick, return_as_list = True):
        """
        Get commands for events at a specified tick.

        Args:
            tick : (int)
                Target game tick to look up.
            return_as_list : (bool)
                If True, return commands as a list; otherwise return a single concatenated string. Defaults to True.
        """
        command_list = []

        if tick in self.timeline_diction:
            command_list = self.timeline_diction[tick]

        if return_as_list:
            return command_list
        else:
            return "\n".join(command_list)



    def add_command(self, tick: int, command: str | list[str]):
        """
        Add one or multiple commands to the timeline at a given tick.

        Args:
            tick : (int)
                Target game tick for the command(s).

            command : (str) | (list[str])
                Single command string, or a list of multiple commands to add.
        """

        if tick not in self.timeline_diction:
            self.timeline_diction[tick] = []

        if isinstance(command, list):
            self.timeline_diction[tick].extend(command)
        else:
            self.timeline_diction[tick].append(command)



    def write_datapack(self, datapack: DatapackManager, scoreboard_name: str, logger: Logger):
        
        max_tick = max(self.timeline_diction.keys())
    
        # generate tick event functions as evt_xxxx.mcfunction
        logger.log_info("正在将动画命令写入数据包...")
        timeline_len = len(self.timeline_diction)
        index = 0
        for tick, commands in self.timeline_diction.items():
            index += 1
            logger.set_progress(index/timeline_len)
            datapack.write_function_file(os.path.join("evt", f"{tick + 2}.mcfunction"), commands)
        logger.log_success("动画命令已写入!")
    
        # loop.mcfunction
        loop_lines = []
        loop_lines.append(
            f"execute if score @s {scoreboard_name} matches 1.. run scoreboard players add @s {scoreboard_name} 1"
        )
    
        sorted_ticks = sorted(self.timeline_diction.keys())
        for t in sorted_ticks:
            loop_lines.append(
                f"execute if score @s {scoreboard_name} matches {t + 2} run function {datapack.datapack_name}:evt/{t + 2}"
            )
        loop_lines.append(
            f"execute if score @s {scoreboard_name} matches {max_tick + 3}.. run scoreboard players set @s {scoreboard_name} 0"
        )
        datapack.write_function_file("loop.mcfunction", loop_lines)
    
        # load.mcfunction
        datapack.write_function_file("load.mcfunction",f"scoreboard objectives add {scoreboard_name} dummy \"{scoreboard_name}\"")
