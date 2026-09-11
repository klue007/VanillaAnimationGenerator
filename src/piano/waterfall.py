
from src.piano.note import Note
from src.piano.config import PianoConfig
from src.util import MCUUIDManager, MovingEntity, Timeline

def get_note_waterfall_timeline(t0: int, t1: int, t_trans: int, x0: float, y0: float, z0: float, x1: int, y1: int, z1: int, block: str, block_size: int, id: int, uuid_manager: MCUUIDManager) -> Timeline:
    output = Timeline({})
    uuid = uuid_manager.get_new_uuid()

    output.add_command(t0, f"summon item_display ~{x0:.5f} ~{y0:.5f} ~{z0:.5f} {{item:{{id:\"{block}\"}},transformation:{{left_rotation:[0.0f,0.0f,0.0f,1.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f],scale:[0.0f,0.0f,0.0f],translation:[0.0f,0.0f,0.0f]}},Tags:[\"piano_waterfall\"],brightness:{{sky:15,block:15}},teleport_duration:1,UUID:{uuid.to_int_array_str()}}}")

    moving_entity = MovingEntity(x0, y0, z0, x1, y1, z1, uuid)
    output.merge(moving_entity.get_straight_line_timeline(t0, t1))

    for i in range(0, t_trans):
        scale_new = block_size * i / t_trans

        output.add_command(t0 + i, f"data merge entity {uuid.to_uuid_string()} {{transformation:{{scale:[{scale_new:.3f}f,{scale_new:.3f}f,{scale_new:.3f}f]}}}}")

    output.add_command(t1, f"kill {uuid.to_uuid_string()}")

    return output


def get_note_waterfall_timeline_vertical(note:Note, cfg:PianoConfig, id: int, uuid_manager: MCUUIDManager) -> Timeline:
    t1 = note.mc_tick
    t0 = t1 - cfg.waterfall_tick
    t_trans = cfg.waterfall_block_transition_tick
    x1 = cfg.note_pos[note.midi_number][0]
    y1 = cfg.note_pos[note.midi_number][1]
    z1 = cfg.note_pos[note.midi_number][2]
    return get_note_waterfall_timeline(t0,t1,t_trans,x1,y1 + cfg.waterfall_height,z1,x1,y1,z1,cfg.waterfall_block,cfg.waterfall_block_size,id, uuid_manager)



def get_note_waterfall_timeline_horizontal(note:Note, cfg:PianoConfig, id: int, uuid_manager: MCUUIDManager) -> Timeline:
    t1 = note.mc_tick
    t0 = t1 - cfg.waterfall_tick
    t_trans = cfg.waterfall_block_transition_tick
    x1 = cfg.note_pos[note.midi_number][0]
    y1 = cfg.note_pos[note.midi_number][1]
    z1 = cfg.note_pos[note.midi_number][2]
    return get_note_waterfall_timeline(t0,t1,t_trans,x1 + cfg.waterfall_height,y1,z1,x1,y1,z1,cfg.waterfall_block,cfg.waterfall_block_size,id, uuid_manager)


def get_waterfall_timeline(note_list: list[Note], cfg: PianoConfig, uuid_manager: MCUUIDManager) -> Timeline:
    output = Timeline({})
    tag_number = 0

    for note in note_list:
        tag_number += 1
        if cfg.waterfall_mode == 0:
            note_timeline = get_note_waterfall_timeline_vertical(note, cfg, tag_number, uuid_manager)
        elif cfg.waterfall_mode == 1:
            note_timeline = get_note_waterfall_timeline_horizontal(note, cfg, tag_number, uuid_manager)
        else:
            note_timeline = get_note_waterfall_timeline_vertical(note, cfg, tag_number, uuid_manager)
        output.merge(note_timeline)  

    return output