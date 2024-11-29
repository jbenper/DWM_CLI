from utilities.offsets import STAT_OFFSETS
import utilities.decoding as decode


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
