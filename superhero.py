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
    
    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor
        #  object.
        #
        #  return the new armor object with values set by user.
        Armor.name = input("Enter armor name: ")
        Armor.max_block = input("Enter defensive strength: ")
        return Armor.name, Armor.max_block
            
    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        # TODO: This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and
        # abilities.
        # Call the methods you made above and use the return values to build
        # your hero.
        #
        # return the new hero object
        # Hero's Information:
        name = input("Hero's name: ")
        health = input("Insert starting health: ")
        hero = Hero(name, health)

        build_hero = True
        while build_hero == True:
            hero_options = input("Please use numbers to enter options:\n1 Ability\n2 Armor\n3 Weapon\n4 Finished: ")
            if hero_options == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif hero_options == "2":
                armor = self.create_armor()
                hero.add_armor(armor)
            elif hero_options == "3":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif hero_options == "4":
                build_hero = False          
            else:
                print("Invalid option. Follow instructions.")
        
        return hero


    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        #
        # Add the created hero to team one.
        self.number_of_heroes = int(input("How many heroes are on each team?: "))
        team_one_name = input("Enter Team One Name: ")
        self.team_one = Team(team_one_name)

        for hero in range(self.number_of_heroes):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

        self.team_one.view_all_heroes()


    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        #
        # Add the created hero to team two.
        team_two_name = input("Enter Team Two Name: ")
        self.team_two = Team(team_two_name)
        
        for hero in range(self.number_of_heroes):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

        self.team_two.view_all_heroes()


    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        Team.fight(self.team_one, self.team_two)

    
    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.
        self.team_one.stats()
        self.team_two.stats()

        winning_team = self.team_one.atack(self.team_two)
        if winning_team == self.team_one.name:
            for hero in self.team_one.heroes:
                if hero.status == "Alive":
                    print("Remaining Heroes: " + hero.name)
        elif winning_team == self.team_two.name:
            for hero in self.team_two.heroes:
                if hero.status == "Alive":
                    print("Remaing Heroes: " + hero.name)
        print("Congratulations {}! Your team wins!".format(winning_team))


            


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
