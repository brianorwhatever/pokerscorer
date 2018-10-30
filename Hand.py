import operator

from constants import CARD_RANKS, ROYAL_FLUSH, STRAIGHT_FLUSH, FOUR_OF_A_KIND, FULL_HOUSE, \
                      FLUSH, STRAIGHT, THREE_OF_A_KIND, TWO_PAIR, PAIR, HIGH_CARD
from Card import Card
from exceptions import ValidationError

def rank(card):
    if card.value.isnumeric():
        return int(card.value)
    else:
        return CARD_RANKS[card.value]

class Hand(object):
    def __init__(self, cards):
        self.cards = []
        if len(cards) != 5:
            raise ValidationError(message='Hand must contain 5 cards')
        self.cards = cards
        self.cards.sort(key=rank)
        self._count_cards()

    def __repr__(self):
        return str(self.cards)
    
    def _count_cards(self):
        card_counts = {}
        for card in self.cards:
            try:
                card_counts[card.value] += 1
            except KeyError:
                card_counts[card.value] = 1
        return card_counts
    
    def has_flush(self):
        found_suits = []
        for card in self.cards:
            if card.suit not in found_suits:
                found_suits.append(card.suit)
                if(len(found_suits) > 1):
                    return False
        return True
    
    def has_straight(self):
        return self._straight_ace_high() or self._straight_ace_low()

    def _straight_ace_high(self):
        for i in range(len(self.cards)-1):
            if self.cards[i].as_rank() + 1 != self.cards[i+1].as_rank():
                return False
        return True
    
    def _straight_ace_low(self):
        if self.cards[len(self.cards)-1].value != 'A':
            return False
        card = self.cards.pop(len(self.cards)-1)
        self.cards.insert(0, card)
        for i in range(len(self.cards)-1):
            if self.cards[i].as_rank(ace_is_low=True) + 1 != self.cards[i+1].as_rank(ace_is_low=True):
                return False
        return True

    def hand_type(self):
        is_flush = self.has_flush()
        is_straight = self.has_straight()
        card_counts = self._count_cards()
        largest_card_count = max(card_counts.items(), key=operator.itemgetter(1))
        del card_counts[largest_card_count[0]]
        second_largest_card_count = max(card_counts.items(), key=operator.itemgetter(1))
        
        if is_flush and is_straight:
            if self.cards[-1:][0].value == 'A':
                return ROYAL_FLUSH
            else:
                return STRAIGHT_FLUSH
        elif largest_card_count[1] == 4:
            return FOUR_OF_A_KIND
        elif largest_card_count[1] == 3 and second_largest_card_count[1] == 2:
            return FULL_HOUSE
        elif is_flush:
            return FLUSH
        elif is_straight:
            return STRAIGHT
        elif largest_card_count[1] == 3:
            return THREE_OF_A_KIND
        elif largest_card_count[1] == 2 and second_largest_card_count[1] == 2:
            return TWO_PAIR
        elif largest_card_count[1] == 2:
            return PAIR
        return HIGH_CARD
