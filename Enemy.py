from math import exp


class Enemy:
    def __init__(self, difficulty=1):
        self.__difficulty = difficulty
        self.__health = round(difficulty * 2.5)

    @property
    def health(self):
        return self.__health

    @property
    def experience_drop(self):
        return round(self.__difficulty * 1.5)

    @property
    def attack(self):
        return round(self.__difficulty * 1.25)

    @property
    def attack_speed(self):
        return 20 - 10 * ((1 / (1 + exp(-0.05 * self.__difficulty))) ** 10)

    @property
    def defense(self):
        return round(self.__difficulty * 1.1)

    @property
    def drop_rate(self):
        return 100 * (1 / (1 + exp(-0.05 * self.__difficulty))) ** 10

    def damage(self, attack):
        """
        Reduces health based on damage taken.
        """
        self.__health -= attack
