from enum import Enum

rank_to_string = {0: " ★",
                  1: " A",
                  2: " 2",
                  3: " 3",
                  4: " 4",
                  5: " 5",
                  6: " 6",
                  7: " 7",
                  8: " 8",
                  9: " 9",
                 10: "10",
                 11: " J",
                 12: " Q",
                 13: " K",}
suit_to_string = {
    "spades": "♠",
    "hearts": "♥",
    "diamonds": "♦",
    "clubs": "♣",
}

class Card:
    def __init__(self, rank, suit, back_color="red"):
        if rank < 0 or rank > 14:
            raise ValueError("Rank not in range")
        if suit not in {"spades", "clubs", "diamonds", "hearts"}:
            raise ValueError("Non valid suit")
        if back_color not in {"red", "blue"}:
            raise ValueError("Non valid back color")
        self.rank = rank
        self.suit = suit
        self.back_color = back_color

    def front(self):
        return ((self.rank, self.suit))

    def back(self):
            return (self.back_color)

    def __str__(self):
        return f"{rank_to_string[self.rank]}{suit_to_string[self.suit]}"

    def __repr__(self):
        return f"{rank_to_string[self.rank]}{suit_to_string[self.suit]}"


"""
a = Card(1,"clubs", "red")
b = str(a)
print(b)"""
