import random

from exceptions import ValidationError
from Card import Card
from Hand import Hand
from constants import CARD_VALUES, CARD_SUITS

class Game(object):
    def __init__(self, player_count):
        self.hands = []
        if player_count < 2:
            raise ValidationError('Not enough players - Minimum is 2')
        if player_count > 10:
            raise ValidationError('Too many players - Maximum is 10')
        self.deck = [Card(value, suit) for value in CARD_VALUES for suit in CARD_SUITS]
        random.shuffle(self.deck)
        for player in range(player_count):
            self.hands.append(self.draw_hand())
    
    def draw_hand(self):
        hand = []
        for i in range(5):
            hand.append(self.draw_card())
        return Hand(hand)

    def draw_card(self):
        return self.deck.pop()

    def compare_hands(self):
        winning_hands = []
        for idx, hand in enumerate(self.hands):
            if len(winning_hands) < 1:
                winning_hands.append(hand)
            else:
                if hand.rank() < winning_hands[0].rank():
                    winning_hands = [hand]
                elif hand.rank() == winning_hands[0].rank():
                    winning_hands = hand.compare_hands_tiebreak(winning_hands)

        return winning_hands
    
    # def _compare_hand_values(self, winning_hands):
    #     hand_type = winning_hands[0]['hand_type']

    #     for hand in winning_hands:
            