import unittest
from src.HandStrength import HandStrength


class TestHandRanking(unittest.TestCase):
    hand_strength_ = HandStrength()

    def test_straight_flush(self):
        test_hand = [[1, 5], [1, 14]]
        test_table = [[1, 4], [1, 2], [1, 3]]
        correct_outcome = ['straight flush', 5]
        unittest_result = self.hand_strength_(test_hand, test_table, False)
        self.assertEqual(unittest_result, correct_outcome)

    def test_flush(self):
        test_hand = [[1, 5], [1, 13]]
        test_table = [[1, 4], [1, 2], [1, 3]]
        correct_outcome = ['flush', 13]
        unittest_result = self.hand_strength_(test_hand, test_table, False)
        self.assertEqual(unittest_result, correct_outcome)

    def test_nothing(self):
        test_hand = [[2, 5], [0, 14]]
        test_table = [[1, 8], [1, 2], [1, 13]]
        correct_outcome = "nothing special"
        unittest_result = self.hand_strength_(test_hand, test_table, False)
        self.assertEqual(unittest_result, correct_outcome)

    def test_full_house(self):
        test_hand = [[2, 14], [0, 14]]
        test_table = [[1, 14], [1, 13], [1, 13]]
        correct_outcome = ['full house', 14]
        unittest_result = self.hand_strength_(test_hand, test_table, False)
        self.assertEqual(unittest_result, correct_outcome)

    def test_royal_flush(self):
        test_hand = [[2, 14], [2, 13]]
        test_table = [[2, 12], [2, 11], [2, 10]]
        correct_outcome = ['royal flush', 14]
        unittest_result = self.hand_strength_(test_hand, test_table, False)
        self.assertEqual(unittest_result, correct_outcome)

    def test_four_of_a_kind(self):
        test_hand = [[2, 4], [2, 4]]
        test_table = [[2, 3], [2, 4], [2, 4]]
        correct_outcome = ['four of a kind', 4]
        unittest_result = self.hand_strength_(test_hand, test_table, False)
        self.assertEqual(unittest_result, correct_outcome)

    def test_straight(self):
        test_hand = [[1, 4], [2, 5]]
        test_table = [[2, 3], [2, 2], [2, 6]]
        correct_outcome = ['straight', 6]
        unittest_result = self.hand_strength_(test_hand, test_table, False)
        self.assertEqual(unittest_result, correct_outcome)

    def test_three_of_a_kind(self):
        test_hand = [[1, 4], [2, 2]]
        test_table = [[2, 2], [2, 2], [2, 6]]
        correct_outcome = ['three of a kind', 2]
        unittest_result = self.hand_strength_(test_hand, test_table, False)
        self.assertEqual(unittest_result, correct_outcome)

    def test_double_pair(self):
        test_hand = [[1, 4], [2, 2]]
        test_table = [[2, 4], [2, 2], [2, 6]]
        correct_outcome = ['double pair', 4]
        unittest_result = self.hand_strength_(test_hand, test_table, False)
        self.assertEqual(unittest_result, correct_outcome)

    def test_pair(self):
        test_hand = [[1, 4], [2, 13]]
        test_table = [[2, 4], [2, 2], [2, 6]]
        correct_outcome = ['pair', 4]
        unittest_result = self.hand_strength_(test_hand, test_table, False)
        self.assertEqual(unittest_result, correct_outcome)


if __name__ == '__main__':
    unittest.main()
