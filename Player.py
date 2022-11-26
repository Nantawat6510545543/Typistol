from math import exp

class Player:
    def __init__(self, name="Guest", level=1):
        self.__name = name
        self.__level = level
        self.__health = 8
        self.__equipment_dict = {"health": 1, "attack": 1, "defense": 1}
        self.__item_dict = {}

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, reset):
        self.__level = reset

    @property
    def max_health(self):
        bonus = 1.5 * sum([v for k, v in self.__equipment_dict.items()
                           if k == "health"])
        return round(self.__level * bonus)

    @property
    def attack(self):
        bonus = 1.3 * sum([v for k, v in self.__equipment_dict.items()
                           if k == "attack"])
        return round(self.__level * bonus)

    @property
    def defense(self):
        bonus = 1.1 * sum([v for k, v in self.__equipment_dict.items()
                           if k == "defense"])
        return round(self.__level * bonus)

    def leveling(self, experience):
        self.__level += experience

    def misspell(self, difficulty):
        self.__health -= difficulty

    def __repr__(self):
        return f"Player's name : {self.__name}, " \
               f"Level : {self.__level}\n" \
               f"Health : {self.__health}/{self.max_health}, " \
               f"Attack : {self.attack}, " \
               f"Defense : {self.defense}"
