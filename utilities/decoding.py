from utilities.encoding_tables import (
    char_id,
    family_id,
    item_id,
    item_id,
    monster_id,
    skill_id,
)


def zero_pad_hex(int_to_hex: int) -> str:
    hex_code: str = hex(int_to_hex)

    if len(hex_code) == 3:
        return hex_code.replace("x", "x0")
    else:
        return hex_code


def little_to_big(int_list: list[int]) -> list[str]:
    reversed_hex_list: list[str] = list(map(zero_pad_hex, int_list))[::-1]

    joined_hex_list: str = "".join(reversed_hex_list)

    big_end_hex_str: str = "0x" + joined_hex_list.replace("0x", "")

    big_end_hex_int: int = int(big_end_hex_str, 16)

    return big_end_hex_int


def name(name_list: list[int]) -> str:
    hex_list: list[str] = list(map(zero_pad_hex, name_list))

    if hex_list == ["0xd3", "0xd4", "0xd5", "0xd6"]:
        return "TERRY"

    decode_chars = lambda hex_code: char_id.get(hex_code, "")

    char_list: list[str] = list(map(decode_chars, hex_list))

    return "".join(char_list)


def list_of_items(item_list: list[int]) -> list[str]:
    hex_item_list: list[str] = list(map(zero_pad_hex, item_list))

    decode_items = lambda hex_code: item_id.get(hex_code, "")

    item_list: list[str] = list(map(decode_items, hex_item_list))

    return item_list


def skills(skill_int_list: list[int]) -> list[str]:
    hex_skill_list: list[str] = list(map(zero_pad_hex, skill_int_list))

    decode_skills = lambda hex_code: skill_id.get(hex_code, "")

    skill_list: list[str] = list(map(decode_skills, hex_skill_list))

    return skill_list


def monster_species(species_int: int) -> str:
    return monster_id.get(zero_pad_hex(species_int), None)


def monster_family(family_int: int) -> str:
    return family_id.get(zero_pad_hex(family_int), None)
