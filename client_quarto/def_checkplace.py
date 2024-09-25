def check_place(row ,column ,board):
    while row > 3 or column > 3 :
        if row > 3 :
            print('the choosen row doesn\'t exist. choose a row!')
            row = int(input(' ▷ row = '))
        if column > 3 :
            print('the choosen column doesn\'t exist. choose a column!')
            column = int(input(' ▷ column = '))
    while board[row][column] != '    ':
        print('the choosen place is already taken. choose another place!')
        row = int(input(' ▷ row = '))
        column = int(input(' ▷ column = '))
        
    return row , column
