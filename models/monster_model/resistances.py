from utilities.offsets import RESISTANCE_OFFSETS
import utilities.decoding as decode

class MonsterResistances:
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
