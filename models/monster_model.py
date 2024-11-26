from utilities.offsets import MONSTER_OFFSETS

from models.monster.parents import MonsterParent
from models.monster.resistances import MonsterResistances
from models.monster.stats import MonsterStats
from models.monster.personality import MonsterPersonality

import utilities.decoding as decode

class Monster:
    def __init__(self, monster_int_list: list[int], farm_index: int):
        self.monster_int_list: list[int] = monster_int_list
        self.species: str = self.get_species()
        self.name: str = self.get_name()
        self.location: str = self.get_location()
        self.farm_index: int = farm_index
        self.stats: MonsterStats = self.get_stats()
        self.status: str = self.get_status()

        self.personality: MonsterPersonality = self.get_personality_values()
        self.resistances: MonsterResistances = self.get_resistances()

        self.learned_skills: list[str] = self.get_learned_skills()
        self.unlearned_skills: list[str] = self.get_unlearned_skills()

    def __repr__(self):
        return f"Monster({self.species}, {self.name}, {self.location}, {self.status})"

    def get_species(self) -> str:
        return decode.monster_species(
            self.monster_int_list[
                MONSTER_OFFSETS.species.start_index : MONSTER_OFFSETS.species.end_index
            ][0]
        )

    def get_name(self) -> str:
        return decode.name(
            self.monster_int_list[
                MONSTER_OFFSETS.name.start_index : MONSTER_OFFSETS.name.end_index
            ]
        )

    def get_learned_skills(self) -> list[str]:
        return decode.skills(
            self.monster_int_list[
                MONSTER_OFFSETS.learned_skills.start_index : MONSTER_OFFSETS.learned_skills.end_index
            ]
        )

    def get_unlearned_skills(self) -> list[str]:
        return decode.skills(
            self.monster_int_list[
                MONSTER_OFFSETS.unlearned_skills.start_index : MONSTER_OFFSETS.unlearned_skills.end_index
            ]
        )

    def get_location(self) -> str:
        location_int = self.monster_int_list[
            MONSTER_OFFSETS.location.start_index : MONSTER_OFFSETS.location.end_index
        ][0]

        if location_int == 0:
            return "Bred"
        elif location_int == 1:
            return "Farm"
        elif location_int == 2:
            return "Party"

    def get_family(self) -> str:
        return decode.monster_family(
            self.monster_int_list[
                MONSTER_OFFSETS.family.start_index : MONSTER_OFFSETS.family.end_index
            ][0]
        )

    def get_stats(self) -> MonsterStats:
        return MonsterStats(
            self.monster_int_list[
                MONSTER_OFFSETS.stats.start_index : MONSTER_OFFSETS.stats.end_index
            ]
        )

    def get_status(self) -> str:
        status_int: int = self.monster_int_list[
            MONSTER_OFFSETS.status.start_index : MONSTER_OFFSETS.status.end_index
        ][0]

        if status_int == 0:
            return "Hatched"
        elif status_int == 1:
            return "Egg"

    def get_personality_values(self) -> MonsterPersonality:
        return MonsterPersonality(
            self.monster_int_list[
                MONSTER_OFFSETS.personality.start_index : MONSTER_OFFSETS.personality.end_index
            ]
        )

    def get_resistances(self) -> MonsterResistances:
        return MonsterResistances(
            self.monster_int_list[
                MONSTER_OFFSETS.resistances.start_index : MONSTER_OFFSETS.resistances.end_index
            ]
        )

    def get_master_name(self) -> str:
        return decode.name(
            self.monster_int_list[
                MONSTER_OFFSETS.master_name.start_index : MONSTER_OFFSETS.master_name.end_index
            ]
        )

    def get_dad(self) -> MonsterParent:
        return MonsterParent(self.monster_int_list, "Dad")

    def get_mom(self) -> MonsterParent:
        return MonsterParent(self.monster_int_list, "Mom")

    def exists(self) -> bool:
        if self.name == "0000":
            if self.species == "DrakSlime":
                if self.learned_skills == ["Blaze"] * 8:
                    return False
        return True
