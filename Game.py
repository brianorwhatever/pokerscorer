import random

from Card import Card
from Hand import Hand
from constants import CARD_VALUES, CARD_SUITS

class Game(object):
    hands = []
    
    def __init__(self, player_count):
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