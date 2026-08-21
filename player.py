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