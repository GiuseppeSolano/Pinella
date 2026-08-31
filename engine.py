from player import Player
from deck   import Deck
from enum import Enum


class Engine:
    def __init__(self, type):
        self.players  = Player(0,"PEPPE"), Player(1,"AMORE MIO")
        self.type     = type
        self.deck     = Deck(type)
        self.discards = Deck("empty")
        self.turn     = 0
        self.phase    = 0
        self.deck.shuffle()

    def __str__(self):
        tmp = "== State of the game ==\n"
        tmp = tmp + f"Discard pile:   {self.discars.get_cards_left()}\n"
        tmp = tmp + f"Remaning cards: {self.deck.get_cards_left()}\n"
        tmp = tmp + self.players[0].__str__() + "\n"
        tmp = tmp + self.players[1].__str__()
        return tmp

    def give_player_cards(self, player, cards):
        self.players[player].hand = self.players[player].hand + cards

    def remove_player_cards(self, list_pos):
        list_pos.sort(reverse=True)
        tmp = []
        for pos in list_pos:
            tmp.append(self.players[self.turn].hand.pop(pos-1))
        return tmp

    
    def check_win_condition(self):
        if self.players[self.turn].hand == []:
            return True
        return False

    def is_valid_draw(self, move):
        #il punto è capire dopo se la carte che ha deciso di pescare va bene per il momento pesca sempre dal deck quindi chill, ma si può fare roba più fine tipo escludere tutto ciò che non è 0
        return True

    def apply_draw(self, move):
        if move == 0:
            self.give_player_cards(self.turn,self.deck.draw_card())

    def is_valid_move(self, move):
        if move[0] == 0:
            card = move[1][0]
            if card > len(self.players[self.turn].hand):
                return False
        return True

    def apply_move(self, move):
        if move[0] == 0:
            self.discards.add_card(self.remove_player_cards(move[1]))
"""
m = Master("pinella")
m.loop()"""