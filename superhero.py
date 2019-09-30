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
        self.max_damage = attack_strength
       
    def attack(self):
        '''Return a value between 0 and the value set by self.max_damage'''
        # TODO: Use random,randomint(a, b) to select a ramdon attack value.
        # Return an attack value between 0 and the full attack.
        # Hint: The constructor initializes the maximum attack value.
        return random.randint(0, self.max_damage)


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
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # TODO: Add ability object to abilities: list
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks. 
            return: total: Int
        '''
        # TODO: This method should run Ability.attack() on every ability
        # in self.abilities and runs the total as an integer.
        total_damage = 0
        for ability in self.abilities:
            attack = ability.attack()
            total_damage += attack
        
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        # TODO: Add armor object that is passed in to 'self.armors'
        self.armors.append(armor)

    def defend(self, damage_amt):
        '''Runs 'block' method on each armor.
            Returns sum of all blocks
        '''
        # TODO: This method should run the block method on each armor in self.armors
        total_armor = 0
        for damage_amt in self.armors:
            total_armor += damage_amt.block()
        return total_armor

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_health to the current 
        # minue the amount returned from calling self.defend(damage).
        self.current_health -= damage

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not. 
        '''
        # TODO: Check whether the hero is alive and return true or false
        if self.current_health > 0:
            return True
        else: 
            return False

    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Fight each hero until a victor emerges.
        # Print the Victor's name to the screen.
        self.opponent = opponent 
        while self.is_alive()== True and opponent.is_alive() == True:
            if len(self.abilities) > 0 or len(opponent.abilities) > 0:
                self_attack = hero.attack()
                opponent_attack = opponent.attack()

                # if hero is taking damage, it is because the opponent attacked vise versa
                self.take_damage(opponent_attack)
                opponent.take_damage(self_attack)

                if self.is_alive == False:
                    print("The winner is: {}!".format(opponent.name))
                else:
                    print("The winner is: {}!".format(self.name))
            else:
                print("Draw!")


class Weapon(Ability):
    def attack(self):
        """ This method returns a random value between 1/2 
        to the full attack power of the weapon.
        """
        # TODO: Use what you learned to complete this method
        return random.randint(self.max_damage//2, self.max_damage)

class Team(Hero):
    def __init__(self, name):
        ''' Initialize your team with its team name 
        '''
        # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        ''' Remove hero from heroes list.
            If Hero isn't found return 0
            '''
            # TODO: Implement this method to return the hero from the list given their name
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
            else:
                return 0
    
    def view_all_heroes(self):
        ''' Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their nmaes to the terminal.
        for hero in self.heroes:
            print(hero.name)
        
    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # TODO: Add the Hero object that is passed in to the list of heroes in 
        # self.heroes
        self.heroes.append(hero)

    
            


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed

    hero = Hero("Pumpkin Pie")
    opponent = Hero("Vanilla Cake")
    ability1 = Ability("Lazer Eyes", 65)
    ability2 = Ability("Super Strength", 80)
    ability3 = Ability("Super Speed", 70)
    hero.add_ability(ability1)
    hero.add_ability(ability2)
    opponent.add_ability(ability2)
    opponent.add_ability(ability3)
    hero.fight(opponent)
