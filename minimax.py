from othello import flip,  moves, opponent, score


def minimax(board, color, depth, alpha, beta, maximizingPlayer):
    best_move = None

    if depth == 0:
        return (score(board, color), None)

    if len(moves(board, color)) == 1:
        valid_moves = moves(board, color)
        for move, move_result in valid_moves.items():
            return (score(board, color), move)

    if maximizingPlayer:
        maxEval = (float('-inf'))

        valid_moves = moves(board, color)

        for move, move_result in valid_moves.items():
            new_board = flip(board, color, (move, move_result))

            evaluation = minimax(
                new_board, opponent(color), depth - 1,
                alpha, beta, False)

            if evaluation[0] > maxEval:
                maxEval = evaluation[0]

                if evaluation[1] is not None:
                    best_move = evaluation[1]
                else:
                    best_move = move

            alpha = max(alpha, evaluation[0])

            if beta <= alpha:
                break

        return (maxEval, best_move)

    else:
        minEval = float('inf')
        valid_moves = moves(board, color)

        for move, move_result in valid_moves.items():
            new_board = flip(board, color, (move, move_result))

            evaluation = minimax(
                new_board, opponent(color), depth - 1,
                alpha, beta, True)

            if evaluation[0] < minEval:
                minEval = evaluation[0]

                if evaluation[1] is not None:
                    best_move = evaluation[1]
                else:
                    best_move = move

            beta = min(beta, evaluation[0])
            if beta <= alpha:
                break

        return (minEval, best_move)
