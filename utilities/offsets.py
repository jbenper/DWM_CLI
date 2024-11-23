from dataclasses import dataclass


@dataclass
class OffsetAttribute:
    start_index: int
    end_index: int


class SaveOffsets:
    checksum = OffsetAttribute(0, 2)
    text_speed = OffsetAttribute(40, 41)
    tiny_medals = OffsetAttribute(61, 62)
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
    location = OffsetAttribute(0, 1)
    name = OffsetAttribute(1, 5)
    species = OffsetAttribute(9, 10)
    family = OffsetAttribute(10, 11)
    gender = OffsetAttribute(11, 12)
    master_name = OffsetAttribute(12, 16)
    learned_skills = OffsetAttribute(41, 49)
    unlearned_skills = OffsetAttribute(49, 74)
    stats = OffsetAttribute(75, 99)
    status = OffsetAttribute(99, 100)

    personality = OffsetAttribute(100, 104)
    resistances = OffsetAttribute(104, 130)


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
    dad_name = OffsetAttribute(131, 135)
    dad_species = OffsetAttribute(21, 22)
    dad_master = OffsetAttribute(23, 27)
    dad_breeding_plus = OffsetAttribute(139, 140)

    mom_name = OffsetAttribute(140, 144)
    mom_species = OffsetAttribute(22, 23)
    mom_master = OffsetAttribute(32, 36)
    mom_breeding_plus = OffsetAttribute(148, 149)


class TraitOffsets:
    bravery = OffsetAttribute(0, 1)
    caring = OffsetAttribute(1, 2)
    prudence = OffsetAttribute(2, 3)
    motivation = OffsetAttribute(3, 4)

class ResistanceOffsets:
    fire = OffsetAttribute(0, 1)
    heat = OffsetAttribute(1, 2)
    explosion = OffsetAttribute(2, 3)
    wind = OffsetAttribute(3, 4)
    lightning = OffsetAttribute(4, 5)
    ice = OffsetAttribute(5, 6)
    accuracy = OffsetAttribute(6, 7)
    sleep = OffsetAttribute(7, 8)
    death = OffsetAttribute(8, 9)
    mp = OffsetAttribute(9, 10)
    spellblock = OffsetAttribute(10, 11)
    confusion = OffsetAttribute(11, 12)
    defdown = OffsetAttribute(12, 13)
    agldown = OffsetAttribute(13, 14)
    sacrifice = OffsetAttribute(14, 15)
    megamagic = OffsetAttribute(15, 16)
    firebreath = OffsetAttribute(16, 17)
    icebreath = OffsetAttribute(17, 18)
    poison = OffsetAttribute(18, 19)
    paralyze = OffsetAttribute(19, 20)
    curse = OffsetAttribute(20, 21)
    miss_a_turn = OffsetAttribute(21, 22)
    danceblock = OffsetAttribute(22, 23)
    breathblock = OffsetAttribute(23, 24)
    aid = OffsetAttribute(24, 25)
    gigaslash = OffsetAttribute(25, 26)

SAVE_OFFSETS = SaveOffsets()
MONSTER_OFFSETS = MonsterOffsets()
STAT_OFFSETS = StatOffsets()
PARENT_OFFSETS = ParentOffsets()
TRAIT_OFFSETS = TraitOffsets()
RESISTANCE_OFFSETS = ResistanceOffsets()