from utilities.models import SaveFile

from inspect import getmembers
from types import FunctionType

def attributes(obj):
    disallowed_names = {
      name for name, value in getmembers(type(obj)) 
        if isinstance(value, FunctionType)}
    
    disallowed_names.add("monster_int_list")

    return {
      name: getattr(obj, name) for name in dir(obj) 
        if name[0] != '_' and name not in disallowed_names and hasattr(obj, name)}

def print_attributes(obj):
    print('')
    print(attributes(obj))


if __name__ == "__main__":
    file_loc: str = "test_saves/zdwm.sav"
    # file_loc: str = "test_dwm.sav"

    file_name: str = file_loc.split("/")[-1]

    with open(file_loc, "rb") as save_file:
        save_bytes: list[int] = [byte for byte in (save_file.read())]
    
    assert(len(save_bytes) == 8192)


    save = SaveFile(file_name=file_name, save_ints=save_bytes)

    print(save)
    # print('\n', save.get_farm_one().monsters[0])

    monster = save.get_farm_one().monsters[2]

    print_attributes(monster)   
