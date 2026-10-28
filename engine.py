from player import Player
from deck   import Deck
from enum import Enum

"""
Goal of the game:
Clear your hand by discarding your last card

Initial set up:
13 cards per player, the deck and a card on the discard pile

TODO: complete this comment

"""

class Engine:
    def __init__(self, type):
        self.players  = Player(0,"PEPPE"), Player(1,"AMORE MIO")
        self.type     = type
        self.deck     = Deck(type)
        self.discards = Deck("empty")
        self.turn     = 0
        self.phase    = 0
        self.deck.shuffle()
        self.give_player_cards(0,self.deck.draw_card(13))
        self.give_player_cards(1,self.deck.draw_card(13))
        print(self.players[0])


    def __str__(self):
        tmp = "== State of the game ==\n"
        tmp = tmp + f"Discard pile:   {self.discars.get_cards_left()}\n"
        tmp = tmp + f"Remaning cards: {self.deck.get_cards_left()}\n"
        tmp = tmp + self.players[0].__str__() + "\n"
        tmp = tmp + self.players[1].__str__()
        return tmp


    def give_player_cards(self, player, cards):
        cards = [(c,0) for c in cards]
        self.players[player].hand = self.players[player].hand + cards


    def remove_player_cards(self, list_pos):
        list_pos.sort(reverse=True)
        tmp = []
        for pos in list_pos:
            tmp.append(self.players[self.turn].hand.pop(pos-1))
        return tmp


    def is_valid_draw(self):
        return True

    def apply_draw(self):
        self.give_player_cards(self.turn,self.deck.draw_card())

    def is_valid_move(self, move):
        if move[0] == 0:
            card = move[1][0]
            if card > len(self.players[self.turn].hand):
                return False
        return True



    def apply_move(self, move):
        type = move["type"]
        if type not in {"draw"}:
            print("Invalid move")
            return
        if type == "draw":
            if not self.is_valid_draw():
                print("Cannot draw")
            self.apply_draw()

    def get_deck(self):
        return self.deck.to_dict()

    
    def get_player_hand(self, player):
        return self.players[player].get_hand()


"""
m = Master("pinella")
m.loop()"""
