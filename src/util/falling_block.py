from .timeline import Timeline
from .block import Block

def calc_y_pos(T: int, y1: float, vy0: float) -> float:
    q = 0.98
    term1 = (vy0 + 1.96) * (1.0 - (q ** T)) / (1.0 - q)
    term2 = 1.96 * T
    return y1 + term1 - term2

def calc_vy_at_tick(T: int, vy0: float) -> float:
    q = 0.98
    return (vy0 + 1.96) * (q ** T) - 1.96

def find_falling_tick(y1: float, y2: float, vy0: float, max_ticks: int = 800):
    low = 1
    high = max_ticks
    best_T = None
    while low <= high:
        mid = (low + high) // 2
        y_mid = calc_y_pos(mid, y1, vy0)
        vy_mid = calc_vy_at_tick(mid, vy0)
        if y_mid <= y2 and vy_mid < 0:
            best_T = mid
            high = mid -1
        else:
            low = mid +1
    if best_T is None:
        return None
    return best_T

def falling_block_calculate(
    x1: float, y1: float, z1: float,
    block: Block,
    mot_y: float,
    tick: int,
    index: int,
    eps: float = 1e-5
) -> Timeline:
    x2 = float(block.x)
    y2 = float(block.y)
    z2 = float(block.z)

    T = find_falling_tick(y1, y2, mot_y, max_ticks=800)
    if T is None:
        raise RuntimeError("Falling time is too long.")

    q = 0.98
    sum_geo = (1.0 - (q ** T)) / (1.0 - q)
    best_vx = (x2 - x1) / sum_geo
    best_vz = (z2 - z1) / sum_geo

    cmd = (
        f"summon minecraft:falling_block ~{x1} ~{y1} ~{z1} "
        f"{{BlockState:{{Name:\"{block.id}\",Properties:{block.get_block_state_str()}}},Motion:[{best_vx:.6f}d,{mot_y:.6f}d,{best_vz:.6f}d],CancelDrop:True,Tags:[\"b{index}\"]}}"
    )
    cmd_setblock = f"setblock ~{block.x} ~{block.y} ~{block.z} {block.name}"
    cmd_kill = f"kill @e[type=falling_block,x={block.x},y={block.y},z={block.z},tag=b{index},limit=1,sort=nearest]"
    return Timeline({tick: [cmd], tick + T - 2: [cmd_setblock, cmd_kill]})
