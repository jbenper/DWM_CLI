import utilities.decoding as decode
from utilities.offsets import MONSTER_OFFSETS, PARENT_OFFSETS, TRAIT_OFFSETS, RESISTANCE_OFFSETS, STAT_OFFSETS

class MonsterParent:
    def __init__(self, monster_ints: list[int], gender: str):
        self.monster_ints: list[int] = monster_ints
        self.gender: str = gender

        self._species: str = self.get_species_from_save()
        self._name: str = self.get_name_from_save()
        self._master: str = self.get_master_from_save()
        self._breeding_plus: int = self.get_breeding_plus_from_save()

    def __repr__(self):
        return f"""Gender: {self.gender} | Species: {self._species} | Name: {self._name} | Master: {self._master} | Breeding Plus: {self._breeding_plus}"""

    def get_species_from_save(self):
        if self.gender == "Mom":
            return decode.monster_species(
                self.monster_ints[
                    PARENT_OFFSETS.mom_species.start_index : PARENT_OFFSETS.mom_species.end_index
                ][0]
            )
        elif self.gender == "Dad":
            return decode.monster_species(
                self.monster_ints[
                    PARENT_OFFSETS.dad_species.start_index : PARENT_OFFSETS.dad_species.end_index
                ][0]
            )

    @property
    def species(self):
        """Species of Parent"""
        # print("getter of level called")
        return self._species

    @species.setter
    def species(self, value):
        # print("setter of level called")
        self._species = value

    def get_name_from_save(self):
        if self.gender == "Mom":
            return decode.name(
                self.monster_ints[
                    PARENT_OFFSETS.mom_name.start_index : PARENT_OFFSETS.mom_name.end_index
                ]
            )
        elif self.gender == "Dad":
            return decode.name(
                self.monster_ints[
                    PARENT_OFFSETS.dad_name.start_index : PARENT_OFFSETS.dad_name.end_index
                ]
            )

    @property
    def name(self):
        """Name of Parent"""
        # print("getter of level called")
        return self._name

    @name.setter
    def name(self, value):
        # print("setter of level called")
        self._name = value

    def get_master_from_save(self):
        if self.gender == "Mom":
            return decode.name(
                self.monster_ints[
                    PARENT_OFFSETS.mom_master.start_index : PARENT_OFFSETS.mom_master.end_index
                ]
            )
        elif self.gender == "Dad":
            return decode.name(
                self.monster_ints[
                    PARENT_OFFSETS.dad_master.start_index : PARENT_OFFSETS.dad_master.end_index
                ]
            )

    @property
    def master(self):
        """Master of Parent"""
        # print("getter of master called")
        return self._master

    @master.setter
    def master(self, value):
        # print("setter of master called")
        self._master = value

    def get_breeding_plus_from_save(self):
        if self.gender == "Mom":
            return self.monster_ints[
                PARENT_OFFSETS.mom_breeding_plus.start_index : PARENT_OFFSETS.mom_breeding_plus.end_index
            ][0]
        elif self.gender == "Dad":
            return self.monster_ints[
                PARENT_OFFSETS.dad_breeding_plus.start_index : PARENT_OFFSETS.dad_breeding_plus.end_index
            ][0]

    @property
    def breeding_plus(self):
        """Breeding Plus of Parent"""
        # print("getter of level called")
        return self._breeding_plus

    @breeding_plus.setter
    def breeding_plus(self, value):
        # print("setter of level called")
        self._breeding_plus = value


