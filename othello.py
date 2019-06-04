
EMPTY = 0
BLACK = 1
WHITE = 2

WEIGHT = [
    [120,   -20,    20,     5,      5,      20,     -20,    120],
    [-20,   -40,   -5,     -5,     -5,     -5,      -40,   -20],
    [20,    -5,     15,     3,      3,      15,     -5,     20],
    [5,     -5,     3,      3,      3,      3,      -5,     5],
    [5,     -5,     3,      3,      3,      3,      -5,     5],
    [20,    -5,     15,     3,      3,      15,     -5,     20],
    [-20,   -40,   -5,     -5,     -5,     -5,      -40,   -20],
    [120,   -20,    20,     5,      5,      20,     -20,    120]
]


def reshape_board(board):
    '''
    Description: Reshape 1D board to a 2D board.
    '''
    return [board[i: i + 8] for i in range(0, len(board), 8)]


def printboard(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            print(board[row][col])


def opponent(color):
    return WHITE if color == BLACK else BLACK


def neighbors(board, color):
    '''
    Description: Find all the empty spaces adjacent to the enemy square.

    Return: Tuples of the form (row, col, direction)
        - row, col = Position of a possible move.
        - direction = Where to walk to verify if it is a valid move.
    '''
    # opp = the opponent's color
    opp = opponent(color)
    adjacent = []

    for row in range(len(board)):
        for col in range(len(board[0])):

            if board[row][col] == opp:

                if row != 0:
                    # Up Tile
                    if board[row - 1][col] == EMPTY:
                        adjacent.append(
                            ((row - 1, col, 'down'))
                            )
                    if col != 0:
                        # Up Left Tile
                        if board[row - 1][col - 1] == EMPTY:
                            adjacent.append(
                                ((row - 1, col - 1, 'down-right'))
                                )
                    if col != 7:
                        # Up Right Tile
                        if board[row - 1][col + 1] == EMPTY:
                            adjacent.append(
                                ((row - 1, col + 1, 'down-left'))
                                )
                if row != 7:
                    # Down Tile
                    if board[row + 1][col] == EMPTY:
                        adjacent.append(
                                ((row + 1, col, 'up'))
                            )
                    if col != 0:
                        # Down Left Tile
                        if board[row + 1][col - 1] == EMPTY:
                            adjacent.append(
                                    ((row + 1, col - 1, 'up-right'))
                                )
                    if col != 7:
                        # Down-Right Tile
                        if board[row + 1][col + 1] == EMPTY:
                            adjacent.append(
                                    ((row + 1, col + 1, 'up-left'))
                                )
                if col != 0:
                    # Left Tile
                    if board[row][col - 1] == EMPTY:
                        adjacent.append(
                                ((row, col - 1, 'right'))
                            )
                if col != 7:
                    # Right Tile
                    if board[row][col + 1] == EMPTY:
                        adjacent.append(
                                    ((row, col + 1, 'left'))
                                )

    return adjacent


def is_valid_move(board, color, move):
    '''
    Description: Check if a movement is valid.

    Return: A tuple that indicates if the move is valid, the amount
        of squares gained and list with the squares that have to flip.
    '''
    row, col, direction = move

    valid = False
    # It is set in 1 by the stone of the current move
    square_count = 1
    # List of all squares to flip in the form (row, col)
    to_flip = []

    opp = opponent(color)

    # Go up
    if direction == 'up':
        while row != 0:
            row -= 1

            if board[row][col] == opp:
                to_flip.append((row, col))
                square_count += 1

            elif board[row][col] == color:
                valid = True
                break
            # Found a empty space
            else:
                break

    # Go down
    elif direction == 'down':
        while row != 7:
            row += 1

            if board[row][col] == opp:
                to_flip.append((row, col))
                square_count += 1

            elif board[row][col] == color:
                valid = True
                break

            else:
                break
    # Go left
    elif direction == 'left':
        while col != 0:
            col -= 1

            if board[row][col] == opp:
                to_flip.append((row, col))
                square_count += 1

            elif board[row][col] == color:
                valid = True
                break

            else:
                break

    # Go Right
    elif direction == 'right':
        while col != 7:
            col += 1

            if board[row][col] == opp:
                to_flip.append((row, col))
                square_count += 1

            elif board[row][col] == color:
                valid = True
                break

            else:
                break

    elif direction == 'up-left':

        while row != 0 and col != 0:
            row -= 1
            col -= 1

            if board[row][col] == opp:
                to_flip.append((row, col))
                square_count += 1

            elif board[row][col] == color:
                valid = True
                break

            else:
                break

    elif direction == 'up-right':

        while row != 0 and col != 7:
            row -= 1
            col += 1

            if board[row][col] == opp:
                to_flip.append((row, col))
                square_count += 1

            elif board[row][col] == color:
                valid = True
                break

            else:
                break

    elif direction == 'down-left':

        while row != 7 and col != 0:
            row += 1
            col -= 1

            if board[row][col] == opp:
                to_flip.append((row, col))
                square_count += 1

            elif board[row][col] == color:
                valid = True
                break

            else:
                break

    elif direction == 'down-right':

        while row != 7 and col != 7:
            row += 1
            col += 1

            if board[row][col] == opp:
                to_flip.append((row, col))
                square_count += 1

            elif board[row][col] == color:
                valid = True
                break

            else:
                break

    return (valid, (to_flip, square_count))


def moves(board, color):
    '''
    Description: Find all valid moves for a board.

    Return: A dictionary, where keys are valid moves
        and the value of the keys are the amount of squares earned.
    '''
    valid_moves = {}
    adjacent = neighbors(board, color)

    for adj in adjacent:
        v = is_valid_move(board, color, adj)
        # if is a valid move . . .
        if v[0]:
            key = (adj[0], adj[1])

            # Same move is valid in other direction
            if key in valid_moves:
                data = valid_moves.get(key)
                to_flip, score = data

                # Update Score
                score += v[1][-1]
                # Update to_flip list
                to_flip = list(set(to_flip + v[1][0]))

                move_result = (to_flip, score)
                valid_moves[key] = move_result

            else:
                valid_moves[key] = v[1]

    return valid_moves


def flip(board, color, valid_move):
    '''
    Description: Change the squares made by the movement.

    Return: Return the new board.
    '''
    copy_board = list(board)

    move, move_result = valid_move
    row, col = move

    to_flip, _ = move_result

    copy_board[row][col] = color

    # Flip the squares made by the movement
    for f in to_flip:
        copy_board[f[0]][f[1]] = color

    return copy_board


def difference_squares(board, color):
    mine, theirs = 0, 0

    opp = opponent(color)

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == color:
                mine += 1
            elif board[row][col] == opp:
                theirs += 1

    return (mine - theirs / (mine + theirs)) * 100


# def corner_occupancy(board, color):
#     pass


def score(board, color):

    diff = difference_squares(board, color)
    return diff


def movement(position):
    row, col = position
    return (col * 8) + row
