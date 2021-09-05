def nim(n):
    computer_turn = False
    while True:  # Game loop, only end when game ends.
        if computer_turn:
            algo_output = computerTurn(n)
            print("The algorithm takes " + str(algo_output) + " stones.")
            n = n - algo_output
            print("There are " + str(n) + " stones left.")
            computer_turn = False
        else:
            if n == 0:
                print("Congrats, you beat the algorithm!")
                exit(1)
            while True:  # Test user input
                user = int(input("How many stones would you like to take away? <1> or <2>: "))
                if user < 3 and user > 0:
                    break
            computer_turn = True
            n = n - user
            if n < 0:
                print("You lose!")
                exit(2)
            print("You take " + str(user) + " stones.")
            print("There are " + str(n) + " stones left.")
            if n == 0:
                print("You lose!")
                exit(1)


def win(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return not (win(n - 1) and win(n - 2))


def computerTurn(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if win(n - 2):
        return 1
    if win(n - 1):
        return 2


nim(10)
