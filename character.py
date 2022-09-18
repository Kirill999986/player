class Character:
    def __init__(self, name='Kirill', healing= 5, hp=100, accuracy=90, armor=30, damage=10, kritdamage=20, chancekritdamage=10):
        self.name = name
        self.hp = hp
        self.accuracy = accuracy
        self.armor = armor
        self.damage = damage
        self.healing = healing
        self.kritdamage = kritdamage
        self.chancekritdamage = chancekritdamage

    def take_damage(self, damage):
        self.hp  -= abs(damage)

    def take_healing(self, damage):
        self.hp  += abs(damage)

    def stats(self):
        return \
            f' === {self.name} ===\n' \
            f' здоровье {self.hp}\n' \
            f' броня {self.armor}\n' \
            f' атака {self.damage}\n' \
            f' критическая атака {self.kritdamage}\n' \
            f' шанс критической атаки {self.chancekritdamage}%\n' \
            f' шанс попасть по врагу {self.accuracy}%\n'\
            f' востановление здоровья {self.healing}\n'