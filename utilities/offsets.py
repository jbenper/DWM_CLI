from dataclasses import dataclass


@dataclass
class OffsetAttribute:
    start_index: int
    end_index: int


class Offsets:
    checksum: OffsetAttribute = OffsetAttribute(0, 2)
    text_speed: OffsetAttribute = OffsetAttribute(40, 41)
    master_name: OffsetAttribute = OffsetAttribute(380, 384)
    gold_in_hand: OffsetAttribute = OffsetAttribute(389, 392)
    gold_in_bank: OffsetAttribute = OffsetAttribute(392, 395)
    inventory: OffsetAttribute = OffsetAttribute(395, 415)
    vault: OffsetAttribute = OffsetAttribute(415, 455)
    time_played: OffsetAttribute = OffsetAttribute(497, 499)

    farm_one: OffsetAttribute = OffsetAttribute(507, 3785)
    farm_two: OffsetAttribute = OffsetAttribute(4388, 7219)

class MonsterOffsets:
    species: OffsetAttribute = OffsetAttribute(9, 10)
    name: OffsetAttribute = OffsetAttribute(1, 5)

OFFSETS = Offsets()
MONSTER_OFFSETS = MonsterOffsets()