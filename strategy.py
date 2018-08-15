from blackjack import BlackJack

class BasicStrategy:

    def hit_recommendation(self, cards, dealer_showing):
        total = sum(cards)
        if dealer_showing >= 7:
            if total < 17:
                return True
        if dealer_showing >= 2 and dealer_showing <= 6:
            if total <= 12:
                return False

    def split_recommendation(self, card, dealer_showing):
        if card == 1 or card == 8:
            return True
        if card == 5 or card == 10:
            return False
        if card == 2 or card == 3:
            if dealer_showing >= 2 and dealer_showing <= 7:
                return True
        if card == 4:
            if dealer_showing == 5 or dealer_showing == 6:
                return True
        if card == 6:
            if dealer_showing >= 2 and dealer_showing <= 6:
                return True
        if card == 7:
            if dealer_showing >= 2 and dealer_showing <= 7:
                return True
        if card == 9:
            if dealer_showing >= 2 and dealer_showing <= 7:
                return True
            elif dealer_showing == 8 or dealer_showing == 9:
                return True
