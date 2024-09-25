from socketio import *
from def_scoreboard import *
from show_defs import *
from description import *
from def_checkplace import *
from def_check_win import *
from exit_menu import *
import os


client = Client()
client.connect("http://127.0.0.1:5000")


board = [[' '*4, ' '*4, ' '*4, ' '*4], [' '*4, ' '*4, ' '*4, ' '*4],
         [' '*4, ' '*4, ' '*4, ' '*4], [' '*4, ' '*4, ' '*4, ' '*4]]  # board

lst_pieces = ['btfc', 'btfq', 'btec', 'bteq', 'bsfc', 'bsfq', 'bsec',
              'bseq', 'wtfc', 'wtfq', 'wtec', 'wteq', 'wsfc', 'wsfq', 'wsec', 'wseq']


@client.event
def connect():
    print("I'm connected")


@client.event
def connect_error(data):
    print("The connection failed!")


@client.event
def disconnect():
    print("disconnected!")


def added_successfully(x):  # 6-added successfully response
    global user_name
    if x == 'username is not available':  # 7-if username is not available we take another username
        print(x)
        user_name = input('↬username: ')
        client.emit('receive username', data=user_name,
                    callback=added_successfully)
    elif x == 'Do not use space in your username!':
        print(x)
        user_name = input('↬username: ')
        client.emit('receive username', data=user_name,
                    callback=added_successfully)
    else:
        print(x)
        # 8-go to server to send a description to each client
        client.emit('start and descriptions' )

# 1-input username
print('\n╔╗╚╝╔╗╚╝ hello, welcome to quarto! ╚╝╔╗╚╝╔╗\n')
user_name = input('↬username: ')
client.emit('receive username', data=user_name,
            callback=added_successfully)  # 2- emiting the username to server to save the names


@client.on('start comment and descriptions')  # 12-print a description
def start_des(playerskeys):
    global board ,lst_pieces
    global sid_player1
    global sid_player2
    sid_player1 = playerskeys[2]
    sid_player2 = playerskeys[3]
    lst_pieces = ['btfc', 'btfq', 'btec', 'bteq', 'bsfc', 'bsfq', 'bsec',
              'bseq', 'wtfc', 'wtfq', 'wtec', 'wteq', 'wsfc', 'wsfq', 'wsec', 'wseq']
    board = [[' '*4, ' '*4, ' '*4, ' '*4], [' '*4, ' '*4, ' '*4, ' '*4],
         [' '*4, ' '*4, ' '*4, ' '*4], [' '*4, ' '*4, ' '*4, ' '*4]]
    print('\n The game starts with '+ playerskeys[0] + ' and '+playerskeys[1])
    print(des())
    # 13-go to ask for a piece from the first client
    client.emit('choose a piece on server')


# 16-show the board and pieces to the first client to choose a piece
@client.on('choose and show piece')
def choose_and_show():
    global board
    global lst_pieces
    show_mohre(lst_pieces)
    show_boardgame(board)
    print('\n ◉ choose a piece !')
    piece = input(' ▷ ')
    while piece not in lst_pieces:  # 17- if the piece doesnt exist we ask the client to choose again
        print('The choosen piece doesn\'t exist!')
        print('\n ◉ choose another piece !')
        piece = input(' ▷ ')
    lst_pieces.remove(piece)
    client.emit('choose a place on server', data=[piece, board])
    # 17-sending the choosen piece to server


def new_turn(data): # 27-new round 
    client.emit('choose a piece on server')


# 19- asking the second client to choose a place
@client.on('choose a place on client')
def choose_a_place_on_client(piece_board):
    global board, lst_pieces
    piece = piece_board[0]
    board = piece_board[1]
    lst_pieces.remove(piece)
    show_boardgame(board)
    print('\n◉ the choosen piece is : '+ piece +' .choose a row and a column!')
    row = int(input(' ▷ row = '))
    column = int(input(' ▷ column = '))
    # 20- check if the choosen place is availabe
    row, column = check_place(row, column, board)
    board[row][column] = piece
    result = check_win(board)  # 21- check if anyone has win or not
    if result == 'the winner is ':
        client.emit('the winner and loser on server', data=['win' ,board])
    elif result == 'continue' and lst_pieces == []:
        client.emit('the winner and loser on server' ,data= ['equal' ,board])
    elif result == 'continue':  # 24- if there is a winner goes to server to send the final menu
        client.emit('changing the role', data=board, callback=new_turn) #25- if there is no winner the game will continue


@client.on('final menu')#28-send win/lose/scoreboard
def finel_menu(winner_loser_scoreboard):
    global board
    board = winner_loser_scoreboard[2]
    show_boardgame(board)
    if winner_loser_scoreboard[0] == 'winner':
        print('\nYOᑌ ᗩᖇE TᕼE ᗯIᑎᑎEᖇ')
    if winner_loser_scoreboard[0] == 'loser':
        print('\nYOᑌ ᗩᖇE TᕼE ᒪOᔕEᖇ')
    if winner_loser_scoreboard[0] == 'no win no lose':
        print('ᑎO ᗯIᑎᑎEᖇ ᑎO ᒪOᔕEᖇ!')

    what_to_do = exit_menu() #29- showing the menu
    if what_to_do == 'exit' :
        client.disconnect() #30-disconnecting from server
    if what_to_do == 'play again':
        os.system('CLS')
        print('\nwaiting for another player to join\n')
        client.emit('play again')
    if what_to_do == 'view scoreboard':
        print()
        print(winner_loser_scoreboard[1])
        print()
        print('\n◉ what do you want to do?\n 1-exit?\n 2-play again ? ')
        choice = input(' ▷ ')
        if choice == '1':
            client.disconnect()
        elif choice == '2':
            os.system('CLS')
            print('\n◉ waiting for another player to join !\n')
            client.emit('play again')
        else:
            while choice not in ['1','2'] :
                print('\n◉ what do you want to do?\n 1-exit?\n 2-play again ? ')
                choice = input(' ▷ ')
                if choice == '1':
                    client.disconnect()
                elif choice == '2':
                    os.system('CLS')
                    print('\n◉ waiting for another player to join !\n')
                    client.emit('play again') 

            