import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--file",
    type=str,
    help="the location of the save file",
    nargs="?",
    default="test_saves/zdwm.sav",
)

parser.add_argument(
    "--interactive",
    action='store_true',
    help="Enable interactivitiy",
)

arguments = parser.parse_args()
