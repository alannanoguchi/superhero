import random

# The hero will use an Ability to save the world
class Ability:

    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
            name: String
            max_damage: Integer
        '''
        # TODO: Instantiate the variables listed in the docstring with then 
        # values passed in
        self.name = name
        self.attack_strength = attack_strength
       
    def attack(self):
        '''Return a value between 0 and the value set by self.max_damage'''
        # TODO: Use random,randomint(a, b) to select a ramdon attack value.
        # Return an attack value between 0 and the full attack.
        # Hint: The constructor initializes the maximum attack value.
        return random.randint(0, self.attack_strength)


class Armor:
        def __init__(self, name, max_block):
            '''Instantiate instance properties. 
                name: String
                max_block = Integer
            '''
            self.name = name
            self.max_block = max_block
            # TODO: Create instance variables for the values passed in.


        def block(self):
            ''' Return a random value between 0 and the initialized max_block strength '''
            return random.randint(0, self.max_block)


class Hero:
    def __init__(self, name, starting_health = 100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        # TODO: Initialized instance variables values as instance variables
        # (some of these valyes are passed in above, 
        # others will need to be set as a starting value)
        # abilities and armors are lists that will contain objects we can use
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # TODO: Add ability object to abilities: list
        self.abilities.append(ability)







if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed

    # Test the Ability class: (
    # expected output: 
    # Debugging Ability
    # plus a random integer 0-20)
    # ability1 = Ability("Debugging Ability", 20)
    # print(ability1.name)
    # print(ability1.attack())

    # Test the Hero class: (
    # expected output:
    # Grace Hopper
    # 200)
    # my_hero = Hero("Pumpkin Pie", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)

    # Test the abilities method inside the Abilities class: (
    # expected output:
    # [<__main__.Ability object at 0x7f8debceeb00])
    ability1 = Ability("Great Debugging", 50)
    ability2 = Ability("Super Strength", 80)
    ability3 = Ability("Super Speed", 70)
    hero = Hero("Pumpkin Pie", 200)
    hero.add_ability(ability1)
    hero.add_ability(ability2)
    hero.add_ability(ability3)
    print(hero.abilities)