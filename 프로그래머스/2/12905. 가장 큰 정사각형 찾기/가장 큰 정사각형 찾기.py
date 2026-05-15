def solution(board):
    rows = len(board)
    cols = len(board[0])

    if rows < 2 or cols < 2:
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 1:
                    return 1
        return 0
    
    max_side = 0
    for i in range(1, rows):
        for j in range(1, cols):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                max_side = max(max_side, board[i][j])

    if max_side == 0:
        for r in board:
            if 1 in r: return 1
        return 0
    return max_side ** 2