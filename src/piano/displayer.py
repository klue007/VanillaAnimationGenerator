from src.util import Timeline
from src.piano.note import Note
from src.piano.config import PianoConfig
import math


class PianoDisplayer():
    def __init__(self, id) -> None:
        self.current_note = 21
        self.current_tick = 0
        self.id = id

    def move(self, time: int, note: Note, config: PianoConfig) -> Timeline:
        output = Timeline({})
        entity = f"@e[tag=piano_displayer,tag=piano_displayer_{self.id}]"
        start_x = config.note_pos[self.current_note][0]
        start_y = config.note_pos[self.current_note][1]
        start_z = config.note_pos[self.current_note][2]
        end_x = config.note_pos[note.midi_number][0]
        end_y = config.note_pos[note.midi_number][1]
        end_z = config.note_pos[note.midi_number][2]
        peak_height = config.displayer_peak_height

        if time <= 0:
            output.add_command(note.mc_tick, f"tp {entity} {end_x:.3f} {end_y:.3f} {end_z:.3f}")
        else:
            for tick_offset in range(0, time + 1):
                t = tick_offset / time
                if config.displayer_vortex:
                    theta0 = math.atan2(start_z, start_x)
                    theta1 = math.atan2(end_z, end_x)
                    delta_raw = theta1 - theta0
                    delta = (delta_raw + math.pi) % (2 * math.pi) - math.pi
                    theta = theta0 + delta * t
                    r0 = math.hypot(start_x, start_z)
                    r1 = math.hypot(end_x, end_z)
                    r = r0 + (r1 - r0) * t
                    x = r * math.cos(theta)
                    z = r * math.sin(theta)
                else:
                    x = start_x + (end_x - start_x) * t
                    z = start_z + (end_z - start_z) * t
                y = start_y * (1 - t) + end_y * t + peak_height * 4 * t * (1 - t)
                cmd = f"tp {entity} ~{x:.3f} ~{y:.3f} ~{z:.3f}"
                output.add_command(tick_offset, cmd)
            output.shift_time(note.mc_tick - time)
        self.current_tick = note.mc_tick
        self.current_note = note.midi_number
        return output


def get_single_displayer_timeline(note_dict: dict[int, list[Note]], displayer_list: list[PianoDisplayer], config: PianoConfig) -> Timeline:
    output = Timeline({})
    for _, note_list in sorted(note_dict.items()):
        available_displayer_list = displayer_list.copy()
        for note in note_list:
            if len(available_displayer_list) <= 0:
                continue
            selected_displayer = min(available_displayer_list, key=lambda x: abs(x.current_note - note.midi_number))

            tp_timeline = selected_displayer.move(
                min(config.displayer_max_moving_tick, abs(note.mc_tick - selected_displayer.current_tick)),
                note, config
            )
            output.merge_absolute(tp_timeline)
            available_displayer_list.remove(selected_displayer)
        if len(available_displayer_list) > 0:
            for displayer in available_displayer_list:
                tp_timeline = displayer.move(
                    min(config.displayer_max_moving_tick, abs(note_list[0].mc_tick - displayer.current_tick)),
                    note_list[0], config
                )
                output.merge_absolute(tp_timeline)
    return output


def get_displayer_timeline(note_list: list, config: PianoConfig) -> Timeline:
    note_dict_left = {}
    note_dict_right = {}
    output_timeline = Timeline({})
    for note in note_list:
        if note.track == 1:
            if note.mc_tick not in note_dict_right:
                note_dict_right[note.mc_tick] = []
            note_dict_right[note.mc_tick].append(note)
        elif note.track == 2:
            if note.mc_tick not in note_dict_left:
                note_dict_left[note.mc_tick] = []
            note_dict_left[note.mc_tick].append(note)
    n = 0
    right_displayer_list = []
    left_displayer_list = []
    output_timeline.add_command(1, f"kill @e[tag=piano_displayer,dx=-22,dy={config.displayer_peak_height + 3},dz=160]")

    while n < config.displayer_count_right:
        n += 1
        right_displayer_list.append(PianoDisplayer(n))
        output_timeline.add_command(1, config.displayer_summon_cmd.format(id=n, displayer_block=config.displayer_block))
    while n < config.displayer_count_right + config.displayer_count_left:
        n += 1
        left_displayer_list.append(PianoDisplayer(n))
        output_timeline.add_command(1, config.displayer_summon_cmd.format(id=n, displayer_block=config.displayer_block))

    timeline_right = get_single_displayer_timeline(note_dict_right, right_displayer_list, config)
    timeline_left = get_single_displayer_timeline(note_dict_left, left_displayer_list, config)
    output_timeline.merge_absolute(timeline_right)
    output_timeline.merge_absolute(timeline_left)
    return output_timeline
