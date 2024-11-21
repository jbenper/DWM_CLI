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
    party_indices = OffsetAttribute(456, 459)
    time_played = OffsetAttribute(497, 499)

    farm_one = OffsetAttribute(507, 3785)
    farm_two = OffsetAttribute(4388, 7219)


class MonsterOffsets:
    species = OffsetAttribute(9, 10)
    name = OffsetAttribute(1, 5)
    master_name = OffsetAttribute(12, 16)
    stats = OffsetAttribute(75, 99)


class StatOffsets:
    level = OffsetAttribute(0, 1)
    max_level = OffsetAttribute(1, 2)
    total_exp = OffsetAttribute(2, 5)

    current_hp = OffsetAttribute(5, 7)
    total_hp = OffsetAttribute(7, 9)
    current_mp = OffsetAttribute(9, 11)
    total_mp = OffsetAttribute(11, 13)

    attack = OffsetAttribute(13, 15)
    defense = OffsetAttribute(15, 17)
    agility = OffsetAttribute(17, 19)
    intelligence = OffsetAttribute(19, 21)
    wild = OffsetAttribute(21, 23)

    breeding_plus = OffsetAttribute(23, 24)  

class ParentOffsets:
    dad_name: OffsetAttribute = OffsetAttribute(131, 135)
    dad_species: OffsetAttribute = OffsetAttribute(21, 22)
    dad_master: OffsetAttribute = OffsetAttribute(23, 27)
    dad_breeding_plus: OffsetAttribute = OffsetAttribute(139, 140)

    mom_name: OffsetAttribute = OffsetAttribute(140, 144)
    mom_species: OffsetAttribute = OffsetAttribute(22, 23)
    mom_master: OffsetAttribute = OffsetAttribute(32, 36)
    mom_breeding_plus: OffsetAttribute = OffsetAttribute(148, 149)



OFFSETS = Offsets()
MONSTER_OFFSETS = MonsterOffsets()
STAT_OFFSETS = StatOffsets()
PARENT_OFFSETS = ParentOffsets()
