from models.monster_model import Monster

class Farm:
    def __init__(self, farm_int_list: list):
        self.farm_int_list: list[int] = farm_int_list
        self.farm_number: int = self.get_farm_number()
        self.monsters: list[Monster] = self.get_farm_monsters()

    def __repr__(self):
        disp_monsters: list[Monster] = [
            monster for monster in self.monsters if monster.exists()
        ]

        while len(disp_monsters) < 19:
            disp_monsters.append("Monster()")

        return f"Farm {self.farm_number}: {disp_monsters}"

    def get_farm_number(self) -> int:
        if len(self.farm_int_list) > 3200:
            return 1

        return 2

    def get_farm_monsters(self) -> list[Monster]:
        chunked_monster_int_list: list[list[int]] = [
            self.farm_int_list[x : x + 149]
            for x in range(0, len(self.farm_int_list), 149)
        ]

        monster_list = [
            Monster(x, ind) for ind, x in enumerate(chunked_monster_int_list)
        ]

        return monster_list
