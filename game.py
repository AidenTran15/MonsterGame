player = {'name':'Aiden', 'attack': 10, 'heal': 16, 'health': 100}
monster = {'name':'Giant', 'attack': 12, 'health': 100}
print('Please select action')
print('1> Attack')
print('2> Heal')

player_choice = input()

if player_choice == '1':
    print('Attack')
elif player_choice == '2':
    print('Heal player')
else:
    print('Invalid Input')
