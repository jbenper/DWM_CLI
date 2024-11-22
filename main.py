from utilities.models import SaveFile
from utilities.general_utils import print_attributes, arguments

if __name__ == "__main__":
    file_loc: str = arguments.file

    file_name: str = file_loc.split("/")[-1]

    with open(file_loc, "rb") as save_file:
        save_bytes: list[int] = [byte for byte in (save_file.read())]
    
    assert(len(save_bytes) == 8192)

    save = SaveFile(file_name=file_name, save_ints=save_bytes)

    print(save)
    

    # print('\n', save.get_farm_one().monsters[0])

    farm = save.get_farm_one()

    print_attributes(farm)
