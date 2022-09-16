from character import Character
import random
player1 = Character()
clas = input('выберите класс: ')
if clas == 'healer':
        hp = 100
        while hp > 0:
            hi = (random.randint(1, 100))
            comand = input('в видите команду: ')
            if comand == 'damage':
                hp = hp - 10
                player1.take_damage(10)
                print(player1.stats())
            if comand == 'healing':
                if hp >= 100:
                    print('maximum hp')
                if hp <= 99:
                    if hi <= 90:
                        hp = hp + 5
                        player1.take_healing(5)
                        print(player1.stats())
                    if hi >= 90:
                        player1.take_damage(hp)
                        hp = 100
                        player1.take_healing(100)
                        print(player1.stats())
        print('game over')