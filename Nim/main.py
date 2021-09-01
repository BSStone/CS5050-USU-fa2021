def nim(n):
    computer_turn = False
    while True:     # Game loop, only end when game ends.
        if computer_turn:
            turn(n)
            computer_turn = False
            while True:     # Test user input
                user = int(input("How many stones would you like to take away? <1> or <2>: "))
                if user < 3 and user > 0:
                    break

        turn(n)


def win(n):
    print(n)
    if n == 0:
        return True
    if n == 1:
        return False
    return not (win(n-1) and win(n-2))


def turn(n):
    if n == 1:
        return 1
    if n == 2:
         return 1
    if win(n - 1):
        return 1
    if win(n - 2):
        return 2

