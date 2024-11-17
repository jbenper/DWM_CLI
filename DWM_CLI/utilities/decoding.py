
def master_name(name_list: list[int]) -> str:
    hex_list: list = list(map(hex, name_list))

    if hex_list == ['0xd3', '0xd4', '0xd5', '0xd6']:
        return "TERRY"
    
    decode_chars = lambda hex_code: char_id.get(hex_code, "")
    
    char_list = list(map(decode_chars, hex_list))

    return ''.join(char_list)

if __name__ == '__main__':
    from encoding_tables.character_table import char_id
    from encoding_tables.family_table import family_id
    from encoding_tables.item_table import item_id
    from encoding_tables.monster_table import monster_id
    from encoding_tables.skill_table import skill_id
else:

    from encoding_tables.character_table import char_id
    from encoding_tables.family_table import family_id
    from encoding_tables.item_table import item_id
    from encoding_tables.monster_table import monster_id
    from encoding_tables.skill_table import skill_id

    # from DWM_CLI.utilities.encoding_tables.character_table import char_id
    # from DWM_CLI.utilities.encoding_tables.family_table import family_id
    # from DWM_CLI.utilities.encoding_tables.item_table import item_id
    # from DWM_CLI.utilities.encoding_tables.monster_table import monster_id
    # from DWM_CLI.utilities.encoding_tables.skill_table import skill_id