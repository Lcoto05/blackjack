from blackjackart import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(): 
    return random.choice(cards) 

def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def clear():  # Prints 50 blank lines
    print("\n" * 50)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "You Draw 🤷🏻"
    elif computer_score == 0:
        return "You Lose, opponent has Blackjack! 😭"
    elif user_score == 0:
        return "You win with a Blackjack! 🤩"
    elif user_score > 21:
        return "You went over 21. You lose 😔"
    elif computer_score > 21:
        return "Opponent went over 21. You win! 😏"
    else: 
        if user_score > computer_score:
            return "You win! 😄"
        if computer_score > user_score:
            return "Computer wins 😒"
def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    should_continue = True

    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while should_continue:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score is: {user_score}\n")
        print(f"    Opponent's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            should_continue = False
        else:
            userdealchoice = input("Would you like to draw another card? 'y' if yes, 'n' if no: ").lower()
            if userdealchoice == 'y':
                user_cards.append(deal_card())
            else:
                should_continue = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}\n     Opponent's final hand: {computer_cards}")
    print(compare(user_score, computer_score))

while input("Do you want to play Blackjack? 'y' if yes, 'n' if no: ").lower() == 'y':
    clear()
    blackjack()