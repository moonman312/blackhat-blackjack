import math
class HiLowCounter:

    def __init__(self, decks_remaining):
        self.decks_remaining = decks_remaining
        self.cards_remaining = self.decks_remaining * 52
        self.running_count = 0

    def get_running_count(self):
        return self.running_count

    def set_count(self, new_cards):
        for card in new_cards:
            if card >= 2 and card <= 6:
                self.running_count += 1
            elif card == 1 or card >= 10:
                self.running_count -= 1
        self.adjust_decks_remaining(len(new_cards))
        return

    def get_true_count(self):
        return math.ceil(self.running_count/self.decks_remaining)

    def adjust_decks_remaining(self, num_new_cards):
        self.cards_remaining -= num_new_cards
        self.decks_remaining = self.cards_remaining / 52
        return

    def get_bet_amount(self):
        return self.get_true_count() - 1
