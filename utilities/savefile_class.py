class SaveFile():
    def __init__(self, file_name: str, save_ints: list[int]):
        self.save_data: list[int] = save_ints
        self.file_name: str = file_name
    
    def __repr__(self):
        return f"""Save File: {self.file_name} | SaveLength: {len(self.save_data)} | Master Name: {self.get_master_name()}
Time Played: {self.get_time_played()} | Gold Amount: {self.get_gold_in_hand()} | Bank Amount: {self.get_gold_in_bank()}"""
    
    def get_master_name(self):
        return decode.master_name(self.save_data[OFFSETS.master_name.start_index : OFFSETS.master_name.end_index])
    
    def get_gold_in_hand(self):
        big_end_hex_list = list(map(hex, self.save_data[OFFSETS.gold_in_hand.start_index : OFFSETS.gold_in_hand.end_index]))

        little_end_hex_string = '0x' + ''.join([format(int(c, 16), '02X') for c in reversed(big_end_hex_list)])

        return int(little_end_hex_string, 16)

    def get_gold_in_bank(self):
        big_end_hex_list = list(map(hex, self.save_data[OFFSETS.gold_in_bank.start_index : OFFSETS.gold_in_bank.end_index]))

        little_end_hex_string = '0x' + ''.join([format(int(c, 16), '02X') for c in reversed(big_end_hex_list)])

        return int(little_end_hex_string, 16)

    def get_time_played(self) -> str:
        time_list = (self.save_data[OFFSETS.time_played.start_index : OFFSETS.time_played.end_index][::-1])

        return f"{time_list[0]}:{time_list[1]}"


    def change_byte_int(self, byte_to_change, int_change):
        """Can be used to edit savefile on an individual byte by byte basis. 

        Args:
            byte_to_change (int): Index of what byte to change. 2 to 8191. 
            int_change (int): What the byte should be changed to. 0 to 255.
        """        
        self.save_data[byte_to_change] = int_change

    def change_byte_int_list(self, starting_index, ending_index, list_ints_change):
        if (ending_index < starting_index):
            raise Exception("Starting Index is Greater Than Ending Index")
        
        if list_ints_change == []:
            raise Exception("List of Ints to Change is Empty")

        self.save_data[starting_index : ending_index] = list_ints_change

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

    def save_to_file(self, filename):
        check_sum_bytes = self.checksum_gen()

        self.change_byte_int_list(0, 2, check_sum_bytes)

        byte_data = bytes(self.save_data)

        with open(f'{filename}.sav', 'wb') as file:
            file.write(byte_data)
    


if __name__ == "__main__":
    import decoding as decode

    file_loc = "test_saves/zdwm.sav"
    file_name = file_loc.split("/")[-1]

    with open(file_loc, "rb") as save_file:
        save_bytes = [byte for byte in (save_file.read())]

    if len(save_bytes) != 8192:
        raise Exception("Save File Length Invalid")

    save = SaveFile(file_name, save_bytes)

    print(save)
    
    save.change_byte_int(380, 36)
    save.change_byte_int(381, 37)
    save.change_byte_int(382, 36)
    save.change_byte_int(383, 36)

    print(save)

    # save.save_to_file("test_dwm")

else:
    import utilities.decoding as decode
    from utilities.offsets import OFFSETS