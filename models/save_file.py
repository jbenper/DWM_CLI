from utilities.offsets import SAVE_OFFSETS
import utilities.decoding as decode

from models.monster_library import MonsterLibrary
from models.monster import Monster
from models.farm import Farm

from pathlib import Path

class SaveFile:
    def __init__(self, file_loc: str):
        self.file_loc: str = file_loc

        self.save_data: list[int] = self.open_file()

    def __repr__(self):
        return f"""Save File: {self.file_loc} | SaveLength: {len(self.save_data)} | Master Name: {self.get_master_name()}
Time Played: {self.get_time_played()} | Gold Amount: {self.get_gold_in_hand()} | Bank Amount: {self.get_gold_in_bank()}
Text Speed: {self.get_text_speed()} | {self.get_monster_library_from_save()} | Tiny Medal Count: {self.get_tiny_medals_from_save()}

Current Party: {self.get_current_party()}

{self.get_farm_one()}

{self.get_farm_two()}

Inventory: {self.get_inventory()}
Vault: {self.get_vault_items()}"""

    def open_file(self) -> list[int]:
        path_to_save = Path(self.file_loc)

        with path_to_save.open("rb") as save_file:
            save_bytes: list[int] = [int_byte for int_byte in (save_file.read())]
        
        if len(save_bytes) != 8192:
            raise Exception("Save File Length does not match .sav format")
        
        return save_bytes


    def get_master_name(self) -> str:
        return decode.name(
            self.save_data[
                SAVE_OFFSETS.master_name.start_index : SAVE_OFFSETS.master_name.end_index
            ]
        )

    def get_gold_in_hand(self) -> int:
        big_end_hex_list = list(
            map(
                hex,
                self.save_data[
                    SAVE_OFFSETS.gold_in_hand.start_index : SAVE_OFFSETS.gold_in_hand.end_index
                ],
            )
        )

        little_end_hex_string = "0x" + "".join(
            [format(int(c, 16), "02X") for c in reversed(big_end_hex_list)]
        )

        return int(little_end_hex_string, 16)

    def get_gold_in_bank(self) -> int:
        big_end_hex_list = list(
            map(
                hex,
                self.save_data[
                    SAVE_OFFSETS.gold_in_bank.start_index : SAVE_OFFSETS.gold_in_bank.end_index
                ],
            )
        )

        little_end_hex_string = "0x" + "".join(
            [format(int(c, 16), "02X") for c in reversed(big_end_hex_list)]
        )

        return int(little_end_hex_string, 16)

    def get_time_played(self) -> str:
        time_list = self.save_data[
            SAVE_OFFSETS.time_played.start_index : SAVE_OFFSETS.time_played.end_index
        ][::-1]

        return f"{time_list[0]}:{time_list[1]}"

    def get_text_speed(self) -> int:
        # In game text speed goes from 1 to 8. 1 being fastest.
        # In save text speed is stored as a single byte 0x00 to 0x07. 0x00 being fastest.
        text_speed = self.save_data[
            SAVE_OFFSETS.text_speed.start_index : SAVE_OFFSETS.text_speed.end_index
        ][0]

        return int(text_speed)

    def get_inventory(self) -> list[str]:
        return decode.list_of_items(
            self.save_data[
                SAVE_OFFSETS.inventory.start_index : SAVE_OFFSETS.inventory.end_index
            ]
        )

    def get_vault_items(self) -> list[str]:
        return decode.list_of_items(
            self.save_data[
                SAVE_OFFSETS.vault.start_index : SAVE_OFFSETS.vault.end_index
            ]
        )

    def change_byte_int(self, byte_to_change: int, int_change: int):
        """Can be used to edit savefile on an individual byte by byte basis.

        Args:
            byte_to_change (int): Index of what byte to change. 2 to 8191.
            int_change (int): What the byte should be changed to. 0 to 255.
        """
        self.save_data[byte_to_change] = int_change

    def change_byte_int_list(
        self, starting_index: int, ending_index: int, list_ints_change: list[int]
    ):
        if ending_index < starting_index:
            raise Exception("Starting Index is Greater Than Ending Index")

        if list_ints_change == []:
            raise Exception("List of Ints to Change is Empty")

        self.save_data[starting_index:ending_index] = list_ints_change

    def checksum_gen(self) -> list[int, int]:
        """Returns the calculated checksum for a save file as a tuple of two bytes.
        These should be put in as the first two bytes of the file. Translated from these gbz80 assembly instructions

        1 - ldi a, [hl]
        2 - add e
        3 - ld e, a
        4 - ld a, $00
        5 - adc d
        6 - ld d, a

        Args:
            save (list[int]): A list of integers representing the save file. Should be 8192 ints long.

        Returns:
            list(int,int): Byte 1 and Byte 2 of the save file.
        """

        # These are what the registers are set to before generating the checksums.
        a = 0x0A
        f = 0x00
        d = 0x46
        e = 0x38
        carry = 256

        for sram_byte in range(2, 8192):
            # 1 - LOAD SRAM TO A
            a = self.save_data[sram_byte]

            # 2 - ADD E TO A. If over 255, F becomes a carry flag
            a += e

            if len(hex(a)) == 5:
                a -= carry
                f += 1

            # 3 - LOAD A INTO E
            e = a

            # 4 - LOAD $00 TO A
            a = 0x00

            # 5 - ADD D (AND CARRY IF EXISTS) TO A
            a += d

            if f != 0:
                a += f
                f = 0x00

            if len(hex(a)) == 5:
                a -= carry

            # 6 - LOAD A INTO D
            d = a

        return [e, d]

    def save_to_file(self, filename: str):
        check_sum_bytes: list[int] = self.checksum_gen()

        self.change_byte_int_list(0, 2, check_sum_bytes)

        byte_data: bytes = bytes(self.save_data)

        with open(f"{filename}.sav", "wb") as file:
            file.write(byte_data)

    def get_party_indices(self) -> list[int]:
        indices = self.save_data[
            SAVE_OFFSETS.party_indices.start_index : SAVE_OFFSETS.party_indices.end_index
        ]

        indices = [x for x in indices if x != 255]

        return indices

    def get_farm_one(self) -> Farm:
        farm_one_list = self.save_data[
            SAVE_OFFSETS.farm_one.start_index : SAVE_OFFSETS.farm_one.end_index
        ]

        return Farm(farm_one_list)

    def get_farm_two(self) -> Farm:
        farm_two_list = self.save_data[
            SAVE_OFFSETS.farm_two.start_index : SAVE_OFFSETS.farm_two.end_index
        ]

        return Farm(farm_two_list)

    def get_current_party(self) -> list[Monster]:
        current_farm_monster_list = self.get_farm_one().monsters

        party_indices = self.get_party_indices()

        current_party = [current_farm_monster_list[index] for index in party_indices]

        return current_party

    def get_monster_library_from_save(self) -> MonsterLibrary:
        return MonsterLibrary(
            self.save_data[
                SAVE_OFFSETS.monster_library.start_index : SAVE_OFFSETS.monster_library.end_index
            ]
        )

    def get_tiny_medals_from_save(self) -> int:
        return self.save_data[
            SAVE_OFFSETS.tiny_medals.start_index : SAVE_OFFSETS.tiny_medals.end_index
        ][0]
