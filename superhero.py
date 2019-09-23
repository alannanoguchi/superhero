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
        




    if __name__ == "__main__":
        # If you run this file from the terminal
        # this block is executed
        ability1 = Ability("Debugging Ability", 20)
        print(ability1.name)
        print(ability1.attack())