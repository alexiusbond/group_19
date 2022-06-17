from random import randint, choice
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.name} health: {self.health} [{self.damage}]'


class Boss(GameEntity):
    def __init__(self, name, health, damage, defence_type):
        GameEntity.__init__(self, name, health, damage)
        self.__defence_type = defence_type

    @property
    def defence_type(self):
        return self.__defence_type

    @defence_type.setter
    def defence_type(self, value):
        self.__defence_type = value

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence_type = hero.super_ability_type


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability_type):
        GameEntity.__init__(self, name, health, damage)
        self.__super_ability_type = super_ability_type

    @property
    def super_ability_type(self):
        return self.__super_ability_type

    @super_ability_type.setter
    def super_ability_type(self, value):
        self.__super_ability_type = value

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = randint(2, 5)
        boss.health -= self.damage * coeff
        print(f'Warrior applied critical damage: {self.damage * coeff}')


class Berserk(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        Hero.__init__(self, name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self is not hero:
                hero.health += self.__heal_points


class Magic(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        boost_point = randint(2, 5)
        for hero in heroes:
            if hero.health > 0 and boss.health > 0:
                hero.damage += boost_point


round_number = 0


def boss_hits(boss, heroes):
    for hero in heroes:
        if hero.health > 0:
            hero.health -= boss.damage


def heroes_hit(boss, heroes):
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 \
                and boss.defence_type != hero.super_ability_type:
            boss.health -= hero.damage
            hero.apply_super_power(boss, heroes)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!!!")
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss won!!!")
    return all_heroes_dead


def print_statistics(boss, heroes):
    print(f'ROUND {round_number} ________________')
    print("BOSS " + str(boss) + " Defence: " + str(boss.defence_type))
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss_hits(boss, heroes)
    heroes_hit(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss("Gorilla", 800, 50, None)

    warrior = Warrior("Hektor", 270, 10)
    magic = Magic("Albert", 260, 15)
    doc = Medic("Aibolit", 240, 5, 15)
    berserk = Berserk("John", 280, 20)
    assistant = Medic("Strange", 290, 10, 5)
    heroes = [warrior, magic, doc, berserk, assistant]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()
