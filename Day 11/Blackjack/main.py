from art import logo
import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def distribute_cards(player_cards):
    player_cards.extend(random.sample(cards, 2))

def sum_of_cards(player_cards):
    total_sum = 0
    for card in player_cards:
        total_sum += card
    return total_sum

def check_for_save(player_cards):
    sum_ace_1 = sum_of_cards(player_cards) - 11 + 1
    return sum_ace_1 <= 21

def draw_another_card(player_cards):
    player_cards.append(random.choice(cards))

def compare(user_cards, computer_cards):
    sum_user_cards = sum_of_cards(user_cards)
    sum_computer_cards = sum_of_cards(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {sum_user_cards}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum_computer_cards}")

    if sum_user_cards > 21:
        print("You went over. You lose!")
    elif sum_computer_cards > 21:
        print("Computer went over. You win! 😀")
    elif sum_user_cards > sum_computer_cards:
        print("You win! 😀")
    elif sum_user_cards < sum_computer_cards:
        print("Computer wins! 😀")
    else:
        print("It's a draw!")

def blackjack():
    os.system('clear')
    print(logo)
    
    distribute_cards(user_cards)
    distribute_cards(computer_cards)
    
    while True:
        sum_user_cards = sum_of_cards(user_cards)
        sum_computer_cards = sum_of_cards(computer_cards)
    
        print(f"Your cards: {user_cards}, current score: {sum_user_cards}")
        print(f"Computer's first card: {computer_cards[0]}")
    
        if sum_user_cards == 21:
            print("Blackjack! You win! 😀")
            return
        elif sum_computer_cards == 21:
            print("Computer has Blackjack! You lose.")
            return
        else:
            if sum_user_cards > 21:
                if 11 in user_cards and check_for_save(user_cards):
                    user_cards[user_cards.index(11)] = 1
                    sum_user_cards = sum_of_cards(user_cards)
                else:
                    print("You went over 21. You lose!")
                    return
            
            if sum_computer_cards > 21:
                if 11 in computer_cards and check_for_save(computer_cards):
                    computer_cards[computer_cards.index(11)] = 1
                    sum_computer_cards = sum_of_cards(computer_cards)
                else:
                    print("Computer went over 21. You win!")
                    return
            
            draw_card = input("Type 'y' to draw another card, 'n' to get results: ").lower()
            if draw_card == 'y':
                draw_another_card(user_cards)
            else:
                while sum_computer_cards < 17:
                    draw_another_card(computer_cards)
                    sum_computer_cards = sum_of_cards(computer_cards)
                
                compare(user_cards, computer_cards)
                return

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    user_cards = []
    computer_cards = []
    blackjack()
