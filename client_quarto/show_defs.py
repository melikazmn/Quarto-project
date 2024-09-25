def show_mohre(lst_pieces):
    part1 = lst_pieces[:len(lst_pieces)//2]
    part2 = lst_pieces[len(lst_pieces)//2:]
    print()
    print(' ║ '.join(part1))
    print()
    print(' ║ '.join(part2))
    print()
    

def show_boardgame(board):
    print('    0    1    2    3')
    print(' '+'═'*21)
    for i in range(4):
        print(str(i)+'║'+'║'.join(board[i])+'║')
        print(' '+'═'*21) 
    