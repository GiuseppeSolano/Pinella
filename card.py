from enum import Enum

class Card:
    def __init__(self, rank, suit, back="red"):
        if rank < 0 or rank > 14:
            raise ValueError("Rank not in range")
        if suit not in {"spades", "clubs", "diamons", "hearts"}:
            raise ValueError("Non valid suit")
        if back not in {"red", "blue"}:
            raise ValueError("Non valid back")
        self.rank = rank
        self.suit = suit
        self.back = back

    def __str__(self):
        return f"{self.rank} of {self.suit} (back: {self.back})"


"""
a = Card(1,"clubs", "red")
b = str(a)
print(b)"""
