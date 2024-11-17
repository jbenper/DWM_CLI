from DWM_CLI.utilities.checksum import checksum_gen



if __name__ == "__main__":
    file_loc = "DWM_CLI/test_saves/zdwm.sav"
    file_name = file_loc.split("/")[-1]

    with open(file_loc, "rb") as save_file:
        save_bytes = [byte for byte in (save_file.read())]
    
    assert(len(save_bytes) == 8192)

    print("Checksum: ", checksum_gen(save=save_bytes))