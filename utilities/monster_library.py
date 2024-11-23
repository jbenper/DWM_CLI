from enum import Enum
from typing import List, Dict
import struct

class Monster(Enum):
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


class MonsterCollection:
    def __init__(self, binary_data: list[int] = None):
        self.num_bytes = 27
        self.bits = bytearray(self.num_bytes)
        if binary_data:
            self.bits = bytearray(binary_data)
    
    def is_monster_tamed(self, monster: Monster) -> bool:
        """Check if a specific monster is tamed."""
        byte_index = monster.value // 8
        bit_index = monster.value % 8
        return bool(self.bits[byte_index] & (1 << bit_index))
    
    def set_monster_tamed(self, monster: Monster, tamed: bool = True):
        """Set a monster's tamed status."""
        byte_index = monster.value // 8
        bit_index = monster.value % 8
        if tamed:
            self.bits[byte_index] |= (1 << bit_index)
        else:
            self.bits[byte_index] &= ~(1 << bit_index)
    
    def get_all_tamed_monsters(self) -> List[Monster]:
        """Return a list of all tamed monsters."""
        return [monster for monster in Monster if self.is_monster_tamed(monster)]
    
    def get_tamed_status_dict(self) -> Dict[str, bool]:
        """Return a dictionary of all monsters and their tamed status."""
        return {monster.name: self.is_monster_tamed(monster) for monster in Monster}
    
    def get_number_tamed(self) -> str:
        return f"{len(self.get_all_tamed_monsters())} / 214"
    
    def to_bytes(self) -> bytes:
        """Convert the collection back to bytes for saving."""
        return list(self.bits)

def read_monster_collection(library_ints: list[int]) -> MonsterCollection:
    """Read monster collection from a save file at specified offset."""
    return MonsterCollection(library_ints)

# Example usage:
if __name__ == "__main__":
    # Read the save file
    collection = read_monster_collection([255, 255, 255, 253, 251, 127, 221, 236, 223, 255, 238, 223, 118, 195, 255, 254, 127, 253, 151, 183, 127, 223, 251, 25, 255, 130, 0])  # Replace with actual offset
    
    # print(collection)
    print(collection.get_number_tamed())

    # Check if a monster is tamed
    if collection.is_monster_tamed(Monster.Healer):
        print("Tamed!")
    else:
        print("Not Tamed!")
    
    # Tame a new monster
    # collection.set_monster_tamed(Monster.Slime, True)
    
    # # Untame a monster
    collection.set_monster_tamed(Monster.Healer, False)

    if collection.is_monster_tamed(Monster.Healer):
        print("Tamed!")
    else:
        print("Not Tamed!")

    
    print(collection.to_bytes())
    print(collection.get_number_tamed())

    
    # # Get all tamed monsters
    # tamed_monsters = collection.get_all_tamed_monsters()
    # for monster in tamed_monsters:
    #     print(f"{monster.name} is tamed")
