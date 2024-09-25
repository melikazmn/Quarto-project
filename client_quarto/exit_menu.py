def exit_menu():
    print('◉ what do you want to do?\n 1-exit?\n 2-play again ?\n 3-view scoreboard?')
    choice = input(' ▷ ')
    if choice == '1':
        return 'exit'
    elif choice == '2':
        return 'play again'
    elif choice == '3':
        return 'view scoreboard'
    else:
        return exit_menu()
          