from utilities.offsets import PARENT_OFFSETS

import utilities.decoding as decode

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