class Personality:
    def __init__(self, personality_ints: list[int]):
        self.personality_ints: list[int] = personality_ints

        self._bravery: int = self.get_bravery_from_save()
        self._caring: int = self.get_caring_from_save()
        self._prudence: int = self.get_prudence_from_save()
        self._motivation: int = self.get_motivation_from_save()

        self.personality = self.calculate_personality()

    def __repr__(self):
        return f"Bravery: {self.bravery} | Caring: {self.caring} | Prudence: {self.prudence} | Motivation: {self.motivation}"

    def calculate_personality(self) -> str:
        return "N/A"

    def get_bravery_from_save(self) -> int:
        return self.personality_ints[
            TRAIT_OFFSETS.bravery.start_index : TRAIT_OFFSETS.bravery.end_index
        ][0]

    @property
    def bravery(self):
        """Current bravery of Monster"""
        # print("getter of bravery called")
        return self._bravery

    @bravery.setter
    def bravery(self, value):
        # print("setter of bravery called")
        self._bravery = value

    def get_caring_from_save(self) -> int:
        return self.personality_ints[
            TRAIT_OFFSETS.caring.start_index : TRAIT_OFFSETS.caring.end_index
        ][0]

    @property
    def caring(self):
        """Current caring of Monster"""
        # print("getter of caring called")
        return self._caring

    @caring.setter
    def caring(self, value):
        # print("setter of caring called")
        self._caring = value

    def get_prudence_from_save(self) -> int:
        return self.personality_ints[
            TRAIT_OFFSETS.prudence.start_index : TRAIT_OFFSETS.prudence.end_index
        ][0]

    @property
    def prudence(self):
        """Current prudence of Monster"""
        # print("getter of prudence called")
        return self._prudence

    @prudence.setter
    def prudence(self, value):
        # print("setter of prudence called")
        self._prudence = value

    def get_motivation_from_save(self) -> int:
        return self.personality_ints[
            TRAIT_OFFSETS.motivation.start_index : TRAIT_OFFSETS.motivation.end_index
        ][0]

    @property
    def motivation(self):
        """Current motivation of Monster"""
        # print("getter of motivation called")
        return self._motivation

    @motivation.setter
    def motivation(self, value):
        # print("setter of motivation called")
        self._motivation = value


class Resistances:
    def __init__(self, resistance_int_list: list[int]):
        self.resistance_int_list = resistance_int_list

        self.fire: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.fire.start_index : RESISTANCE_OFFSETS.fire.end_index
        ][0]
        self.heat: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.heat.start_index : RESISTANCE_OFFSETS.heat.end_index
        ][0]
        self.explosion: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.explosion.start_index : RESISTANCE_OFFSETS.explosion.end_index
        ][0]
        self.wind: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.wind.start_index : RESISTANCE_OFFSETS.wind.end_index
        ][0]
        self.lightning: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.lightning.start_index : RESISTANCE_OFFSETS.lightning.end_index
        ][0]
        self.ice: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.ice.start_index : RESISTANCE_OFFSETS.ice.end_index
        ][0]
        self.accuracy: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.accuracy.start_index : RESISTANCE_OFFSETS.accuracy.end_index
        ][0]
        self.sleep: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.sleep.start_index : RESISTANCE_OFFSETS.sleep.end_index
        ][0]
        self.death: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.death.start_index : RESISTANCE_OFFSETS.death.end_index
        ][0]
        self.mp: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.mp.start_index : RESISTANCE_OFFSETS.mp.end_index
        ][0]
        self.spellblock: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.spellblock.start_index : RESISTANCE_OFFSETS.spellblock.end_index
        ][0]
        self.confusion: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.confusion.start_index : RESISTANCE_OFFSETS.confusion.end_index
        ][0]
        self.defdown: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.defdown.start_index : RESISTANCE_OFFSETS.defdown.end_index
        ][0]
        self.agldown: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.agldown.start_index : RESISTANCE_OFFSETS.agldown.end_index
        ][0]
        self.sacrifice: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.sacrifice.start_index : RESISTANCE_OFFSETS.sacrifice.end_index
        ][0]
        self.megamagic: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.megamagic.start_index : RESISTANCE_OFFSETS.megamagic.end_index
        ][0]
        self.firebreath: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.firebreath.start_index : RESISTANCE_OFFSETS.firebreath.end_index
        ][0]
        self.icebreath: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.icebreath.start_index : RESISTANCE_OFFSETS.icebreath.end_index
        ][0]
        self.poison: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.poison.start_index : RESISTANCE_OFFSETS.poison.end_index
        ][0]
        self.paralyze: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.paralyze.start_index : RESISTANCE_OFFSETS.paralyze.end_index
        ][0]
        self.curse: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.curse.start_index : RESISTANCE_OFFSETS.curse.end_index
        ][0]
        self.miss_a_turn: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.miss_a_turn.start_index : RESISTANCE_OFFSETS.miss_a_turn.end_index
        ][0]
        self.danceblock: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.danceblock.start_index : RESISTANCE_OFFSETS.danceblock.end_index
        ][0]
        self.breathblock: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.breathblock.start_index : RESISTANCE_OFFSETS.breathblock.end_index
        ][0]
        self.aid: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.aid.start_index : RESISTANCE_OFFSETS.aid.end_index
        ][0]
        self.gigaslash: int = self.resistance_int_list[
            RESISTANCE_OFFSETS.gigaslash.start_index : RESISTANCE_OFFSETS.gigaslash.end_index
        ][0]

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(f'{key}={value!r}' for key, value in self.__dict__.items() if key != "resistance_int_list")})"


