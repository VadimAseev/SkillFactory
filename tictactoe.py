# Map with index fields
maps_init = [1,2,3,4,5,6,7,8,9]

# All possible winning combinations in the game
win_combination = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


# Map printing
def print_maps():

    print(maps_init[0], end="  ")
    print(maps_init[1], end="  ")
    print(maps_init[2])

    print(maps_init[3], end="  ")
    print(maps_init[4], end="  ")
    print(maps_init[5])

    print(maps_init[6], end="  ")
    print(maps_init[7], end="  ")
    print(maps_init[8])

stat_player = False

# Make step in the game
# The correctness of the player's move is determined.
# If everything is correct, we put the desired symbol in the card list and switch the player.
# If not, we suggest trying again.
def step_maps(step, symbol, player):
    if maps_init[step - 1] == "X" or maps_init[step - 1] == "O":
        print("Неправильный ход, попробуйте ещё раз")
        player =  False
    else:
        ind = maps_init.index(step)
        maps_init[ind] = symbol
        player = True
    return player







# Check the game's result status. If already hav winner
def get_result():
    winner = ""
    for i in win_combination:
        if maps_init[i[0]] == "X" and maps_init[i[1]] == "X" and maps_init[i[2]] == "X":
            winner = "X"
        elif maps_init[i[0]] == "O" and maps_init[i[1]] == "O" and maps_init[i[2]] == "O":
            winner = "O"
    return winner


# Main program
game_over = False
player = True

while game_over == False:

    # 1. Show map
    print_maps()
    print()
    # 2. Invition and next turn request
    if player:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))

    stat_player = step_maps(step, symbol, stat_player)  # Make step
    winner = get_result()  # Check winner
    if winner != "":
        game_over = True
    else:
        game_over = False

    if stat_player:
        player = not player


# Finish game. Show map and declaration of winner
print_maps()
print()
print(f"Победитель - ", "Игрок 1" if get_result() == "X" else "Игрок 2")
