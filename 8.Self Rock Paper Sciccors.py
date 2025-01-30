# Game: Rock-Paper-Sciccors with Score (Lesson 8: Exercise 8) - Edition Self
from random import randrange
from datetime import datetime 
from random import seed

seed(datetime.now())

cards = ["paper", "sciccors", "rock"]


score = [0,0]
while score[0] >= 3 or score[1] <= 3:
    user_input = input("Enter 0-paper, 1-scissors, 2-rock: ").strip()
    if user_input.isalpha() or user_input == "" :
        print("Wrong Input! Enter a number in range 0-2!")
        continue
    else:
        user = int(user_input)
        if user > 2 or user < 0:
            print("Number Out Of Range! Enter between 0-2!")
        else:
            computer = randrange(3)
            # Case 1 - Computer: Paper
            if computer == 0:
                if user == 0:
                    print("Draw!")
                elif user == 1:
                    print("Computer picked paper and Player picked sciccors!")
                    print("Player Wins!")
                    score[0] += 1
                elif user == 2:
                    print("Computer picked paper and Player picked rock!")
                    print("Computer Wins!")
                    score[1] += 1
                    
            # Case 2 - Computer Sciccors
            elif computer == 1:
                if user == 0:
                    print("Computer picked sciccors and Player picked paper!")
                    print("Computer Wins!")
                    score[1] += 1
                elif user == 1:
                    print("Draw!")
                elif user == 2:
                    print("Computer picked sciccors and Player picked rock!")
                    print("Player Wins!")
                    score[0] += 1
                    
            # Case 3 - Computer: Rock
            else:
                if user == 0:
                    print("Computer picked rock and Player picked paper!")
                    print("Player Wins!")
                    score[0] += 1
                elif user == 1:
                    print("Computer picked rock and Player picked sciccors!")
                    print("Computer Wins!")
                    score[1] += 1
                elif user == 2:
                    print("Draw!")
        if score[0] == 3 and score[1] != 3:
            print("\nCongratulations! Player Won!")
            print("Total Score")
            print(f"Player:{score[0]} - Computer:{score[1]}")
            break
        elif score[0] != 3 and score[1] == 3:
            print("\nSorry! Computer Won!")
            print("Total Score")
            print(f"Player:{score[0]} - Computer:{score[1]}")
            break
