from dataclasses import dataclass

@dataclass
class OffsetAttribute():
    start_index: int
    length: int

class Offsets():
    checksum: OffsetAttribute = OffsetAttribute(0, 2)
    
    master_name: OffsetAttribute = OffsetAttribute(380, 4)
    gold_in_hand: OffsetAttribute = OffsetAttribute(389, 3)
    gold_in_bank: OffsetAttribute = OffsetAttribute(392, 3)
    time_played: OffsetAttribute = OffsetAttribute(497, 2)


print(Offsets.time_played)