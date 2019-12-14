
game_running = True

while game_running == True: 
    new_round = True
    player = {'name':'Aiden', 'attack': 10, 'heal': 16, 'health': 100}
    monster = {'name':'Giant', 'attack': 12, 'health': 100}

    print('             Welcome to Monster Game')
    print('Enter your name')
    player['name'] = input()
    print('Hello ' + player['name'] + ", let's start game")


    while new_round == True:

        player_won = False
        monster_won = False

        print('Please select action')
        print('1> Attack')
        print('2> Heal')
        print('3> Exit Game')
        print('4> To have introduction')

        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - monster['attack']
                if player['health'] <= 0:
                    monster_won = True
            

        
            print('Monster health: ' + str(monster['health']))
            print('Your health: ' + str(player['health']))

        elif player_choice == '2':
            print('Heal player')

        elif player_choice =='3':
             game_running = False
             new_round = False

        elif player_choice == '4':
            print("""
            Introduce Monster Game
    You need to kill monster with name Giant
    Press 1 for attack the monster
    Press 2 for heal health yourself
    Press 3 to exit game
    """"")


        else:
            print('Invalid Input')

        if player_won == True or monster_won == True :
            if player_won == True:
                print('You win')
            else:
                print('You lose')
            game_running = False
            new_round = False











    
