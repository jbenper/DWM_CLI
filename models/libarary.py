from utilities.offsets import MonsterLibraryOffsets

class MonsterLibrary:
    def __init__(self, binary_data: list[int] = None):
        self.bits = bytearray(27)

        if binary_data:
            self.bits = bytearray(binary_data)

    def __repr__(self):
        return f"Library: {self.get_number_tamed()}"

    def is_monster_tamed(self, monster: MonsterLibraryOffsets) -> bool:
        """Check if a specific monster is tamed."""
        byte_index = monster.value // 8
        bit_index = monster.value % 8

        return bool(self.bits[byte_index] & (1 << bit_index))

    def set_monster_tamed(self, monster: MonsterLibraryOffsets, tamed: bool = True):
        """Set a monster's tamed status."""
        byte_index = monster.value // 8
        bit_index = monster.value % 8

        if tamed:
            self.bits[byte_index] |= 1 << bit_index
        else:
            self.bits[byte_index] &= ~(1 << bit_index)

    def get_all_tamed_monsters(self) -> list[MonsterLibraryOffsets]:
        """Return a list of all tamed monsters."""
        return [
            monster
            for monster in MonsterLibraryOffsets
            if self.is_monster_tamed(monster)
        ]

    def get_tamed_status_dict(self) -> dict[str, bool]:
        """Return a dictionary of all monsters and their tamed status."""
        return {
            monster.name: self.is_monster_tamed(monster)
            for monster in MonsterLibraryOffsets
        }

    def get_number_tamed(self) -> str:
        return f"{len(self.get_all_tamed_monsters())} / 214"

    def to_ints(self) -> list[int]:
        """Convert the collection back to bytes for saving."""
        return list(self.bits)

