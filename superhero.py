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

    def defend(self, damage_amt=0):
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

    def add_kill(self, num_kills):
        '''Update kills with num_kills'''
        # TODO: This method should add the number of kills to self.kills
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        '''Update dealths with num_deaths'''
        # TODO: This method should add the number of deaths to self.deaths
        self.deaths += num_deaths

    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Fight each hero until a victor emerges.
        # Print the Victor's name to the screen.

        # TODO: Refractor this method to update the number of kills the hero
        # has when the opponent dies. Also update the number of deaths for whoever
        # dies in the fight
        
        # self.opponent = opponent 
        
        while self.is_alive()== True and opponent.is_alive() == True:
            if len(self.abilities) > 0 or len(opponent.abilities) > 0:
                self_attack = self.attack()
                opponent_attack = opponent.attack()

                # if hero is taking damage, it is because the opponent attacked vise versa
                self.take_damage(opponent_attack)
                opponent.take_damage(self_attack)

                if self.is_alive == False:
                    print("The winner is: {}!".format(opponent.name))
                    opponent.kills += 1
                    self.deaths += 1
                else:
                    print("The winner is: {}!".format(self.name))
                    self.kills += 1
                    opponent.deaths += 1
            else:
                print("Draw!")

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)



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

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.

        # while self.hero in hero.is_alive() == True and self.hero in other_team.is_alive() == True:
        #     hero = random.choice(self.heroes)
        #     opponent = random.choice(self.heroes)
        #     return hero.fight()
        alive_heroes = []
        alive_opponents = []

        for hero in self.heroes:
            if hero.is_alive():
                alive_heroes.append(hero)

        for hero in other_team.heroes:
            if hero.is_alive():
                alive_opponents.append(hero)
        
        hero = random.choice(alive_heroes)
        opponent = random.choice(alive_opponents)

        hero.fight(opponent)

            
    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        print("Current stats: ")
        for hero in self.heroes:
            print("Hero: {}".format(hero.name))
            print("Kills/Deaths: {}/{}".format(hero.kills, hero.deaths))

    
class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.
        self.team_one: None
        self.team_two: None

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        # TODO: This method will allow a user to create an ability.
        # Prompt the user for the necessary information to create a new ability object.
        # return the new ability object.
        Ability.name = input("Enter in an ability: ")
        Ability.attack_strength = input("Enter attack strength: ")
        return Ability.name, Ability.attack_strength
        
    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        Weapon.name = input("Enter weapon name: ")
        Weapon.attack_strength = input("Enter attack strength: ")
        return Weapon.name, Weapon.attack_strength
    
            


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed

    team_one = Team("One")
    jodie = Hero("Jodie Foster")
    aliens = Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_two = Team("Two")
    athena = Hero("Athena")
    socks = Armor("Socks", 10)
    athena.add_armor(socks)
    team_two.add_hero(athena)
    # assert team_two.heroes[0].deaths == 0
    team_one.attack(team_two)
    # assert team_two.heroes[0].deaths == 1
    print(team_one.stats()) 