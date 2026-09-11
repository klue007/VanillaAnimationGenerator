from src.util import Timeline, MovingEntity
from src.piano.note import Note
from src.piano.config import PianoConfig
from src.util import MCUUIDManager, MCUUID

class PianoDisplayer():
    def __init__(self, uuid: MCUUID) -> None:
        self.current_note = 21
        self.current_tick = 0
        self.uuid = uuid

    def move(self, time: int, note: Note, config: PianoConfig) -> Timeline:
        output = Timeline({})
        start_x = config.note_pos[self.current_note][0]
        start_y = config.note_pos[self.current_note][1]
        start_z = config.note_pos[self.current_note][2]
        end_x = config.note_pos[note.midi_number][0]
        end_y = config.note_pos[note.midi_number][1]
        end_z = config.note_pos[note.midi_number][2]
        peak_height = config.displayer_peak_height

        if time <= 0:
            output.add_command(note.mc_tick, f"tp {self.uuid.to_uuid_string()} {end_x:.3f} {end_y:.3f} {end_z:.3f}")
        else:
            moving_entity = MovingEntity(start_x, start_y, start_z, end_x, end_y, end_z, self.uuid)
            if config.displayer_vortex:
                output.merge(moving_entity.get_vortex_parabolic_timeline(peak_height, note.mc_tick - time, note.mc_tick, 0, 0))
            else:
                output.merge(moving_entity.get_parabolic_timeline(peak_height, note.mc_tick - time, note.mc_tick))
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
            output.merge(tp_timeline)
            available_displayer_list.remove(selected_displayer)
        if len(available_displayer_list) > 0:
            for displayer in available_displayer_list:
                tp_timeline = displayer.move(
                    min(config.displayer_max_moving_tick, abs(note_list[0].mc_tick - displayer.current_tick)),
                    note_list[0], config
                )
                output.merge(tp_timeline)
    return output


def get_displayer_timeline(note_list: list, config: PianoConfig, uuid_manager: MCUUIDManager) -> Timeline:
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

    displayer_summon_command = "summon item_display ~ ~ ~ {{item:{{id:\"{displayer_block}\"}},transformation:{{left_rotation:[0.0f,0.0f,0.0f,1.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f],scale:[{size}f,{size}f,{size}f],translation:[0.0f,0.0f,0.0f]}},Tags:[\"piano_displayer\"],Glowing:1b,brightness:{{sky:15,block:15}},teleport_duration:1,UUID:{uuid}}}"

    while n < config.displayer_count_right:
        n += 1
        uuid = uuid_manager.get_new_uuid()
        right_displayer_list.append(PianoDisplayer(uuid))
        output_timeline.add_command(1, displayer_summon_command.format(uuid=uuid.to_int_array_str(), displayer_block=config.displayer_block, size=config.displayer_size))
    while n < config.displayer_count_right + config.displayer_count_left:
        n += 1
        uuid = uuid_manager.get_new_uuid()
        left_displayer_list.append(PianoDisplayer(uuid))
        output_timeline.add_command(1, displayer_summon_command.format(uuid=uuid.to_int_array_str(), displayer_block=config.displayer_block, size=config.displayer_size))

    timeline_right = get_single_displayer_timeline(note_dict_right, right_displayer_list, config)
    timeline_left = get_single_displayer_timeline(note_dict_left, left_displayer_list, config)
    output_timeline.merge(timeline_right)
    output_timeline.merge(timeline_left)
    return output_timeline
