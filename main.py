from character import Character
import random
a = 0
hi = 50
hp = 100
coins = (random.randint(3, 5))
player1 = Character()
clas = input('выберите класс: ')
if clas == 'healer':
        while a < hi:
            chance = (random.randint(1, 2))
            print('')
            print('new game')
            print('')
            print(player1.stats())
            monster = 100
            print('')
            print('жизней у монстра:', monster)
            while hp > 0 and monster > 0:
              hp = hp - 10
              player1.take_damage(10)
              hi = (random.randint(1, 100))
              no = (random.randint(1, 100))
              comand = input('в видите команду: ')
              if comand == 'damage':
                  if hi >= 10:
                    if no <= 90:
                      monster = monster-10
                  if hi <= 10:
                   monster = monster - 20
                   print('')
                   print('krit damage')
                   print('')
                  if no >=90:
                   print('')
                   print('missed')
                   print('')
              if comand == 'healing':
                  if hp >= 100:
                      print('')
                      print('maximum hp')
                      print('')
                  if hp <= 99:
                      if hi <= 90:
                          hp = hp + 5
                          player1.take_healing(5)
                      if hi >= 90:
                          player1.take_damage(hp)
                          hp = 100
                          player1.take_healing(100)
                          print('')
                          print('super healing')
                          print('')
              if comand == 'surrender':
                  player1.take_damage(hp)
                  hp = 0
              if comand == 'chance':
                  if chance == 1:
                      player1.take_damage(hp)
                      hp = 0
                  if chance == 2:
                      monster = 0
                      player1.take_healing(10)
                      hp = 100
              print('')
              print(player1.stats())
              print('')
              print('жизней у монстра:', monster)
            if monster <= 1:
                print('game win')
                player1.take_coins(coins)
            else:
                print('game over')
            if hp <= 0:
                while hp<0:
                    player1.take_healing(1)
                    hp = hp + 1
            if hp == 0:
              player1.take_healing(100)
              hp = 100