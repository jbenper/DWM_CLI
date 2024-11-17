def checksum_gen(save: list[int]) -> tuple[hex, hex]:
    """Returns the calculated checksum for a save file as a tuple of two bytes. 
    These should be put in as the first two bytes of the file. Translated from these assembly instructions

    1 - ldi a, [hl]
    2 - add e
    3 - ld e, a
    4 - ld a, $00
    5 - adc d
    6 - ld d, a

    Args:
        save (list[int]): A list of integers representing the save file. Should be 8192 ints long.

    Returns:
        tuple(hex, hex): Byte 1 and Byte 2 of the save file. 
    """

    # These are what the registers are set to before generating the checksums.
    a = 0x0A
    f = 0x00
    d = 0x46
    e = 0x38
    carry = 256

    for sram_byte in range(2, 8192):
        # 1 - LOAD SRAM TO A
        a = save[sram_byte]

        # 2 - ADD E TO A. If over 255, F becomes a carry flag
        a += e
        if len(hex(a)) == 5:
            a -= carry
            f += 1

        # 3 - LOAD A INTO E
        e = a

        # 4 - LOAD $00 TO A
        a = 0x00

        # 5 - ADD D (AND CARRY IF EXISTS) TO A
        a += d
        if f != 0:
            a += f
            f = 0x00

        if len(hex(a)) == 5:
            a -= carry

        # 6 - LOAD A INTO D
        d = a

    return (hex(e), hex(d))


if __name__ == "__main__":    
    with open("DWM_CLI/test_saves/zdwm.sav", "rb") as save_file:
        save_bytes = [byte for byte in (save_file.read())]

    assert(len(save_bytes) == 8192)

    print(checksum_gen(save_bytes))