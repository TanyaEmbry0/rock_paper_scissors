import sys

ask_player_one = input('Do you wanna play?')
ask_player_two = input('Do you wanna play?')

if ask_player_one == 'Yes' and ask_player_two == 'Yes':
    print('OK, let`s GO!')

    user_one_choice = input('That`s your choice player 1?')
    user_two_choice = input('What`s your choice player 2?')

    def users_game(user1, user2):
        if user1 == user2:
            print('Tie!')
            return
        elif user1 == 'rock':
            if user2 == 'paper':
                print('PAPER WIN!')
            elif user2 == 'scissors':
                print('ROCK WIN!')
            else:
                print('Thunder hit you!')
        elif user1 == 'paper':
            if user2 == 'rock':
                print('PAPER WIN!')
            elif user2 == 'scissors':
                print('SCISSORS WIN')
            else:
                print('Thunder hit you!')
        elif user1 == 'scissors':
            if user2 == 'rock':
                print('ROCK WIN!')
            elif user2 == 'paper':
                print('SCISSORS WIN!')
            else:
                print('Thunder hit you!')
        else:
            print('Are you kidding me idiot?')
    print(users_game(user_one_choice, user_two_choice))
else:
    print('Go home, stupid!')



