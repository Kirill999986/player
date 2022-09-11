from character import Character
comand = input('в видите команду: ')
player1 = Character()
if comand == 'damage':
    player1.take_damage(5)
    print(player1.stats())