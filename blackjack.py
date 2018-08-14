import argparse
from counter import HiLowCounter

def split(card):
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

def hit_or_stay(cards):
    total = sum(cards)
    if dealer_showing >= 7:
        if total < 17:
            return True
    if dealer_showing >= 2 and dealer_showing <= 6:
        if total <= 12:
            return False

def handle_split(card):
    print("SPLIT " + str(card))
    card_1 = int(input("First Card: "))
    card_2 = int(input("Second Card: "))
    if card_1 == card or card_2 == card:
        handle_split(card)
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
    if hit_or_stay(total_1):
        handle_hit(total_1)
    if hit_or_stay(total_2):
        handle_hit(total_2)
    return

def handle_hit(cards):
    print("HIT ON " + str(sum(cards)))
    new_card  = int(input("New Card: "))
    if new_card in cards:
        if split(new_card):
            handle_split(new_card)
            return
    cards.append(new_card)
    total = sum(cards)
    if total > 21 and new_card == 13:
        total = total - 12
    if total > 21:
        print("BUST")
    if hit_or_stay(cards):
        handle_hit(cards)
    return

def main():
    counting = False
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count_type", help="supported counting strategies: 'hl': High-Low")
    args = parser.parse_args()
    if args.count_type == "hl":
        counting = True
        decks_remaining = input("How many decks are left?")
        counter = HiLowCounter(decks_remaining)
    else:
        print("We don't support that counting strategy yet")
    while True:
        dealer_showing = input("Dealer Showing: ")
        your_first_card = input("Card 1: ")
        your_second_card = input("Card 2: ")
        cards = [your_first_card, your_second_card]
        if counting:
            other_cards = input("What are the other cards on the table (seperated by spaces)? ")
            other_cards = [int(x) for x in other_cards.split(" ")]
            counter.set_count(cards + other_cards)
        if your_first_card == your_second_card:
            if split(your_first_card):
                handle_split(your_first_card)
                if raw_input("Play Again (y/n): ") == "n":
                    break
            else:
                print("DO NOT SPLIT")
        if hit_or_stay([your_first_card, your_second_card]):
            handle_hit([your_first_card, your_second_card])
        else:
            print("STAY")
        print("Next round your bet should be: " + counter.get_bet_amount() + " betting units.")
        if raw_input("Play Again (y/n): ") == "n":
            break
main()
