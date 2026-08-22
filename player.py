class Player:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.hand = []

    def __str__(self):
        tmp = "hand of "+ self.name +": "
        for card in self.hand:
            tmp = tmp + card.__str__() + " "
        return tmp

    def decide_draw_phase(self):
        print(f"Player {self.name} decide what to do:")
        print(self.hand)
        print(f"Press 0 to draw from deck")
        move = input()
        return int(move)

    def decide_lay_down_phase(self):
        print(f"Player {self.name} decide what to do:")
        print(self.hand)
        print(f"Press 0 to discard a card")
        move = int(input())
        if move == 0:
            print(f"Write the number of the card to discard from 1 to {len(self.hand)+1}")
            card = int(input())
            return (0, [card])