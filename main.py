class Character:
    def __int__(self, name, race, level=1):
        self.name = name
        self.race = race
        self.level = level 

def Level_up(self):
    self.__level += 1

def show_info(self):
    print(f"Name: {self.name}/nRace: {self.race}/nlevel: {self.level}")

class Warrior(Character):
    def __init__(self, name, race, weapon):
        super().__int__(name, race)
        self.weapon = weapon

class Mage(Character):
    def __init__(self, name, race, magic_type):
        super().__int__(name, race)
        self.magic_type = magic_type

class Character:
    def special_ability(self):
        print("This character has no special abilities.")

class Warrior(Character):
    def special_ability(self):
        print(f"{self.name} swings their {self.weapon} mightily!")

class Mage(Character):
    def special_ability(self):
        print(f"{self.name} casts a powerful {self.magic_type} spell!")

grommash = Warrior("Grommash", "Orc", "Axe")
jaina = Mage("Jaina", "Human", "Frost")

grommash.show_info()
grommash.special_ability()

jaina.show_info()
jaina.special_ability()
jaina.level_up()
jaina.show_info()