class MonsterStats:
    def __init__(self, stats_ints: list[int]):
        self.stats_ints: list[int] = stats_ints
        self._level: int = self.get_level_from_save()
        self._max_level: int = self.get_max_level_from_save()
        self._total_exp: int = self.get_total_exp_from_save()

        self._current_hp: int = self.get_current_hp_from_save()
        self._total_hp: int = self.get_total_hp_from_save()

        self._current_mp: int = self.get_current_mp_from_save()
        self._total_mp: int = self.get_total_mp_from_save()

        self._attack: int = self.get_attack_from_save()
        self._defense: int = self.get_defense_from_save()
        self._agility: int = self.get_agility_from_save()
        self._intelligence: int = self.get_intelligence_from_save()
        self._wild: int = self.get_wild_from_save()

        self._breeding_plus: int = self.get_breeding_plus_from_save()

    def __repr__(self):
        return f"""Level: {self.level} | Max Level: {self.max_level} | Total Ex: {self.total_exp} | Breeding Plus: {self.breeding_plus} | Current HP: {self.current_hp} | Total HP: {self.total_hp} | Current MP: {self.current_mp} | Total MP: {self.total_mp} | ATK: {self.attack} | DEF: {self.defense} | AGL: {self.agility} | INT: {self.intelligence} | WLD: {self.wild}"""

    def get_level_from_save(self) -> int:
        return self.stats_ints[
            STAT_OFFSETS.level.start_index : STAT_OFFSETS.level.end_index
        ][0]

    @property
    def level(self):
        """Current Level of Monster"""
        # print("getter of level called")
        return self._level

    @level.setter
    def level(self, value):
        # print("setter of level called")
        self._level = value

    def get_max_level_from_save(self) -> int:
        return self.stats_ints[
            STAT_OFFSETS.max_level.start_index : STAT_OFFSETS.max_level.end_index
        ][0]

    @property
    def max_level(self):
        """Max Level of Monster"""
        # print("getter of max_level called")
        return self._max_level

    @max_level.setter
    def max_level(self, value):
        # print("setter of max_level called")
        self._max_level = value

    def get_total_exp_from_save(self) -> int:
        exp_list = self.stats_ints[
            STAT_OFFSETS.total_exp.start_index : STAT_OFFSETS.total_exp.end_index
        ]

        return decode.little_to_big(exp_list)

    @property
    def total_exp(self):
        """Total Exp of Monster"""
        # print("getter of total_exp called")
        return self._total_exp

    @total_exp.setter
    def total_exp(self, value):
        # print("setter of total_exp called")
        self._total_exp = value

    def get_current_hp_from_save(self) -> int:
        current_hp_list = self.stats_ints[
            STAT_OFFSETS.current_hp.start_index : STAT_OFFSETS.current_hp.end_index
        ]

        return decode.little_to_big(current_hp_list)

    @property
    def current_hp(self):
        """Current HP of Monster"""
        # print("getter of current_hp called")
        return self._current_hp

    @current_hp.setter
    def current_hp(self, value):
        # print("setter of current_hp called")
        self._current_hp = value

    def get_total_hp_from_save(self) -> int:
        total_hp_list = self.stats_ints[
            STAT_OFFSETS.total_hp.start_index : STAT_OFFSETS.total_hp.end_index
        ]

        return decode.little_to_big(total_hp_list)

    @property
    def total_hp(self):
        """Total HP of Monster"""
        # print("getter of total_hp called")
        return self._total_hp

    @total_hp.setter
    def total_hp(self, value):
        # print("setter of total_hp called")
        self._total_hp = value

    def get_current_mp_from_save(self) -> int:
        current_mp_list = self.stats_ints[
            STAT_OFFSETS.current_mp.start_index : STAT_OFFSETS.current_mp.end_index
        ]

        return decode.little_to_big(current_mp_list)

    @property
    def current_mp(self):
        """Current MP of Monster"""
        # print("getter of current_mp called")
        return self._current_mp

    @current_mp.setter
    def current_mp(self, value):
        # print("setter of current_mp called")
        self._current_mp = value

    def get_total_mp_from_save(self) -> int:
        total_mp_list = self.stats_ints[
            STAT_OFFSETS.total_mp.start_index : STAT_OFFSETS.total_mp.end_index
        ]

        return decode.little_to_big(total_mp_list)

    @property
    def total_mp(self):
        """Total MP of Monster"""
        # print("getter of total_mp called")
        return self._total_mp

    @total_mp.setter
    def total_mp(self, value):
        # print("setter of total_mp called")
        self._total_mp = value

    def get_attack_from_save(self) -> int:
        attack_list: list[int] = self.stats_ints[
            STAT_OFFSETS.attack.start_index : STAT_OFFSETS.attack.end_index
        ]
        return decode.little_to_big(attack_list)

    @property
    def attack(self):
        """Attack of Monster"""
        # print("getter of attack called")
        return self._attack

    @attack.setter
    def attack(self, value):
        # print("setter of attack called")
        self._attack = value

    def get_defense_from_save(self) -> int:
        defense_list: list[int] = self.stats_ints[
            STAT_OFFSETS.defense.start_index : STAT_OFFSETS.defense.end_index
        ]
        return decode.little_to_big(defense_list)

    @property
    def defense(self):
        """Defense of Monster"""
        # print("getter of defense called")
        return self._defense

    @defense.setter
    def defense(self, value):
        # print("setter of defense called")
        self._defense = value

    def get_agility_from_save(self) -> int:
        agility_list: list[int] = self.stats_ints[
            STAT_OFFSETS.agility.start_index : STAT_OFFSETS.agility.end_index
        ]
        return decode.little_to_big(agility_list)

    @property
    def agility(self):
        """Agility of Monster"""
        # print("getter of agility called")
        return self._agility

    @agility.setter
    def agility(self, value):
        # print("setter of agility called")
        self._agility = value

    def get_intelligence_from_save(self) -> int:
        intelligence_list: list[int] = self.stats_ints[
            STAT_OFFSETS.intelligence.start_index : STAT_OFFSETS.intelligence.end_index
        ]
        return decode.little_to_big(intelligence_list)

    @property
    def intelligence(self):
        """Intelligence of Monster"""
        # print("getter of intelligence called")
        return self._intelligence

    @intelligence.setter
    def intelligence(self, value):
        # print("setter of intelligence called")
        self._intelligence = value

    def get_wild_from_save(self) -> int:
        wild_list: list[int] = self.stats_ints[
            STAT_OFFSETS.wild.start_index : STAT_OFFSETS.wild.end_index
        ]
        return decode.little_to_big(wild_list)

    @property
    def wild(self):
        """Wild of Monster"""
        # print("getter of wild called")
        return self._wild

    @wild.setter
    def wild(self, value):
        # print("setter of wild called")
        self._wild = value

    def get_breeding_plus_from_save(self) -> int:
        return self.stats_ints[
            STAT_OFFSETS.breeding_plus.start_index : STAT_OFFSETS.breeding_plus.end_index
        ][0]

    @property
    def breeding_plus(self):
        """Breeding Plus of Monster"""
        # print("getter of breeding_plus called")
        return self._breeding_plus

    @breeding_plus.setter
    def breeding_plus(self, value):
        # print("setter of breeding_plus called")
        self._breeding_plus = value


class Monster:
    def __init__(self, monster_int_list: list[int], farm_index: int):
        self.monster_int_list: list[int] = monster_int_list
        self.species: str = self.get_species()
        self.name: str = self.get_name()
        self.location: str = self.get_location()
        self.farm_index: int = farm_index
        self.stats: MonsterStats = self.get_stats()
        self.status: str = self.get_status()

        self.personality: Personality = self.get_personality_values()
        self.resistances: Resistances = self.get_resistances()

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

    def get_personality_values(self) -> Personality:
        return Personality(
            self.monster_int_list[
                MONSTER_OFFSETS.personality.start_index : MONSTER_OFFSETS.personality.end_index
            ]
        )

    def get_resistances(self) -> Resistances:
        return Resistances(
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
