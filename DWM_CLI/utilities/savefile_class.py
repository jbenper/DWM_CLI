class SaveFile():
    def __init__(self, file_name: str, save_ints: list[int]):
        self.save_ints = save_ints
        self.file_name = file_name
    
    def __repr__(self):
        return f"Save File: {self.file_name} | SaveLength: {len(self.save_ints)} | Master Name: {self.get_master_name()}"
    
    def get_master_name(self):
        return decode.master_name(self.save_ints[380:384])
    
    def change_byte_int(self, byte_to_change, int_change):
        """Can be used to edit savefile on an individual byte by byte basis. 

        Args:
            byte_to_change (int): Index of what byte to change. 2 to 8191. 
            int_change (int): What the byte should be changed to. 0 to 255.
        """        
        self.save_ints[byte_to_change] = int_change

    


if __name__ == "__main__":
    import decoding as decode

    file_loc = "DWM_CLI/test_saves/zdwm.sav"
    file_name = file_loc.split("/")[-1]

    with open(file_loc, "rb") as save_file:
        save_bytes = [byte for byte in (save_file.read())]

    assert len(save_bytes) == 8192

    save = SaveFile(file_name, save_bytes)

    print(save)
    
    save.change_byte_int(380, 36)
    save.change_byte_int(381, 36)
    save.change_byte_int(382, 36)
    save.change_byte_int(383, 36)

    print(save)


else:
    import DWM_CLI.utilities.decoding as decode