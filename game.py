import random

game_running = True

while game_running == True: 
    new_round = True
    player = {'name':'Aiden', 'attack': 10, 'heal': 16, 'health': 100}
    monster = {'name':'Giant', 'attack': 12, 'health': 100}

    print('            Welcome to Monster Game')
    print('---' * 17)
    print('Enter your name')
    player['name'] = input()
    print("")
    print('Hello ' + player['name'] + ", let's start game")


    while new_round == True:

        player_won = False
        monster_won = False

        print('___' * 17 )
        print('  ')
        print('Please select action')
        print('1> Attack')
        print('2> Heal')
        print('3> Exit Game')
        print('4> For More Information')

        player_choice = input()
        monster_attack = random.randint(10,25)
        player_heal = random.randint(10,23)

        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - monster_attack
                if player['health'] <= 0:
                    monster_won = True
            

        elif player_choice == '2':
            player['health'] = player['health'] + player_heal
            player['health'] = player['health'] - monster_attack
            if player['health'] <= 0:
                monster_won = True



        elif player_choice =='3':
             game_running = False
             new_round = False

        elif player_choice == '4':
            print("""
            ---Introduce Monster Game---
    You need to kill monster with name Giant
    Press 1 for attack the monster
    Press 2 for heal health yourself
    Press 3 to exit game
    """"")


        else:
            print('Invalid Input')

        if player_won == False or monster_won == False :
            print(player['name'] + ' has ' + str(player['health']) + ' hp left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' hp left')

        elif player_won:
            print(player(player['name'] + 'won.'))
            new_round = False

        elif monster_won:
            print('Monster won.')
            new_round = False



            










    
