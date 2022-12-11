from math import exp, floor


class Player:
    """
    Player class represented as a user and containing values for player.
    """
    def __init__(self, name="", level=100):
        self.__name = name
        self.__level = level
        self.__experience = 0
        self.__equipment_dict = {"HP": 23, "ATK": 21, "DEF": 20}
        self.__item_dict = {"S": [15, 5], "M": [7, 10], "L": [3, 20]}
        self.__health = self.max_health

    @property
    def name(self):
        return self.__name

    @property
    def equipment(self):
        return "\n".join(
            [f"{k}+{v}" for k, v in self.__equipment_dict.items()])

    @property
    def item(self):
        return "Potion\n" + "\n".join(
            [f"{k} : {v[0]}" for k, v in self.__item_dict.items()])

    @property
    def limit(self):
        return self.__level ** 2 - self.__level + 1

    @property
    def max_health(self):
        return round(self.__level * 1.5) \
               + sum([v for k, v in self.__equipment_dict.items()
                      if k == "HP"])

    @property
    def health(self):
        return max(0, self.__health)

    @property
    def attack(self):
        return round(self.__level * 1.3) \
               + sum([v for k, v in self.__equipment_dict.items()
                      if k == "ATK"])

    @property
    def defense(self):
        return round(self.__level * 1.1) \
               + sum([v for k, v in self.__equipment_dict.items()
                      if k == "DEF"])

    def get_equipment(self, equipment, status):
        if self.__equipment_dict[equipment] < status:
            self.__equipment_dict[equipment] = status

    def get_item(self, size, amount):
        self.__item_dict[size][0] += amount

    def use_item(self, size, difficulty):
        """
        Using an item if it doesn't exist counts as a misspelling.
        """
        if self.__item_dict[size][0] != 0:
            self.__item_dict[size][0] -= 1
            self.__health += self.__item_dict[size][1]
            if self.__health > self.max_health:
                self.__health = self.max_health
        else:
            self.misspell(difficulty)

    def leveling(self, experience):
        """
        Earn experience and level up if you reach the experience threshold.
        """
        self.__experience += experience
        if self.__experience >= self.limit:
            self.__experience -= self.limit
            self.__level += 1
            self.__health = self.max_health

    def misspell(self, difficulty):
        """ Reduce health by difficulty. """
        self.__health = floor(
            self.__health * (1 - 0.4 * (1 / (1 + exp(-0.05 * difficulty)))))

    def damage(self, attack):
        """ Reduces health based on damage taken. """
        self.__health -= attack

    def __repr__(self):
        return f"Name : {self.__name}, " \
               f"Experience : {self.__experience}/{self.limit}, " \
               f"Level : {self.__level}\n" \
               f"Health : {self.health}/{self.max_health}, " \
               f"Attack : {self.attack}, " \
               f"Defense : {self.defense}"
