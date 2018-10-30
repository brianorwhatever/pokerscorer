import unittest

from exceptions import ValidationError
from Game import Game

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

if __name__ == '__main__':
    unittest.main()