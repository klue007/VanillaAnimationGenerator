
from .timeline import Timeline
from .falling_block import falling_block_calculate
from .mcuuid import MCUUID
import math

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
            tp_cmd = f"tp {self.mcuuid.to_uuid_string()} ~{x:.3f} ~{y:.3f} ~{z:.3f}"
            output.add_command(t, tp_cmd)

        return output


    def get_straight_line_timeline(self, start_tick: int, end_tick: int) -> Timeline:
        output = Timeline({})
        delta_tick = end_tick - start_tick
        for tick in range(0, delta_tick+1):
            t = tick / delta_tick
            x = self.x0 + (self.x1 - self.x0) * t
            y = self.y0 + (self.y1 - self.y0) * t
            z = self.z0 + (self.z1 - self.z0) * t
            output.add_command(tick + start_tick, f"tp {self.mcuuid.to_uuid_string()} ~{x:.3f} ~{y:.3f} ~{z:.3f}")
        return output


    def get_parabolic_timeline(self, dy: float, start_tick: int, end_tick: int) -> Timeline:
        output = Timeline({})
        delta_tick = end_tick - start_tick
        for tick in range(0, delta_tick+1):
            t = tick / delta_tick
            x = self.x0 + (self.x1 - self.x0) * t
            y = self.y0 * (1 - t) + self.y1 * t + dy * 4 * t * (1 - t)
            z = self.z0 + (self.z1 - self.z0) * t
            output.add_command(tick + start_tick, f"tp {self.mcuuid.to_uuid_string()} ~{x:.3f} ~{y:.3f} ~{z:.3f}")
        return output
    

    def get_vortex_parabolic_timeline(self, dy: float, start_tick: int, end_tick: int, center_x: float, center_z: float) -> Timeline:
        output = Timeline({})
        delta_tick = end_tick - start_tick
        for tick in range(0, delta_tick+1):
            t = tick / delta_tick
            theta0 = math.atan2(self.z0 - center_z, self.x0 - center_x)
            theta1 = math.atan2(self.z1 - center_z, self.x1 - center_x)
            delta_raw = theta1 - theta0
            delta = (delta_raw + math.pi) % (2 * math.pi) - math.pi
            theta = theta0 + delta * t
            r0 = math.hypot(self.x0 - center_x, self.z0 - center_z)
            r1 = math.hypot(self.x1 - center_x, self.z1 - center_z)
            r = r0 + (r1 - r0) * t
            x = r * math.cos(theta)
            y = self.y0 * (1 - t) + self.y1 * t + dy * 4 * t * (1 - t)
            z = r * math.sin(theta)
            output.add_command(tick + start_tick, f"tp {self.mcuuid.to_uuid_string()} ~{x:.3f} ~{y:.3f} ~{z:.3f}")
        return output
        