from dataclasses import dataclass

@dataclass
class OffsetAttribute():
    start_index: int
    end_index: int


class Offsets():
    checksum: OffsetAttribute = OffsetAttribute(0, 2)

    text_speed: OffsetAttribute = OffsetAttribute(40, 41)
    master_name: OffsetAttribute = OffsetAttribute(380, 384)
    gold_in_hand: OffsetAttribute = OffsetAttribute(389, 392)
    gold_in_bank: OffsetAttribute = OffsetAttribute(392, 395)
    inventory: OffsetAttribute = OffsetAttribute(395, 415)
    vault: OffsetAttribute = OffsetAttribute(415, 455)


    time_played: OffsetAttribute = OffsetAttribute(497, 499)
OFFSETS = Offsets()
