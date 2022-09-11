class Character:
    def __init__(self, name='Kirill', luck=50, hp=100, accuracy=50, armor=30, damage=10, kritdamage=20, level=11, chancekritdamage=10, maxspeed=120):
        self.name = name
        self.luck = luck
        self.hp = hp
        self.accuracy = accuracy
        self.armor = armor
        self.damage = damage
        self.kritdamage = kritdamage
        self.level = level
        self.chancekritdamage = chancekritdamage
        self.maxspeed = maxspeed
    def attack(self, target):
        target.take_damage(self.damage)

    def take_damage(self, damage):
        self.hp  -= abs(damage)

    def stats(self):
        return \
            f' === {self.name} ===\n' \
            f' здоровье {self.hp}\n' \
            f' броня {self.armor}\n' \
            f' атака {self.damage}\n' \
            f' критическая атака {self.kritdamage}\n' \
            f' шанс критической атаки {self.chancekritdamage}%\n' \
            f' максимальная скорость {self.maxspeed}\n' \
            f' точность {self.accuracy}\n' \
            f' удача {self.luck}\n' \
            f' уровень {self.level}\n'
