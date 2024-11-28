class Character:
    def __init__(self, name, health, attack_power): # Attributes
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health # Store the original health for maximum limit

    def attack(self, opponent):
        opponent.health -= self.attack_power # Subtracts the attacker's attack_power from the opponent's health.
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0: # Checks the opponents health and if it has dropped to 0 or below.
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        heal_amount = 20 # Health is restored when the method is called with a fixed amount.
        if self.health < self.max_health: # Only heals if the characters current health is below max limit.
            self.health += heal_amount # Adds the healing amount to the characters current health.
        if self.health > self.max_health: # Makes sure that the characters health does not exceed max health.
            self.health = self.max_health
            print(f"{self.name} heals for {heal_amount}!")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25) # Boost health and attack power

    def power_attack(self, opponent):
        damage = self.attack_power * 1.5 # Damage dealt by a power attack is 1.5 times the attackers attack_power.
        opponent.health -= damage # Subtracts the calculated damage from their current health.
        print(f"{self.name} performs a Power Attack on {opponent.name} for {damage} damage!")
        if opponent.health <= 0: # Checks to see if the opponents health has dropped to 0 or below. 
            print(f"{opponent.name} has been defeated!") # Displays message if health has dropped to 0 or below for the opponent.

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35) # Boost attack power

    def cast_spell(self, opponent):
        spell_damage = self.attack_power * 2 # Damage inflicted by a spell is 2 times the casters attack_pwoer.
        opponent.health -= spell_damage # Subtracts the calculated damage from the spell from the opponents health.
        print(f"{self.name} casts a powerful spell on {opponent.name} for {spell_damage} damage!")
        if opponent.health <= 0: # Checks to see if the opponents health has dropped to 0 or below.
            print(f"{opponent.name} has been defeated!")


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15) # Lower attack power
# Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5 # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Added Archer Character
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30) # Calls the constructor of the parent class to initialize shared attributes.

    def precision_shot(self, opponent): # A unique method specific to the Archer class
        damage = self.attack_power * 1.7 # Damage is calculated at 1.7 times the Archer's attack_power. This attack it stronger than a normal one.
        opponent.health -= damage
        print(f"{self.name} performs a Precision Shot on {opponent.name} for {damage} damage! ")
        if opponent.health <= 0: # Checks to see if the opponents health has dropped to 0 or below.
            print(f"{opponent.name} has been defeated!")

# Added Paladin Character
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)

    def divine_shield(self):
        print(f"{self.name} casts Divine Shield, becoming immune to damage for one turn!")
        self.immune = True # Sets an immune attribute to True, representing invulnerability. 

    def attack(self, opponent):
        if hasattr(opponent, 'immune') and opponent.immune:
            print(f"{opponent.name} is immune to damage!")
            opponent.immune = False # Reset immunity after one turn
            return
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

# Function to create player character based on user input
def create_character(): # Displays a menu of character classes for theuser to choose from.
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin") 
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
        pass
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0: # While loop, continues as long as the wizard and the player have health greateer than 0.
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        choice = input("Choose an action: ")

# Special abilities
        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                player.power_attack(wizard)
            elif isinstance(player, Mage):
                player.cast_spell(wizard)
            elif isinstance(player, Archer):
                player.precision_shot(wizard)
            elif isinstance(player, Paladin):
                player.divine_shield()
            else:
                print("No special ability available!")
    
        elif choice == '3':
                player.heal()
        elif choice == '4':
            print(f"{player.name}: Health = {player.health}/{player.max_health}, Attack Power = {player.attack_power}")
        else:
            print("Invalid choice, try again.")
        continue

    if wizard.health > 0: # Displays "wizard's turn" as long as the wizard's health is greater than 0
        print("\n--- Wizard's Turn ---")
    wizard.attack(player)

    if player.health <= 0:
        print("You have been defeated!")
    elif wizard.health <= 0: # Checks to see if the opponents health has dropped to 0 or below.
        print("The wizard has been defeated!")

    if wizard.health <= 0: # Checks to see if the opponents health has dropped to 0 or below.
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
# Character creation phase
    player = create_character()

# Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

# Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()