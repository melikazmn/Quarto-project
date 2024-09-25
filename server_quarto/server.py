from io import SEEK_CUR
from gevent import pywsgi
from socketio import *
from def_scoreboard import *


server = Server(async_mode='gevent')

players = {}  # {username :[sid , win]}

board = [[' '*4, ' '*4, ' '*4, ' '*4], [' '*4, ' '*4, ' '*4, ' '*4],
         [' '*4, ' '*4, ' '*4, ' '*4], [' '*4, ' '*4, ' '*4, ' '*4]]  # board

lst_pieces = ['btfc', 'btfq', 'btec', 'bteq', 'bsfc', 'bsfq', 'bsec',
              'bseq', 'wtfc', 'wtfq', 'wtec', 'wteq', 'wsfc', 'wsfq', 'wsec', 'wseq']
sid_player1 = '-'
sid_player2 = '-'
username1 = '_'
username2 = '_'
final_scoreboard = ''


@server.event
def connect(sid, environ, auth):
    print(sid, "connected!")

# 3- receiving username and adding them in a dict with a list of sid and winning times
@server.on('receive username')
def receive_username(sid, data):
    global players
    if data in players:
        # 4- if the usrname is already taken it will ask the client to choose another username
        return 'username is not available'
    if ' ' in data:
        return 'Do not use space in your username!'
    players[data] = [sid, 0]
    with open ('scoreboard.txt','r+') as scb:
        scoreboard_avalie = scb.read()
        if data not in scoreboard_avalie:
            scb.write(data +' '+ str(0)+' win '+ str(0) + ' lose|')
    # 5- send a response to client that he/she is added successfully
    return '► added successfully ◄'


# 9-whenever we have 2 clients we start to send description
@server.on('start and descriptions')
def game_start(sid ):
    global players ,sid_player1 ,sid_player2 ,username1 ,username2
    #if data == 'play again':
      
    if len(players) == 2:
        playerskeys = []
        for i in players.keys():
            playerskeys.append(i)  # 10-saving the usernames and sids
        username1 = playerskeys[0]  # username bazikon 1
        username2 = playerskeys[1]   # username bazikon 2
        sid_player1 = players[username1][0]  # sid bazikon 1
        sid_player2 = players[username2][0]  # sid bazikon 2
        server.emit('start comment and descriptions',
                    data=playerskeys+[sid_player1, sid_player2] ,sid=sid_player1)  # 11-sending usernames and sids to clients and description
        #server.emit('start comment and descriptions',
                    #data=playerskeys+[sid_player1, sid_player2] ,sid=sid_player2)  # 11-sending usernames and sids to clients and description


# 14-ask the first client to choose a piece
@server.on('choose a piece on server')
def ask_for_piece(sid):
    if sid == sid_player1:  # for the first client
        server.emit('choose and show piece',  # 15-go to client event to ask for a piece
                    room=sid_player1)

# 13-ask the second client to choose a place


@server.on('choose a place on server')
def choose_a_place_on_server(sid, piece_board):
    global lst_pieces, board
    piece = piece_board[0]
    board = piece_board[1]
    lst_pieces.remove(piece)  # 18-ask the second client to choose a place
    
    server.emit('choose a place on client', data=[
                piece, board], room=sid_player2)


@server.on('the winner and loser on server')
# 22- sending the win messege to winner and lose messege to loser nad opening the menu
def win_lose_server(sid ,data):
    global username2 ,sid_player2 ,sid_player1 ,final_scoreboard ,board
    if data[0] == 'win':
        board = data[1]
        final_scoreboard = scoreboard(username2 ,username1) #23-updating the scoreboard
        server.emit('final menu', data=['winner',final_scoreboard ,board], room=sid_player2)
        server.emit('final menu', data=['loser',final_scoreboard ,board], room=sid_player1)
    if data[0] == 'equal':
        final_scoreboard = scoreboard(' ' ,' ')
        server.emit('final menu', data=['no win no lose',final_scoreboard ,board])

@server.on('changing the role') # 26- changing the clients role 
def change_the_role(sid, new_board):
    global players ,username1 ,username2 ,sid_player1 ,sid_player2 ,board
    board = new_board
    new_players = {}
    new_players[username2] = players[username2]
    new_players[username1] = players[username1]
    players = new_players
    playerskeys = []
    for i in players.keys():
        playerskeys.append(i)
    username1 = playerskeys[0]
    username2 = playerskeys[1]
    sid_player1 = players[username1][0]
    sid_player2 = players[username2][0]
    print(players)
    return players


@server.on('play again')
def play_again(sid):
    global players ,username1 ,username2 ,sid_player1 ,sid_player2 ,board ,lst_pieces
    if len(players) == 2:
        lst_pieces = ['btfc', 'btfq', 'btec', 'bteq', 'bsfc', 'bsfq', 'bsec',
              'bseq', 'wtfc', 'wtfq', 'wtec', 'wteq', 'wsfc', 'wsfq', 'wsec', 'wseq']
        board = [[' '*4, ' '*4, ' '*4, ' '*4], [' '*4, ' '*4, ' '*4, ' '*4],
         [' '*4, ' '*4, ' '*4, ' '*4], [' '*4, ' '*4, ' '*4, ' '*4]]
        players = {}
        if sid == sid_player2:
            players[username2] = [sid_player2 ,0]
        if sid == sid_player1:
            players[username1] = [sid_player1 ,0]
    else:
        if sid == sid_player2:
            players[username2] = [sid_player2 ,0]
        if sid == sid_player1:
            players[username1] = [sid_player1 ,0]
        playerskeys =[]
        for i in players.keys():
            playerskeys.append(i)  # 10-saving the usernames and sids
        username1 = playerskeys[0]  # username bazikon 1
        username2 = playerskeys[1]   # username bazikon 2
        sid_player1 = players[username1][0]  # sid bazikon 1
        sid_player2 = players[username2][0]  # sid bazikon 2
        server.emit('start comment and descriptions',data =playerskeys+[sid_player1, sid_player2] ,room =sid_player2 )
        server.emit('start comment and descriptions',data =playerskeys+[sid_player1, sid_player2] ,room =sid_player1 )


app = WSGIApp(server)
pywsgi.WSGIServer(("127.0.0.1", 5000), app).serve_forever()
