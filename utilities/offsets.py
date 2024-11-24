from dataclasses import dataclass
from enum import Enum

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
    monster_library = OffsetAttribute(462, 489)
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

class MonsterLibraryOffsets(Enum):
    BoxSlime = 0  
    Babble = 1  
    SlimeNite = 2  
    Snaily = 3  
    TreeSlime = 4  
    WingSlime = 5  
    SpotSlime = 6  
    DrakSlime = 7  
    KingSlime = 8  
    SpotKing = 9  
    Slabbit = 10  
    SlimeBorg = 11  
    RockSlime = 12  
    FangSlime = 13  
    Healer = 14  
    Slime = 15  
    Gasgon = 16  
    Pteranod = 17  
    Tortragon = 18  
    DragonKid = 19  
    GoldSlime = 20  
    MetalKing = 21  
    Metabble = 22  
    Metaly = 23  
    Rayburn = 24  
    MadDragon = 25  
    MiniDrak = 26  
    Dragon = 27  
    Swordgon = 28  
    Poisongon = 29  
    LizardMan = 30  
    FairyDrak = 31  
    WingSnake = 32  
    Crestpent = 33  
    GreatDrak = 34  
    Spikerous = 35  
    KingCobra = 36  
    Andreal = 37  
    LizardFly = 38  
    Chamelgon = 39  
    Catfly = 40  
    Almiraj = 41  
    Tonguella = 42  
    Divinegon = 43  
    SkyDragon = 44  
    BattleRex = 45  
    Orochi = 46  
    Coatol = 47  
    IronTurt = 48  
    SuperTen = 49  
    Anteater = 50  
    WindBeast = 51  
    Skullroo = 52  
    GulpBeast = 53  
    Saccer = 54  
    PillowRat = 55  
    Goategon = 56  
    Unicorn = 57  
    FairyRat = 58  
    MadGopher = 59  
    Yeti = 60  
    Grizzly = 61  
    HammerMan = 62  
    Mommonja = 63  
    Wyvern = 64  
    Picky = 65  
    BigEye = 66  
    MadCat = 67  
    DarkHorn = 68  
    KingLeo = 69  
    Trumpeter = 70  
    WildApe = 71  
    BigRoost = 72  
    Dracky = 73  
    MistyWing = 74  
    MadRaven = 75  
    MadPecker = 76  
    DuckKite = 77  
    FloraJay = 78  
    BullBird = 79  
    WhipBird = 80  
    ZapBird = 81  
    Phoenix = 82  
    Blizzardy = 83  
    MadCondor = 84  
    MadGoose = 85  
    LandOwl = 86  
    StubBird = 87  
    Gulpple = 88  
    CactiBall = 89  
    WingTree = 90  
    FloraMan = 91  
    FireWeed = 92  
    MadPlant = 93  
    RainHawk = 94  
    FunkyBird = 95  
    HerbMan = 96  
    FaceTree = 97  
    TreeBoy = 98  
    DanceVegi = 99  
    Oniono = 100  
    StubSuck = 101  
    AmberWeed = 102  
    Toadstool = 103  
    Catapila = 104  
    GiantSlug = 105  
    Watabou = 106  
    Rosevine = 107  
    Snapper = 108  
    ManEater = 109  
    EvilSeed = 110  
    BeanMan = 111  
    GoHopper = 112  
    ArmyAnt = 113  
    StagBug = 114  
    Lipsy = 115  
    GiantWorm = 116  
    WeedBug = 117  
    Butterfly = 118  
    Gophecada = 119  
    EyeBall = 120  
    DarkEye = 121  
    Demonite = 122  
    AgDevil = 123  
    ArcDemon = 124  
    Pixy = 125  
    Digster = 126  
    Armorpion = 127  
    HornBeet = 128  
    MadHornet = 129  
    ArmyCrab = 130  
    Droll = 131  
    GiantMoth = 132  
    Eyeder = 133  
    ArmorPede = 134  
    TailEater = 135  
    GoatHorn = 136  
    Lionex = 137  
    MedusaEye = 138  
    Gremlin = 139  
    OneEyeClown = 140  
    EvilBeast = 141  
    SkulRider = 142  
    Orc = 143  
    Centasaur = 144  
    Gigantes = 145  
    MadKnight = 146  
    Akubar = 147  
    Grendal = 148  
    ChopClown = 149  
    GateGuard = 150  
    Ogre = 151  
    Mummy = 152  
    RotRaven = 153  
    Putrepup = 154  
    Skullgon = 155  
    Spooky = 156  
    Durran = 157  
    Jamirus = 158  
    EvilArmor = 159  
    WindMerge = 160  
    MadSpirit = 161  
    NiteWhip = 162  
    Mudron = 163  
    Hork = 164  
    Shadow = 165  
    DeadNite = 166  
    DarkCrab = 167  
    JewelBag = 168  
    Copycat = 169  
    Servant = 170  
    Skeletor = 171  
    BoneSlave = 172  
    WhiteKing = 173  
    DeadNoble = 174  
    Reaper = 175  
    Goopi = 176  
    RogueNite = 177  
    MadMirror = 178  
    SpikyBoy = 179  
    Facer = 180  
    CoilBird = 181  
    MadCandle = 182  
    EvilWand = 183  
    Gismo = 184  
    EvilPot = 185  
    Roboster = 186  
    CurseLamp = 187  
    SabreMan = 188  
    Balzak = 189  
    MetalDrak = 190  
    Voodoll = 191  
    GoldGolem = 192  
    BombCrag = 193  
    StoneMan = 194  
    Golem = 195  
    MudDoll = 196  
    Mimic = 197  
    IceMan = 198  
    LavaMan = 199  
    Esterk = 200  
    Pizzaro = 201  
    Zoma = 202  
    Baramos = 203  
    Sidoh = 204  
    Hargon = 205  
    DracoLord_2 = 206  
    DracoLord = 207  
    BLANK = 208  
    DarkDrium = 209  
    DeathMore_3 = 210  
    DeathMore_2 = 211  
    DeathMore = 212  
    Mudou = 213  
    Mirudraas_2 = 214  
    Mirudraas = 215  


SAVE_OFFSETS = SaveOffsets()
MONSTER_OFFSETS = MonsterOffsets()
STAT_OFFSETS = StatOffsets()
PARENT_OFFSETS = ParentOffsets()
TRAIT_OFFSETS = TraitOffsets()
RESISTANCE_OFFSETS = ResistanceOffsets()
