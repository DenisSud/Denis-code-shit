"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if len(set(row)) == 1 and row[0] != 0:
            return row[0]

    for col in range(len(board)):
        if len(set([row[col] for row in board])) == 1 and board[0][col] != 0:
            return board[0][col]

    if len(set([board[i][i] for i in range(len(board))])) == 1 and board[0][0] != 0:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1 and board[0][len(board)-1] != 0:
        return board[0][len(board)-1]

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board)):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    curr_player = player(board)
    if curr_player == X:
        v = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            min_val = min_value(new_board)
            if min_val > v:
                v = min_val
                optimal_action = action
    else:
        v = math.inf
        for action in actions(board):
            new_board = result(board, action)
            max_val = max_value(new_board)
            if max_val < v:
                v = max_val
                optimal_action = action

    return optimal_action


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        new_board = result(board, action)
        v = max(v, min_value(new_board))

    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        new_board = result(board, action)
        v = min(v, max_value(new_board))

    return v
