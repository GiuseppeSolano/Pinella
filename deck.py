from card import Card
import random

class Deck():
    def __init__(self, type):
        if type == "empty":
            self.deck = []
        elif type == "test":
            self.deck = []
            for i in range(1,14):
                self.deck.append(Card(i,"spades"))
            for i in range(1,14):
                self.deck.append(Card(i,"hearts"))
        elif type == "standard":
            self.deck = []
            for i in range(1,14):
                self.deck.append(Card(i,"spades"))
            for i in range(1,14):
                self.deck.append(Card(i,"clubs"))
            for i in range(1,14):
                self.deck.append(Card(i,"hearts"))
            for i in range(1,14):
                self.deck.append(Card(i,"diamonds"))

        elif type == "pinella":
            self.deck = []
            for i in range(1,14):
                self.deck.append(Card(i,"spades","red"))
            for i in range(1,14):
                self.deck.append(Card(i,"clubs","red"))
            self.deck.append(Card(1,"hearts","red"))
            for i in range(3,14):
                self.deck.append(Card(i,"hearts","red"))
            self.deck.append(Card(1,"diamonds","red"))
            for i in range(3,14):
                self.deck.append(Card(i,"diamonds","red"))
            self.deck.append(Card(0,"hearts","red"))
            self.deck.append(Card(0,"clubs","red"))
            for i in range(1,14):
                self.deck.append(Card(i,"spades","blue"))
            for i in range(1,14):
                self.deck.append(Card(i,"clubs","blue"))
            self.deck.append(Card(1,"hearts","blue"))
            for i in range(3,14):
                self.deck.append(Card(i,"hearts","blue"))
            self.deck.append(Card(1,"diamonds","blue"))
            for i in range(3,14):
                self.deck.append(Card(i,"diamonds","blue"))
            self.deck.append(Card(0,"hearts","blue"))
            self.deck.append(Card(0,"clubs","blue"))

    def get_cards_left(self):
        return len(self.deck)

    def get_back_last_card(self):
        return self.deck[-1].back

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self, quantity=1):
        cards = []
        i = quantity
        while (i > 0) and (self.get_cards_left() != 0):
            cards.append(self.deck.pop())
            i = i-1
        return cards

    def add_card(self, card):
        self.deck.append(card)
    

    def __str__(self):
        tmp = str(self.deck)
        return tmp + f"\ntotal cards left: {self.get_cards_left()}"

    def __len__(self):
        return len(self.deck)

"""
tmp = Deck("pinella")
print(tmp)"""