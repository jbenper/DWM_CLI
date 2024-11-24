from models.save_file import SaveFile
from utilities.general_utils import print_attributes, arguments

if __name__ == "__main__":
    print(r"""
          
  _______          ____  __    _____                 
 |  __ \ \        / /  \/  |  / ____|                
 | |  | \ \  /\  / /| \  / | | (___   __ ___   _____ 
 | |  | |\ \/  \/ / | |\/| |  \___ \ / _` \ \ / / _ \
 | |__| | \  /\  /  | |  | |  ____) | (_| |\ V /  __/
 |_____/   \/  \/   |_|  |_| |_____/ \__,_| \_/ \___|
                                                                                              
""")
    file_loc: str = arguments.file

    file_name: str = file_loc.split("/")[-1]

    with open(file_loc, "rb") as save_file:
        save_bytes: list[int] = [int_byte for int_byte in (save_file.read())]
    
    if len(save_bytes) != 8192:
        raise Exception("Save File Length does not match .sav format")

    save = SaveFile(file_name=file_name, save_ints=save_bytes)

    print(save)