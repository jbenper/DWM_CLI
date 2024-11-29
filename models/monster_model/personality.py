from utilities.offsets import TRAIT_OFFSETS
import utilities.decoding as decode

class MonsterPersonality:
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
