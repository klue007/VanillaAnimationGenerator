
from .mcuuid import MCUUIDManager
from .timeline import Timeline
from .block import Block
from .falling_block import falling_block_calculate
from .mcuuid import MCUUID

class MovingEntity():
    """
    Implement a moving entity animation based on teleport command. The entity shall translate from the start position to the target position following a custom-defined motion path.
    """

    def __init__(self, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float, mcuuid: MCUUID) -> None:
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0 
        self.y1 = y1
        self.z0 = z0
        self.z1 = z1
        self.mcuuid = mcuuid


    def get_projectile_timeline(self, vy: float, start_tick: int) -> Timeline:
        """
        Alternative implementation to falling block entities.
        Generate timeline commands for entities to simulate falling block trajectory.
        """
        output = Timeline({})

        vx, vz, total_ticks = falling_block_calculate(self.x0, self.y0, self.z0, self.x1, self.y1, self.z1, vy)

        x = self.x0
        y = self.y0
        z = self.z0
        t = start_tick

        while t < start_tick + total_ticks:
            vy = (vy - 0.04) * 0.98
            vx *= 0.98
            vz *= 0.98

            x += vx
            y += vy
            z += vz

            t += 1
            tp_cmd = f"tp {self.mcuuid.to_uuid_string()} {x:.5f} {y:.5f} {z:.5f}"
            output.add_command(t, tp_cmd)

        return output