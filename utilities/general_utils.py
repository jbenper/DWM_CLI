from inspect import getmembers
from types import FunctionType
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "file",
    help="the location of the save file",
    nargs="?",
    default="test_saves/zdwm.sav",
)
arguments = parser.parse_args()


def attributes(obj):
    disallowed_names = {
        name for name, value in getmembers(type(obj)) if isinstance(value, FunctionType)
    }

    disallowed_names.add("monster_int_list")
    disallowed_names.add("farm_int_list")
    disallowed_names.add("save_data")

    return {
        name: getattr(obj, name)
        for name in dir(obj)
        if name[0] != "_" and name not in disallowed_names and hasattr(obj, name)
    }


def print_attributes(obj):
    print("")
    print(attributes(obj))
