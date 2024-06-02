from art import logo,vs
import random
from game_data import data

a = {}
b = {}
score = 0

print(logo)

def choose():
    return random.choice(data)

def compare_followers(a, b):
    follower_a =  a['follower_count']
    follower_b =  b['follower_count']
    # print("A: ",follower_a)
    # print("B: ",follower_b)

    if follower_a > follower_b:
        # print("this is a")
        return a
    else:
        # print("this is b")
        return b

def score_counter(winner, guess):
    global score
    if winner['name'] == guess:
        score+=1
        print(f"You are right, current score: {score}")
        swap(winner)
        # print(f"a in counter{a}")
        # print(f"b in counter{b}")
        return True
    else:
        print(f"That's incorrect, Your Final score is {score}")
        return False

def swap(winner):
    global a
    a = winner
    # print(f"a in swap: {a}")
    # print(f"b in swap: {b}")
    return

a = choose()

def game():
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs) 
    b = choose()

    while a == b:
        b = choose()
    
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # print(guess)
    result = compare_followers(a, b)
    # print(result)

    if guess == 'a':
        guess = a['name']
    else:
        guess = b['name']

    # print(result)
    if score_counter(result, guess):
        game()
    else:
        return

game()