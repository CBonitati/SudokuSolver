import argparse
from sudoku import solve_sudoku

BOARD_SIZE = 9

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Sudoku Solver')

    # Add an argument for the Sudoku board
    parser.add_argument('board', type=int, nargs='*',
                        help='Sudoku board (space-separated numbers, use -1 for empty cells)')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if the board was provided as arguments
    if not args.board:
        # Prompt the user to enter the board
        print("Enter the Sudoku board line by line:")
        board = []
        for _ in range(BOARD_SIZE):
            row = input().split()
            if len(row) != BOARD_SIZE:
                print(f'Invalid board size. Expected {BOARD_SIZE}x{BOARD_SIZE} numbers.')
                return
            board.append([int(num) for num in row])
    else:
        # Create the puzzle from the provided board
        if len(args.board) != BOARD_SIZE:
            print(f'Invalid board size. Expected {BOARD_SIZE}x{BOARD_SIZE} numbers.')
            return
        board = [args.board[i:i+BOARD_SIZE] for i in range(0, BOARD_SIZE * BOARD_SIZE, BOARD_SIZE)]

    # Solve the Sudoku puzzle
    if solve_sudoku(board):
        print('Solution found:')
        for row in board:
            print(' '.join(map(str, row)))
    else:
        print('No solution found for the given board.')


if __name__ == '__main__':
    main()
