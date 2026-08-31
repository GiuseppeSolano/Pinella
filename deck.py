from card import Card
import random

class Deck():
    def __init__(self, type):
        if type == "empty":
            self.cards = []
        elif type == "test":
            self.cards = []
            for i in range(1,14):
                self.cards.append(Card(i,"spades"))
            for i in range(1,14):
                self.cards.append(Card(i,"hearts"))
        elif type == "standard":
            self.cards = []
            for i in range(1,14):
                self.cards.append(Card(i,"spades"))
            for i in range(1,14):
                self.cards.append(Card(i,"clubs"))
            for i in range(1,14):
                self.cards.append(Card(i,"hearts"))
            for i in range(1,14):
                self.cards.append(Card(i,"diamonds"))

        elif type == "pinella":
            self.cards = []
            for i in range(1,14):
                self.cards.append(Card(i,"spades","red"))
            for i in range(1,14):
                self.cards.append(Card(i,"clubs","red"))
            self.cards.append(Card(1,"hearts","red"))
            for i in range(3,14):
                self.cards.append(Card(i,"hearts","red"))
            self.cards.append(Card(1,"diamonds","red"))
            for i in range(3,14):
                self.cards.append(Card(i,"diamonds","red"))
            self.cards.append(Card(0,"hearts","red"))
            self.cards.append(Card(0,"clubs","red"))
            for i in range(1,14):
                self.cards.append(Card(i,"spades","blue"))
            for i in range(1,14):
                self.cards.append(Card(i,"clubs","blue"))
            self.cards.append(Card(1,"hearts","blue"))
            for i in range(3,14):
                self.cards.append(Card(i,"hearts","blue"))
            self.cards.append(Card(1,"diamonds","blue"))
            for i in range(3,14):
                self.cards.append(Card(i,"diamonds","blue"))
            self.cards.append(Card(0,"hearts","blue"))
            self.cards.append(Card(0,"clubs","blue"))

    def get_cards_left(self):
        return len(self.cards)

    def get_back(self):
        if len(self.cards) == 0:
            return ""
        return self.cards[-1].back()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self, quantity=1):
        cards = []
        i = quantity
        while (i > 0) and (self.get_cards_left() != 0):
            cards.append(self.cards.pop())
            i = i-1
        return cards

    def add_card(self, card):
        self.cards.append(card)
    

    def __str__(self):
        tmp = str(self.cards)
        return tmp + f"\ntotal cards left: {self.get_cards_left()}"

    def __len__(self):
        return len(self.cards)

"""
tmp = cards("pinella")
print(tmp)"""