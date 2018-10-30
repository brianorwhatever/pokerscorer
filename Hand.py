from exceptions import ValidationError

class Hand(object):
    def __init__(self, cards):
        self.cards = []
        if len(cards) != 5:
            raise ValidationError(message='Hand must contain 5 cards')
        self.cards = cards
