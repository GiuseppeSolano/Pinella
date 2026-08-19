from player import Player
from deck   import Deck

class Master:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.deck    = Deck("pinella")

