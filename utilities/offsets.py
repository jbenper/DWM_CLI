from dataclasses import dataclass


@dataclass
class OffsetAttribute:
    start_index: int
    end_index: int


class Offsets:
    checksum = OffsetAttribute(0, 2)
    text_speed = OffsetAttribute(40, 41)
    master_name = OffsetAttribute(380, 384)
    gold_in_hand = OffsetAttribute(389, 392)
    gold_in_bank = OffsetAttribute(392, 395)
    inventory = OffsetAttribute(395, 415)
    vault = OffsetAttribute(415, 455)
    time_played = OffsetAttribute(497, 499)

    farm_one = OffsetAttribute(507, 3785)
    farm_two = OffsetAttribute(4388, 7219)

class MonsterOffsets:
    species = OffsetAttribute(9, 10)
    name = OffsetAttribute(1, 5)
    master_name = OffsetAttribute(12, 16)
    stats = OffsetAttribute(75, 98)

class StatOffsets:
    level = OffsetAttribute(0,1)

OFFSETS = Offsets()
MONSTER_OFFSETS = MonsterOffsets()
STAT_OFFSETS = StatOffsets()