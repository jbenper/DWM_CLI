from models.save_file import SaveFile

from utilities.cli import arguments
from utilities.debugging_utils import print_attributes

if __name__ == "__main__":
    print(r"""
          
  _______          ____  __    _____                 
 |  __ \ \        / /  \/  |  / ____|                
 | |  | \ \  /\  / /| \  / | | (___   __ ___   _____ 
 | |  | |\ \/  \/ / | |\/| |  \___ \ / _` \ \ / / _ \
 | |__| | \  /\  /  | |  | |  ____) | (_| |\ V /  __/
 |_____/   \/  \/   |_|  |_| |_____/ \__,_| \_/ \___|
                                                                                              
""")

    save = SaveFile(file_loc = arguments.file)

    if arguments.interactive:
        print("interactive")
    else:
        print(save)
        # print_attributes(save.get_farm_one().get_farm_monsters()[0])