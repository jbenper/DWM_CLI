from models.save_file import SaveFile
from utilities.debugging_utils import print_attributes


def main_menu_selection() -> str:
    print("What do you want to view?")
    print("(M)isc Save Information")
    print("Farm (O)ne")
    print("Farm (T)wo")
    selection = input("")
    print("\n")

    return selection

def interactivity_main(savefile: SaveFile):
    selection = "?"

    while selection == "?":
        selection = main_menu_selection()

        if selection == "M":
            print("Misc Save Information")
            print(savefile)

        elif selection == "O":
            print("Farm One")
            print(savefile.get_farm_one().get_farm_monsters())

        elif selection == "T":
            print("Farm Two")
            print(savefile.get_farm_two().get_farm_monsters())

        else:
            selection = "?"
            print("Unknown Option. Choose again.")