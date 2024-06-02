from art import logo
import os # type: ignore
#HINT: You can call clear() to clear the output in the console.
print(logo)


bids = {}

more_bids = "yes"


while more_bids == "yes":
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    more_bids = input("Are there any more bidders? Yes or No.\n").lower()
    if more_bids == "yes":
        os.system('clear')



def highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if  bid_amount >= highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner of auction is {winner} with bid of {highest_bid}")



highest_bidder(bids)

