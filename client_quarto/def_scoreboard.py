def scoreboard(winner ,loser):
    with open ('scoreboard.txt' , 'r+') as scb:
        new_uw_joda = ''
        scoreboard = scb.read()
        lst_users_win_lose = scoreboard.split('|')  #['melika 0 win 0 lose','ahmad 1']
        for user in lst_users_win_lose:
            if user != '':
                user_win_lose_joda = user.split() #[['melika '],['0'],[win],[0],[lose]]
                if user_win_lose_joda[0] == winner:
                    wintime = str(int(user_win_lose_joda[1]) + 1)
                    user_win_lose_joda[1] = str(wintime)
                if user_win_lose_joda[0] == loser:
                    losetime = str(int(user_win_lose_joda[3]) + 1)
                    user_win_lose_joda[3] =losetime
                new_uw_joda += ' '.join(user_win_lose_joda) + '|'
        scb.seek(0)
        scoreboard = scb.write(new_uw_joda[0:len(new_uw_joda)-1])
        scb.seek(0)
        scoreboard = scb.read()
        return scoreboard
    