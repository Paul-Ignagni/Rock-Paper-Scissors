import random

def playRockPaperScissors():
    choice = -1
    winCounter = 0
    lossCounter = 0
    tieCounter = 0
    while choice != 0:
        print("Press 1 to select rock")
        print("Press 2 to select paper")
        print("Press 3 to select scissors")
        print("Press 0 to exit")
        print("")
        choice = input("Select choice: ")
        if (choice == "1"):
            print("You selected: Rock")
        elif (choice == "2"):
            print("You selected: Paper")
        elif (choice == "3"):
            print("You selected: Scissors")
        elif (choice == "0"):
            print("Exiting")
            exit(0)
        else:
            print("Incorrect option, shutting down")
            exit(1)

        opponentChoice = random.randint(1,3)
        if (opponentChoice == 1):
            print("Opponent selected: Rock")
        elif (opponentChoice == 2):
            print("Opponent selected: Paper")
        elif (opponentChoice == 3):
            print("Opponent selected: Scissors")

        match choice:
            case "1":
                if (opponentChoice == 1):
                    print("Tie")
                    tieCounter += 1
                elif (opponentChoice == 2):
                    print("You lose")
                    lossCounter += 1
                elif (opponentChoice == 3):
                    print("You win!")
                    winCounter += 1
            case "2":
                if (opponentChoice == 1):
                    print("You win!")
                    winCounter += 1
                elif (opponentChoice == 2):
                    print("Tie")
                    tieCounter += 1
                elif (opponentChoice == 3):
                    print("You lose")
                    lossCounter += 1
            case "3":
                if (opponentChoice == 1):
                    print("You lose")
                    lossCounter += 1
                elif (opponentChoice == 2):
                    print("You win")
                    winCounter += 1
                elif (opponentChoice == 3):
                    print("Tie")
                    tieCounter += 1
        print("Wins: %d     Losses: %d     Ties: %d" % (winCounter, lossCounter, tieCounter))
        print("\n")


if __name__ == '__main__':
    playRockPaperScissors()

