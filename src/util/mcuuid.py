import uuid


class MCUUID:
    def __init__(self, most_sig: int, least_sig: int):
        """
        Internal storage matches java.util.UUID: two 64-bit longs.

        Args:
            most_sig : (int) 
                Most significant 64 bits
            least_sig : (int)
                Least significant 64 bits
        """
        self.most_sig = most_sig
        self.least_sig = least_sig

    @classmethod
    def get_random(cls) -> MCUUID:
        """Generate standard UUID v4."""
        u = uuid.uuid4()
        return cls(u.time_low | (u.time_mid << 32),
                   (u.time_hi_version << 48) | (u.clock_seq_hi_variant << 40) | (u.clock_seq_low << 32) | u.node)

    @classmethod
    def get_from_number(cls, num: int) -> MCUUID:
        """
        Generate a deterministic UUID from an integer.
        Same input number always yields the same UUID.
        The input number is stored in the lower 64 bits; upper 64 bits uses a fixed seed for uniqueness.

        Args:
            num : (int) 
                integer index / id
        """
        seed = 0x12345678  # fixed 64-bit seed for most significant bits
        most = seed
        least = num & ((1 << 64) - 1)
        return cls(most, least)

    def to_int_array_str(self) -> str:
        """
        Output Minecraft NBT int array string, format: "[I;A,B,C,D]"
        Directly usable in summon command NBT for UUID tag.
        Convert Java-style two longs (most, least) into four signed 32-bit ints.
        """
        def long_to_two_ints(val: int):
            # Extract high/low 32 bits and convert to signed 32-bit integer
            mask32 = 0xFFFFFFFF
            low = val & mask32
            high = (val >> 32) & mask32
            # Convert unsigned 32-bit value to signed
            if low >= 0x80000000:
                low -= 0x100000000
            if high >= 0x80000000:
                high -= 0x100000000
            return high, low

        a, b = long_to_two_ints(self.most_sig)
        c, d = long_to_two_ints(self.least_sig)
        return f"[I;{a},{b},{c},{d}]"

    def to_uuid_string(self) -> str:
        """Output standard hyphenated UUID string, used for `execute as entity <uuid>` selector."""
        u = uuid.UUID(int=(self.most_sig << 64) | self.least_sig)
        return str(u)


class MCUUIDManager():
    """
    Manager class to generate and keep track of sequential deterministic MCUUID instances.
    """

    def __init__(self) -> None:
        self.uuids = []
        self.id = 1 

    def get_new_uuid(self) -> MCUUID:
        """
        Generate a new deterministic UUID using current sequential id,
        increment id counter and append new MCUUID instance to internal list.
        :return: MCUUID instance
        """
        uuid_new = MCUUID.get_from_number(self.id)
        self.id += 1
        self.uuids.append(uuid_new)
        return uuid_new

    