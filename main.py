from utilities.models import SaveFile
from utilities.debugging import print_attributes

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("file", help="the location of the save file")
# args = parser.parse_args()

debug = True

if __name__ == "__main__":
    if debug:
        file_loc: str = "test_dwm.sav"
    else:
        file_loc: str = args.file

    file_name: str = file_loc.split("/")[-1]

    with open(file_loc, "rb") as save_file:
        save_bytes: list[int] = [byte for byte in (save_file.read())]
    
    assert(len(save_bytes) == 8192)


    save = SaveFile(file_name=file_name, save_ints=save_bytes)

    print(save)
    # print('\n', save.get_farm_one().monsters[0])

    monster = save.get_farm_one().monsters[2]

    print_attributes(monster)   
