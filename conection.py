import socketio

from othello import reshape_board, printboard, movement
from minimax import minimax

USERNAME = 'JoseRa'
TOURNAMENT_ID = 142857
USER_ROL = 'player'

GAME_ID = 0
PLAYERTURN_ID = 0
BOARD = []


# Standard Python
sio = socketio.Client()

sio.connect('http://192.168.1.148:4000')


@sio.event
def connect():
    # Sign in
    print('Se conecto')
    sio.emit('signin', {
        'user_name': USERNAME,
        'tournament_id': TOURNAMENT_ID,
        'user_role': USER_ROL
        })

# Ready
@sio.on('ready')
def on_message(data):
    global GAME_ID, PLAYERTURN_ID, BOARD

    GAME_ID = data['game_id']
    PLAYERTURN_ID = data['player_turn_id']
    BOARD = data['board']

    # printboard(reshape_board(BOARD))

    move = minimax(
        reshape_board(BOARD), PLAYERTURN_ID, 5,
        float('-inf'), float('inf'), True
        )
    print(move)
    move = movement()

    sio.emit('play', {
        'user_name': USERNAME,
        'tournament_id': TOURNAMENT_ID,
        'user_role': USER_ROL,
        'movement': move
        })


@sio.on('finish')
def on_finish(data):
    GAME_ID = data['game_id']
    PLAYERTURN_ID = data['player_turn_id']
    winnerTurnID = data['winner_turn_id']
    board = data['board']

    print('You', PLAYERTURN_ID)
    print('Winner', winnerTurnID)

    print('')
    print('Board: ')
    printboard(reshape_board(board))

    # TODO: Your cleaning board logic here

    sio.emit('player_ready', {
        'tournament_id': TOURNAMENT_ID,
        'game_id': GAME_ID,
        "player_turn_id": PLAYERTURN_ID
    })

    @sio.on('ready')
    def on_message(data):
        global GAME_ID, PLAYERTURN_ID, BOARD

        GAME_ID = data['game_id']
        PLAYERTURN_ID = data['player_turn_id']
        BOARD = data['board']
