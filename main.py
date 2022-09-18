from character import Character
import random
a = 0
hi = 50
hp = 100
player1 = Character()
clas = input('выберите класс: ')
if clas == 'healer':
        while a < hi:
            print('new game')
            print(player1.stats())
            while hp > 0:
              hi = (random.randint(1, 100))
              no = (random.randint(1, 100))
              comand = input('в видите команду: ')
              if comand == 'damage':
                  if hi >= 10:
                    if no <= 90:
                      hp = hp - 10
                      player1.take_damage(10)
                      print(player1.stats())
                  if hi <= 10:
                   hp = hp - 20
                   player1.take_damage(20)
                   print(player1.stats())
                   print('krit damage')
                  if no >=90:
                   print(player1.stats())
                   print('missed')
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
                          print('super healing')
            if hp <= 0:
                while hp<0:
                    player1.take_healing(1)
                    hp = hp + 1
            if hp == 0:
              player1.take_healing(100)
              hp = 100
            print('game over')