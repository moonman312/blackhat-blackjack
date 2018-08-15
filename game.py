import argparse
from counter import HiLowCounter
from strategy import BasicStrategy
from blackjack import BlackJack

def main():
    counting = False
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count_type", help="supported counting strategies: 'hl': High-Low")
    args = parser.parse_args()
    strategy = BasicStrategy()
    if args.count_type == "hl":
        counting = True
        decks_remaining = input("How many decks are left? ")
        counter = HiLowCounter(decks_remaining)
        game = BlackJack(strategy, counter)
    elif args.count_type:
        print("We don't support that counting strategy yet")
    else:
        game = BlackJack(strategy)
    while True:
        dealer_showing = input("Dealer Showing: ")
        your_first_card = input("Card 1: ")
        your_second_card = input("Card 2: ")
        cards = [your_first_card, your_second_card]
        game.set_dealer_showing(dealer_showing)
        if counting:
            other_cards = raw_input("What are the other cards on the table (seperated by spaces)? ")
            other_cards = [int(x) for x in other_cards.split(" ")]
            game.count_strat.set_count(cards + other_cards)
        if your_first_card == your_second_card:
            if game.play_strat.split_recommendation(your_first_card, game.get_dealer_showing()):
                cards_1, cards_2 = game.handle_split(your_first_card)
            else:
                print("DO NOT SPLIT")
        if game.play_strat.hit_recommendation([your_first_card, your_second_card], game.get_dealer_showing()):
            game.handle_hit([your_first_card, your_second_card])
        else:
            print("STAY")
        if counting:
            print("Next round your bet should be: " + str(game.count_strat.get_bet_amount()) + " betting units.")
        if raw_input("Play Again (y/n): ") == "n":
            break
main()
