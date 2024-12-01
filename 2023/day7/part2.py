from dataclasses import dataclass
from enum import IntEnum


class HandTypes(IntEnum):
    FIVE = 6
    FOUR = 5
    FULL_HOUSE = 4
    THREE = 3
    TWO_PAIR = 2
    PAIR = 1
    HIGH = 0

@dataclass
class Entry:
    hand: str
    bid: int
    type: HandTypes = HandTypes.HIGH
    _cmp_hand: str = None

    @property
    def cmp_hand(self) -> str:
        if self._cmp_hand is None:
            self._cmp_hand = self.hand.replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "1")
        return self._cmp_hand

    def __lt__(self, other: "Entry") -> bool:
        if self.type != other.type:
            return self.type < other.type
        return self.cmp_hand < other.cmp_hand


lines = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]

with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

entries = []

for line in lines:
    entries.append(entry := Entry(line[0:5], int(line[6:])))
    hand = {}
    for card in entry.hand:
        hand[card] = 1 + hand.get(card, 0)
    unique = len(hand.keys())
    if unique == 1:
        entry.type = HandTypes.FIVE
    elif unique == 2:
        count = next(iter(hand.values()))
        if "J" in hand:
            entry.type = HandTypes.FIVE
        elif 4 in set(hand.values()):
            entry.type = HandTypes.FOUR
        else:
            entry.type = HandTypes.FULL_HOUSE
    elif unique == 3:
        if 3 in set(hand.values()):
            if "J" in hand:
                entry.type = HandTypes.FOUR
            else:
                entry.type = HandTypes.THREE
        else:
            if "J" in hand:
                if hand["J"] == 2:
                    entry.type = HandTypes.FOUR
                else:
                    entry.type = HandTypes.FULL_HOUSE
            else:
                entry.type = HandTypes.TWO_PAIR
    elif unique == 4:
        if "J" in hand:
            entry.type = HandTypes.THREE
        else:
            entry.type = HandTypes.PAIR
    elif "J" in hand:
        entry.type = HandTypes.PAIR

ranked = sorted(entries)

total = 0
for i,e in enumerate(ranked):
    total += e.bid * (i + 1)
    print(e)

print(total)
