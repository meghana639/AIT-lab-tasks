def solve(row, board):
    if row == 4:
        print(board)
        return True

    for col in range(4):
        if col not in board and all(
            abs(board[i] - col) != row - i for i in range(row)
        ):
            board.append(col)
            if solve(row + 1, board):
                return True
            board.pop()

    return False

solve(0, [])
