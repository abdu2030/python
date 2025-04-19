logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
more=True
bid_collection = {}
while more != False:
    name = input("WHAT IS YOUR NAME? : ")
    bid = int(input("WHAT IS YOUR BID? :$"))
    bid_collection[name]=bid
    approve = input("is there an an other bidders,\"yes\" or \"No\"?")
    if approve=="yes":
        more=True
        print("\n" * 20)
    elif approve=="no":
        more=False
values=0
winner=""
for key in bid_collection:
    if bid_collection[key]>values:
        values=bid_collection[key]
        winner=key
print(f"THE WINNER IS {winner} WITH THE BID OF ${values}")



