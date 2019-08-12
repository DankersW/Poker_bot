class HandStrength:
    hand_ = None
    table_ = None
    cards_ = None
    card_bucket_ = None  # example: [2, 3, ..., 10, 11 (=J), 12 (=Q), 13 (=K), 14 (=A)]
    suit_bucket_ = None  # example: [0 (Hearts), 1 (Diamonds), 2 (Clubs), 3 (Spades)]
    hand_ranking_card_index = 0

    def __init__(self):
        pass

    def __call__(self, hand, table, testing_stage):
        self.hand_ = hand
        self.table_ = table
        self.cards_ = hand + table
        self.calculate_card_occurrence()
        self.calculate_suit_occurrence()

        if testing_stage:
            print("hand: " + str(self.hand_) + "\t table: " + str(self.table_))
            print("cards: " + str(self.cards_))
            print("card bucket: " + str(self.card_bucket_))
            print("suit bucket: " + str(self.suit_bucket_))

        return self.calculate_hand_strength()

    def calculate_card_occurrence(self):
        card_bucket = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(self.cards_)):
            card_bucket[self.cards_[i][1]] += 1
        del card_bucket[:2]
        self.card_bucket_ = card_bucket

    def calculate_suit_occurrence(self):
        suit_bucket = [0, 0, 0, 0]
        for i in range(len(self.cards_)):
            suit_bucket[self.cards_[i][0]] += 1
        self.suit_bucket_ = suit_bucket

    def calculate_hand_strength(self):
        if self.contains_royal_flush():
            return ["royal flush", self.hand_ranking_card_index]
        elif self.contains_straight_flush():
            return ["straight flush", self.hand_ranking_card_index]
        elif self.contains_four_of_kind():
            return ["four of a kind", self.hand_ranking_card_index]
        elif self.contains_full_house():
            return ["full house", self.hand_ranking_card_index]
        elif self.contains_flush():
            return ["flush", self.hand_ranking_card_index]
        elif self.contains_straight():
            return ["straight", self.hand_ranking_card_index]
        elif self.contains_three_of_kind():
            return ["three of a kind", self.hand_ranking_card_index]
        elif self.contains_double_pair():
            return ["double pair", self.hand_ranking_card_index]
        elif self.contains_a_pair():
            return ["pair", self.hand_ranking_card_index]
        else:
            return "nothing special"

    def contains_royal_flush(self):
        royal_flush_card_bucket_list = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
        contains_royal_straight = royal_flush_card_bucket_list == self.card_bucket_
        royal_flush = contains_royal_straight and self.contains_flush()
        return True if royal_flush else False

    def contains_straight_flush(self):
        straight_flush = self.contains_flush() and self.contains_straight()
        return True if straight_flush else False

    def contains_four_of_kind(self):
        quantity_of_four = 4
        if quantity_of_four in self.card_bucket_:
            self.hand_ranking_card_index = self.card_bucket_.index(quantity_of_four) + 2
            return True
        return False

    def contains_full_house(self):
        quantity_of_three = 3
        quantity_of_pair = 2
        full_house = quantity_of_three in self.card_bucket_ and quantity_of_pair in self.card_bucket_
        if full_house:
            index_three = self.card_bucket_.index(quantity_of_three)
            index_pair = self.card_bucket_.index(quantity_of_pair)
            highest_index = max(index_three, index_pair)
            self.hand_ranking_card_index = highest_index + 2
            return True
        return False

    def contains_flush(self):
        length_of_flush = 5
        if length_of_flush in self.suit_bucket_:
            self.hand_ranking_card_index = max([item[1] for item in self.cards_])
            return True
        return False

    def contains_straight(self):
        consecutive_five_cards_set = [1, 1, 1, 1, 1]
        size_of_straight = 5
        number_of_aces = self.card_bucket_[-1]
        card_bucket = [number_of_aces] + self.card_bucket_
        for i in range(len(card_bucket)):
            five_card_sublist = card_bucket[i:(i+size_of_straight)]
            if five_card_sublist == consecutive_five_cards_set:
                self.hand_ranking_card_index = i+size_of_straight
                return True
        return False

    def contains_three_of_kind(self):
        quantity_of_three = 3
        if quantity_of_three in self.card_bucket_:
            self.hand_ranking_card_index = self.card_bucket_.index(quantity_of_three) + 2
            return True
        return False

    def contains_double_pair(self):
        quantity_of_pair = 2
        if self.card_bucket_.count(2) == quantity_of_pair:
            indices = [i for i, x in enumerate(self.card_bucket_) if x == quantity_of_pair]
            self.hand_ranking_card_index = max(indices) + 2
            return True
        return False

    def contains_a_pair(self):
        quantity_of_pair = 2
        if quantity_of_pair in self.card_bucket_:
            self.hand_ranking_card_index = self.card_bucket_.index(quantity_of_pair) + 2
            return True
        return False

    def __del__(self):
        pass


if __name__ == '__main__':
    testing_stage = True
    test_hand = [[1, 4], [2, 13]]
    test_table = [[2, 4], [2, 2], [2, 6]]
    hand_strength = HandStrength()
    result = hand_strength(test_hand, test_table, testing_stage)
    print(result)
