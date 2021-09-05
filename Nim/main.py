import time


def nim(n):
    computer_turn = False
    total_time = 0
    while True:  # Game loop, only end when game ends.
        if computer_turn:
            begin = time.time()
            algo_output = computerTurn(n)
            end = time.time()
            total_time = total_time + (end - begin)
            print("The algorithm takes " + str(algo_output) + " stones.")
            n = n - algo_output
            print("There are " + str(n) + " stones left.")
            computer_turn = False
        else:
            if n == 0:
                print("Congrats, you beat the algorithm!")
                print("Time: " + str(int(total_time)))
                exit(1)
            user = 1
            computer_turn = True
            n = n - user
            if n < 0:
                print("You lose!")
                print("Time: " + str(int(total_time)))
                exit(2)
            print("You take " + str(user) + " stones.")
            print("There are " + str(n) + " stones left.")
            if n == 0:
                print("You lose!")
                print("Time: " + str(int(total_time)))
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
    if win(n - 1):
        return 2
    if win(n - 2):
        return 1


def memoized(n):
    sol = [False] * (n+1)
    sol[0] = True
    for i in range (2, n+1):
        sol[i] = not(sol[i-1] and sol[i-2])
    print(sol)
    return sol[n]


nim(61)
