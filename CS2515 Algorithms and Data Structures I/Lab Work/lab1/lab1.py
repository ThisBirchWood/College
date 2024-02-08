import random

class Card:
    def __init__(self, number, suite):
        self.suite = suite
        self.number = number

    def __str__(self):
        return (str(self.number) + ":" + str(self.suite))
    
    def is_equal(self, c):
        if self.suite == c.suite and self.number == c.number:
            return True
        return False
    
    def is_higher(self, other):
        if self.number >= other.number:
            return True
        return False

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, Card):
        self.cards.append(Card)

    def get_highest_card(self):
        highest = Card(0, 0)
        for card in self.cards:
            if card.number > highest.number:
                highest = card

        return highest
    
    def return_cards(self):
        all_cards = ''

        for card in self.cards:
            all_cards += (str(card.number) + ":" + str(card.suite) + "\n")

        return all_cards
    
class Deck:
    def __init__(self):
        self.cards = []
        for suite in range(1, 5):
            for number in range(1, 14):
                self.cards.append(Card(number, suite))

    def shuffle(self):
        random.shuffle(self.cards)

    def get_top_card(self):
        return self.cards.pop(0)

#1
def gameOne():
    deck = Deck()
    userHand = Hand()
    systemHand = Hand()
    deck.shuffle()

    for i in range(5):
        userHand.add_card(deck.get_top_card())
        systemHand.add_card(deck.get_top_card())

    print("Your Cards:")
    print(userHand.return_cards())

    user_guess = input("Do you think that you have the highest card? (y/n) ")
    user_highest = userHand.get_highest_card()
    system_highest = systemHand.get_highest_card()

    if user_guess == "y":
        if user_highest.is_higher(system_highest):
            print("Correct! Yours is higher.")
            print("Your Card: " + str(user_highest.number) + ", System Card: " + str(system_highest.number))
        else:
            print("Incorrect! Yours is lower.")
            print("Your Card: " + str(user_highest.number) + ", System Card: " + str(system_highest.number))
    else:
        if user_highest.is_higher(system_highest):
            print("Incorrect! Yours is higher.")
            print("Your Card: " + str(user_highest.number) + ", System Card: " + str(system_highest.number))
        else:
            print("Correct! Yours is lower.")
            print("Your Card: " + str(user_highest.number) + ", System Card: " + str(system_highest.number))

class Board:
    def __init__(self):
        self.facedown_cards = []
        self.faceup_card = None
        self.previous_faceups = []

    def add_card(self, card):
        self.facedown_cards.append(card)

    def reveal_card(self):
        next_card = self.facedown_cards.pop(0)

        if self.faceup_card != None:
            self.previous_faceups.append(self.faceup_card)

        self.faceup_card = next_card

        return next_card
    
    def length(self):
        return len(self.facedown_cards)

#2 
def gameTwo():
    deck = Deck()
    deck.shuffle()

    player1_board = Board()
    player2_board = Board()
    player1_passes = 2
    player2_passes = 2

    player_turn = 1 
    turn_changed = True

    for i in range(8):
        player1_board.add_card(deck.get_top_card())
        player2_board.add_card(deck.get_top_card())

    previous_card = player1_board.reveal_card()
    print("First Card:", previous_card)

    while player_turn != 0:
        while player_turn == 1:
            if player1_board.length() > 0:
                if turn_changed:
                    print("--- PLAYER 1 ---")
                    turn_changed = False

                user_guess = input("Will the next card be higher or lower? (h/l/p) ")

                next_card = player1_board.reveal_card()

                if (user_guess == "h" and next_card.number > previous_card.number) or (user_guess == "l" and next_card.number < previous_card.number):
                    print("Correct!", next_card)
                elif user_guess == "p" and player1_passes > 0:
                    print("Passed, ", next_card)
                    player_turn = 2
                    player1_passes -= 1
                    turn_changed = True
                else:
                    print("Incorrect!", next_card)
                    player_turn = 2
                    turn_changed = True

                previous_card = next_card
            else:
                player_turn = 0
                print("PLAYER 1 WINS!")

        while player_turn == 2:
            if player2_board.length() > 0:
                if turn_changed:
                    print("--- PLAYER 2 ---")
                    turn_changed = False

                user_guess = input("Will the next card be higher or lower? (h/l/p) ")

                next_card = player2_board.reveal_card()

                if (user_guess == "h" and next_card.number > previous_card.number) or (user_guess == "l" and next_card.number < previous_card.number):
                    print("Correct! ", next_card)
                elif user_guess == "p" and player2_passes > 0:
                    print("Passed, ", next_card)
                    player_turn = 1
                    player2_passes -= 1
                    turn_changed = True
                else:
                    print("Incorrect!", next_card)
                    player_turn = 1
                    turn_changed = True

                previous_card = next_card

            else:
                player_turn = 0
                print("PLAYER 2 WINS!")

    input()
        















        




