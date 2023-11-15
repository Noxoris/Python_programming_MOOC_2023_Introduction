# Write your solution here

def who_won(game_board: list):
    player1 = 0
    player2 = 0

    for i in range(len(game_board)): # using the number of rows in the matrix
        for j in range(len(game_board[i])): # using the number of items on each row 
            if game_board[i][j] == 1:
                player1 += 1
            elif game_board[i][j] == 2:
                player2 += 1
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0

if __name__ == "__main__":
    go = [[1, 2, 2, 2], [2, 1, 1, 1], [0, 2, 1, 0]]
    print(who_won(go))