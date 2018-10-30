import unittest

from exceptions import ValidationError
from Game import Game
from Hand import Hand
from Card import Card

class TestGame(unittest.TestCase):
    def test_init_with_no_player_count(self):
        with self.assertRaises(TypeError) as cm:
            Game()
            self.assertEqual(
                "__init__() missing 1 required positional argument: 'player_count'",
                str(cm.message)
            )
    
    def test_init_with_too_few_player_count(self):
        with self.assertRaises(ValidationError) as cm:
            Game(player_count=1)
            self.assertEqual(
                'Not enough players - Minimum is 2',
                str(cm.message)
            )
    
    def test_init_with_too_many_players(self):
        with self.assertRaises(ValidationError) as cm:
            Game(player_count=11)
            self.assertEqual(
                'Too many players - Maximum is 10',
                str(cm.message)
            )
    
    def test_init_success(self):
        player_count = 4

        game = Game(player_count=player_count)
        
        self.assertEqual(len(game.hands), player_count)
        self.assertEqual(len(game.deck), 52-player_count*5)
    
    def test_draw_card(self):
        player_count = 4
        game = Game(player_count=player_count)
        self.assertEqual(len(game.deck), 52-player_count*5)

        card = game.draw_card()

        self.assertEqual(len(game.deck), 52-player_count*5-1)
        self.assertTrue(card not in game.deck)
        for hand in game.hands:
            self.assertTrue(card not in hand.cards)
    
    def test_draw_hand(self):
        player_count = 4
        game = Game(player_count=player_count)

        hand = game.draw_hand()

        self.assertEqual(len(hand.cards), 5)
        for card in hand.cards:
            self.assertTrue(card not in game.deck)
    
    def test_compare_hands(self):
        player_count = 4
        game = Game(player_count=player_count)
        winning_hand = Hand([Card('2', '♥'), Card('4', '♣'), Card('5', '♦'), Card('5', '♥'), Card('8', '♠')])
        game.hands = [
            winning_hand,
            Hand([Card('6', '♣'), Card('9', '♥'), Card('J', '♦'), Card('J', '♣'), Card('K', '♦')]),
            Hand([Card('3', '♠'), Card('5', '♠'), Card('6', '♠'), Card('7', '♥'), Card('9', '♦')]),
            Hand([Card('3', '♣'), Card('9', '♠'), Card('10', '♣'), Card('Q', '♦'), Card('A', '♦')])
        ]
        
        winning = game.compare_hands()
        
        self.assertEqual(winning[0], winning_hand)
        self.assertEqual(winning[0].hand_type(), 'Pair')
        
