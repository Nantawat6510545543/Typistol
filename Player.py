import json


class Player:
    def __init__(self, name="", level=1):
        self.__name = name
        self.__level = level
        self.__experience = 0
        self.__equipment_dict = {"health": 1, "attack": 1, "defense": 1}
        self.__item_dict = {"reduce": 0}
        self.__health = self.max_health

    @property
    def name(self):
        return self.__name

    @property
    def experience(self):
        return self.__experience

    @property
    def limit(self):
        return self.__level ** 2 - self.__level + 1

    @property
    def max_health(self):
        bonus = 1.5 * sum([v for k, v in self.__equipment_dict.items()
                           if k == "health"])
        return round(self.__level * bonus)

    @property
    def health(self):
        return self.__health

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
        self.__experience += experience
        if self.__experience >= self.limit:
            self.__experience -= self.limit
            self.__level += 1
            self.__health = self.max_health

    def misspell(self, difficulty):
        self.__health -= round(difficulty / 2) - round(self.defense / 10)

    def damage(self, attack):
        self.__health -= attack

    def __repr__(self):
        return f"Name : {self.__name}, " \
               f"Experience : {self.__experience}/{self.limit}, " \
               f"Level : {self.__level}\n" \
               f"Health : {self.__health}/{self.max_health}, " \
               f"Attack : {self.attack}, " \
               f"Defense : {self.defense}"
