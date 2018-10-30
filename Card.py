from exceptions import ValidationError
from constants import CARD_VALUES, CARD_SUITS, CARD_RANKS

class Card(object):
    def __init__(self, value, suit):
        """Initializes a card"""
        if value not in CARD_VALUES:
            raise ValidationError(message='Card value {value} is invalid'.format(value=value))
        if suit not in CARD_SUITS:
            raise ValidationError(message='Card suit {suit} is invalid'.format(suit=suit))
        self.value = value
        self.suit = suit
    
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Card):
            return other.value == self.value and other.suit == self.value
        return False
    
    def __repr__(self):
        return 'Card: ' + self.value + self.suit
    
    def as_rank(self, ace_is_low=False):
        if self.value.isnumeric():
            return int(self.value)
        else:
            if ace_is_low and self.value == 'A':
                return 1
            return CARD_RANKS[self.value]