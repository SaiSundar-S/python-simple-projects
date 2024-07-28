import os
print("********Silent Action Program********")
def find_winner(bidding_details):
    highest_price=0
    winner=""
    for bidder in bidding_details:
        bidding_price=bidding_details[bidder]
        if bidding_price>highest_price:
            highest_price=bidding_price
            winner=bidder
    print(f"highest bidding_price by {winner}as {highest_price}")


bidding_data = {}
end_bidding=False
while not end_bidding:
    name=input("enter your name?")
    price=int(input("enter the price"))
    bidding_data[name]=price
    more_bidding=input("type yes for continue bidding,no for exit").lower()
    if more_bidding=='no':
        end_bidding=False
        find_winner(bidding_data)
    elif more_bidding=='yes':
        os.system('cls')

