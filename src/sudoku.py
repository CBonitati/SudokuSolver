BOARD_SIZE = 9
# locates the next space with -1 meaning empty
def find_next_empty_space(puzzle):
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if puzzle[r][c] == -1:
                return r, c
    return None, None


# Checks the validity of the number guess
def is_valid(puzzle, guess, row, col):
    row_vals = set(puzzle[row])
    if guess in row_vals:
        return False

    col_vals = {puzzle[i][col] for i in range(BOARD_SIZE)}
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

# determines if the guess at the empty space is valid and continues
def solve_sudoku(puzzle):
    row, col = find_next_empty_space(puzzle)

    if row is None:
        return True

    for guess in range(1, BOARD_SIZE + 1):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True

            puzzle[row][col] = -1

    return False
