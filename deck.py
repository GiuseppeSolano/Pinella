from card import Card
import random

class Deck():
    def __init__(self, type):
        if type == "empty":
            self.deck = []
        if type == "test":
            self.deck = [Card(1,"spades"), Card(2,"spades","blue")]
        if type == "standard":
            self.deck = []
            for i in range(1,14):
                self.deck.append(Card(i,"spades"))
            for i in range(1,14):
                self.deck.append(Card(i,"clubs"))
            for i in range(1,14):
                self.deck.append(Card(i,"hearts"))
            for i in range(1,14):
                self.deck.append(Card(i,"diamons"))

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

    def __str__(self):
        tmp = ""
        for card in self.deck:
            tmp = tmp + str(card) + "\n"
        return tmp + f"total cards left: {self.get_cards_left()}"


tmp = Deck("test")
print(tmp)