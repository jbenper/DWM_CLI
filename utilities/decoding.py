
def master_name(name_list: list[int]) -> str:
    hex_list: list = list(map(hex, name_list))

    if hex_list == ['0xd3', '0xd4', '0xd5', '0xd6']:
        return "TERRY"
    
    decode_chars = lambda hex_code: char_id.get(hex_code, "")
    
    char_list = list(map(decode_chars, hex_list))

    return ''.join(char_list)

if __name__ == '__main__':
    from encoding_tables import char_id, family_id, item_id, item_id, monster_id, skill_id

else:
    # from encoding_tables import char_id, family_id, item_id, item_id, monster_id, skill_id
    from utilities.encoding_tables import char_id, family_id, item_id, item_id, monster_id, skill_id

