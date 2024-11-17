from DWM_CLI.utilities.checksum import checksum_gen


if __name__ == "__main__":
    with open("DWM_CLI/test_saves/zdwm.sav", "rb") as save_file:
        save_bytes = [byte for byte in (save_file.read())]

    print(checksum_gen(save=save_bytes))