
from src.util import Timeline
from src.util import Block
from src.util import MCUUIDManager
from src.util import MovingEntity

def get_paint_block_timeline(x0: float, y0: float, z0: float, vy: float, start_tick: int, block: Block, uuid_manager: MCUUIDManager) -> Timeline:
    output = Timeline({})

    uuid = uuid_manager.get_new_uuid()

    summon_cmd = (
        f"summon block_display ~{x0:.5f} ~{y0:.5f} ~{z0:.5f} "
        "{"
        f'block_state:{{Name:"{block.id}",Properties:{block.get_block_state_str()}}},'
        "transformation:{"
        "left_rotation:[0.0f,0.0f,0.0f,1.0f],"
        "right_rotation:[0.0f,0.0f,0.0f,1.0f],"
        "scale:[1.0f,1.0f,1.0f],"
        "translation:[0.0f,0.0f,0.0f]"
        "},"
        'Tags:["piano_falling_block"],'
        "brightness:{sky:12,block:12},"
        "teleport_duration:1,"
        f"UUID:{uuid.to_int_array_str()}"
        "}"
    )
    output.add_command(start_tick, summon_cmd)

    moving_entity = MovingEntity(x0, y0, z0, block.x, block.y, block.z, uuid)
    timeline = moving_entity.get_projectile_timeline(vy, start_tick)
    output.merge(timeline)
    last_tick = timeline.get_last_tick()
    output.add_command(last_tick + 1, f"setblock ~{block.x} ~{block.y} ~{block.z} {block.name}")
    output.add_command(last_tick + 1, f"kill {uuid.to_uuid_string()}")

    return output