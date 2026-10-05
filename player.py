class Player:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.hand = []

    def get_num_cards(self):
        return len(self.hand)

    def get_cards(self):
        return [card.to_dict() for card in self.hand]

    def __str__(self):
        tmp = ""
        for c in self.hand:
            tmp = tmp + c.__str__() + "\n"
        return tmp
