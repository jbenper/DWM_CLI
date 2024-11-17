

class SaveFile():
    def __init__(self, file_name: str, save_ints: list[int]):
        self.save_ints = save_ints
        self.file_name = file_name
    
    def __repr__(self):
        return f"Save File: {self.file_name} | SaveLength: {len(self.save_ints)}"

if __name__ == "__main__":
    file_loc = "DWM_CLI/test_saves/zdwm.sav"
    file_name = file_loc.split("/")[-1]

    with open(file_loc, "rb") as save_file:
        save_bytes = [byte for byte in (save_file.read())]

    assert len(save_bytes) == 8192

    save = SaveFile(file_name, save_bytes)

    print(save)
