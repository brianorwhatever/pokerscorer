import unittest

from Hand import Hand
from Card import Card
from constants import *

class TestHand(unittest.TestCase):
    def setUp(self):
        self.flush = [Card('Q', '♦'), Card('K', '♦'), Card('4', '♦'), Card('2', '♦'), Card('8', '♦')]

    def test_flush_true(self):
        hand = Hand([Card('Q', '♦'), Card('K', '♦'), Card('4', '♦'), Card('2', '♦'), Card('8', '♦')])

        self.assertTrue(hand.has_flush())
    
    def test_flush_false(self):
        hand = Hand([Card('Q', '♦'), Card('K', '♦'), Card('4', '♦'), Card('2', '♦'), Card('8', '♠')])

        self.assertFalse(hand.has_flush())
    
    def test_straight_with_high_ace(self):
        hand = Hand([Card('Q', '♦'), Card('K', '♦'), Card('J', '♦'), Card('10', '♦'), Card('A', '♠')])
        self.assertTrue(hand.has_straight())
    
    def test_straight_with_a_low_ace(self):
        hand = Hand([Card('2', '♦'), Card('3', '♦'), Card('4', '♦'), Card('5', '♦'), Card('A', '♠')])
        self.assertTrue(hand.has_straight())
    
    def test_straight_without_an_ace(self):
        hand = Hand([Card('5', '♦'), Card('6', '♦'), Card('7', '♦'), Card('8', '♦'), Card('9', '♠')])
        self.assertTrue(hand.has_straight())

    def test_not_straight(self):
        hand = Hand([Card('2', '♦'), Card('8', '♦'), Card('4', '♦'), Card('5', '♦'), Card('A', '♠')])
        self.assertFalse(hand.has_straight())

        hand = Hand([Card('A', '♠'), Card('8', '♦'), Card('4', '♦'), Card('5', '♦'), Card('A', '♠')])
        self.assertFalse(hand.has_straight())
    
    def test_count_cards(self):
        hand = Hand([Card('2', '♦'), Card('8', '♦'), Card('4', '♦'), Card('5', '♦'), Card('A', '♠')])
        
        card_counts = hand._count_cards()

        self.assertEqual(card_counts[2], 1)
        self.assertEqual(card_counts[8], 1)
        self.assertEqual(card_counts[4], 1)
        self.assertEqual(card_counts[5], 1)
        self.assertEqual(card_counts[14], 1)

    def test_count_cards_multiple_of_a_kind(self):
        hand = Hand([Card('2', '♠'), Card('2', '♥'), Card('2', '♣'), Card('2', '♦'), Card('A', '♠')])
        
        card_counts = hand._count_cards()

        self.assertEqual(card_counts[2], 4)
        self.assertEqual(card_counts[14], 1)
        
    def test_hand_type_royal_flush(self):
        hand = Hand([Card('10', '♦'), Card('J', '♦'), Card('Q', '♦'), Card('K', '♦'), Card('A', '♦')])
        hand_type = hand.hand_type()
        self.assertEqual(hand_type, ROYAL_FLUSH)
    
    def test_hand_type_straight_flush(self):
        hand = Hand([Card('10', '♦'), Card('J', '♦'), Card('Q', '♦'), Card('K', '♦'), Card('9', '♦')])
        hand_type = hand.hand_type()
        self.assertEqual(hand_type, STRAIGHT_FLUSH)
    
    def test_hand_type_four_of_a_kind(self):
        hand = Hand([Card('2', '♠'), Card('2', '♥'), Card('2', '♣'), Card('2', '♦'), Card('A', '♠')])
        hand_type = hand.hand_type()
        self.assertEqual(hand_type, FOUR_OF_A_KIND)
    
    def test_hand_type_full_house(self):
        hand = Hand([Card('2', '♠'), Card('2', '♥'), Card('2', '♣'), Card('A', '♦'), Card('A', '♠')])
        hand_type = hand.hand_type()
        self.assertEqual(hand_type, FULL_HOUSE)
    
    def test_hand_type_flush(self):
        hand = Hand([Card('10', '♦'), Card('3', '♦'), Card('Q', '♦'), Card('6', '♦'), Card('9', '♦')])
        hand_type = hand.hand_type()
        self.assertEqual(hand_type, FLUSH)
    
    def test_hand_straight(self):
        hand = Hand([Card('10', '♥'), Card('J', '♦'), Card('Q', '♥'), Card('K', '♦'), Card('9', '♥')])
        hand_type = hand.hand_type()
        self.assertEqual(hand_type, STRAIGHT)
    
    def test_hand_three_of_a_kind(self):
        hand = Hand([Card('10', '♥'), Card('10', '♦'), Card('10', '♣'), Card('K', '♦'), Card('9', '♥')])
        hand_type = hand.hand_type()
        self.assertEqual(hand_type, THREE_OF_A_KIND)
    
    def test_hand_two_pair(self):
        hand = Hand([Card('10', '♥'), Card('10', '♦'), Card('K', '♣'), Card('K', '♦'), Card('9', '♥')])
        hand_type = hand.hand_type()
        self.assertEqual(hand_type, TWO_PAIR)
    
    def test_hand_pair(self):
        hand = Hand([Card('10', '♥'), Card('10', '♦'), Card('J', '♣'), Card('K', '♦'), Card('9', '♥')])
        hand_type = hand.hand_type()
        self.assertEqual(hand_type, PAIR)
    
    def test_hand_high_card(self):
        hand = Hand([Card('3', '♥'), Card('10', '♦'), Card('J', '♣'), Card('K', '♦'), Card('9', '♥')])
        hand_type = hand.hand_type()
        self.assertEqual(hand_type, HIGH_CARD)
    
    # def test_rank(self):
    #     self.assertFalse(True)
    
    # def test_compare_hands_tiebreak_royal_flush(self):
    #     self.assertFalse(True)
        
    # def test_compare_hands_tiebreak_straight_flush(self):
    #     self.assertFalse(True)
    
    # def test_compare_hands_tiebreak_four_of_a_kind(self):
    #     hand1 = Hand([Card('2', '♠'), Card('2', '♥'), Card('2', '♣'), Card('2', '♦'), Card('A', '♠')])
    #     hand2 = Hand([Card('3', '♠'), Card('3', '♥'), Card('3', '♣'), Card('3', '♦'), Card('K', '♠')])

    #     compared = hand2.compare_hands_tiebreak([hand1])
    #     self.assertEqual(compared, [hand2])
