#Auction Program

print("\nWelcome To  the Secret Auction.")
auction_record = []
stop = False
highest_bid = 0
data = {}

while stop == False:
    name = input("\nWhat is your name?\n")
    bid = int(input("\nWhat's your bid?\n"))
    data[name] = bid
    auction_record.append(data)
    others = input("\nAre there any bidders? Type 'Yes' or 'No'.\n").lower()
    if others == "yes":
        print("\nAuction Continued")

    if others == "no":
        print("\nAuction Closed")
        stop = True

for bidder in data:
    bid_amount = data[bidder]
    if highest_bid < bid_amount:
        highest_bid = bid_amount
        winner = bidder
print(winner, "is the winner with a bid of", highest_bid)

print("auction_record", auction_record)






