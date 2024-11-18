from utilities.savefile_class import SaveFile


if __name__ == "__main__":
    file_loc: str = "test_saves/zdwm.sav"
    file_name: str = file_loc.split("/")[-1]

    with open(file_loc, "rb") as save_file:
        save_bytes: list[int] = [byte for byte in (save_file.read())]
    
    assert(len(save_bytes) == 8192)


    save = SaveFile(file_name=file_name, save_ints=save_bytes)

    print(save)