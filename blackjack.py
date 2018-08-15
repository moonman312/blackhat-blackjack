class BlackJack:
    def __init__(self, play_strat, count_strat = False):
        self.play_strat = play_strat
        self.count_strat = count_strat
        self.dealer_showing = None

    def handle_split(self, card):
        print("SPLIT " + str(card))
        card_1 = int(input("First Card: "))
        card_2 = int(input("Second Card: "))
        if card_1 == card or card_2 == card and self.play_strat.split_recommendation(card, self.dealer_showing):
            self.handle_split(card)
        total_1 = [card, card_1]
        total_2 = [card, card_2]
        if sum(total_1) > 21:
            if card == 13:
                total_1[0] = 1
            elif card_1 == 13:
                total_1[1] = 1
        if sum(total_2) > 21:
            if card == 13:
                total_2[0] = 1
            elif card_2 == 13:
                total_2[1] = 1
        if self.play_strat.hit_recommendation(total_1, self.dealer_showing):
            self.handle_hit(total_1)
        if self.play_strat.hit_recommendation(total_2, self.dealer_showing):
            self.handle_hit(total_2)
        return total_1, total_2

    def handle_hit(self, cards):
        print("HIT ON " + str(sum(cards)))
        new_card  = int(input("New Card: "))
        if new_card in cards:
            if self.play_strat.split_recommendation(new_card, self.dealer_showing):
                self.handle_split(new_card)
                return
        cards.append(new_card)
        total = sum(cards)
        if total > 21 and new_card == 13:
            total = total - 12
        if total > 21:
            print("BUST")
        if self.play_strat.hit_recommendation(cards, self.dealer_showing):
            self.handle_hit(cards)
        return

    def set_dealer_showing(self, card):
        self.dealer_showing = card
        return

    def get_dealer_showing(self):
        return self.dealer_showing
