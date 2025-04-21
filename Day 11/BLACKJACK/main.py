from art import logo
import random


continue_game=True
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
while continue_game:
    con=input("do you want to play a game of blackjack? 'y' or 'n' : ")
    if con=='y':
        print(logo)
        player=[]
        player_total=0
        computer=[]
        computer_total=0
        player.append(random.sample(cards,2))
        i=0
        for play in player:
            print(f"your cards: {play}")
            player_total=sum(play)

        print(f"current score: {player_total}")
        computer.append(random.sample(cards, 2))
        print(f"computer card: {computer[0][0]}")
        for play in computer:
            computer_total=sum(play)
        if player_total == 21:
            print("BLACKJACK,you win.")
            break
        hit=''
        while hit!='n':
            hit=input("do you want another card? 'y' or 'n': ")
            if hit=='y':
                player[0].append(random.choice(cards))
                for play in player:
                    print(f"your cards: {play}")
                    player_total = sum(play)
                if player_total>21:
                    print(f"{player_total}, YOU WENT OVER 21.")
                    print("IT IS A BUST. YOU LOSE 🙃")
                    break

        while computer_total != 0 and computer_total < 17 and hit=='n':

            computer[0].append(random.choice(cards))
            for play in computer:

                computer_total = sum(play)
            if computer_total > 21:
                for play in computer:
                    print(f"DEALER cards: {play}")  # testing
                print(f"{computer_total}, DEALER WENT OVER 21.")
                print("IT IS A BUST FOR DEALER. YOU WIN")
                break

        if computer_total==player_total:
            for play in computer:
                print(f"DEALER cards: {play}")#testing
            print("Draw 🙃")
        elif computer_total <= 21 and computer_total > player_total:
            for play in computer:
                print(f"DEALER cards: {play}")#testing
            print(f"{computer_total} > {player_total},YOU LOSE 🙃")
        elif computer_total <= 21 and computer_total < player_total and player_total <=21:
            for play in computer:
                print(f"DEALER cards: {play}")#testing
            print(f"{computer_total} < {player_total},YOU WIN 🙃")
    else:
        continue_game=False

