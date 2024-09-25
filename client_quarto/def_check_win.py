def check_win(board):    
    for i in range(4):
        for j in board[i][0]:
            for x in board[i][1:4]:
                if j in x and j!= ' ':
                    flag = True
                else:
                    flag = False
                    break   
            if flag == True:
                return 'the winner is '
             
    for i in range(4):
        for j in board[0][i]:
            for x in range(1,4):
                if j in board[x][i] and j!= ' ':
                    flag = True
                else:
                    flag = False
                    break
            if flag == True:
                return 'the winner is '
            
    
    for j in board[0][0]:
        for i in range(1,4):
            if j in board[i][i] and j!= ' ':
                flag = True
            else:
                flag = False
                break
        if flag == True:
            return 'the winner is '
        
    for j in board[3][0]:    
        for i in range(3):
            if j in board[2-i][i+1] and j!= ' ':
                flag = True
            else:
                flag = False
                break
        if flag == True:
            return 'the winner is '
        
    if flag == False:
        return 'continue'
   
   

