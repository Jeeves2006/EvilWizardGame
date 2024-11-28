RPG Battle Game
A simple text-based RPG game where the player creates a character and battles an Evil Wizard. Choose from four classes (Warrior, Mage, Archer, Paladin), each with their own unique abilities, 
and see if you can defeat the wizard in a turn-based battle.

Features
Character Creation: Choose from 4 classes: Warrior, Mage, Archer, or Paladin.
Turn-Based Combat: Fight against the Evil Wizard in a series of turns, using attacks, special abilities, and healing.
Special Abilities: Each class has a unique special ability, such as the Warrior's Power Attack, the Mage's Spellcasting, and the Paladin's Divine Shield.
Healing System: Heal yourself during battle to maintain your health.
Battle Stats: View your health and attack power at any time during the battle.
Classes
Warrior: High health and strong attack. Can use Power Attack to deal 1.5x damage.
Mage: High attack power but lower health. Can cast a spell for 2x damage.
Archer: Balanced health and attack. Can perform a Precision Shot that deals 1.7x damage.
Paladin: High health and moderate attack. Can use Divine Shield to become immune to damage for one turn.
How to Play
Character Creation: When the game starts, you'll be prompted to choose a character class (Warrior, Mage, Archer, or Paladin) and enter a name for your character.
Battle: You will face the Evil Wizard in a turn-based battle. On your turn, you can:
Attack: Perform a regular attack.
Use Special Ability: Use your class’s special ability (e.g., Power Attack, Cast Spell, etc.).
Heal: Heal for 20 health points (up to your maximum health).
View Stats: Check your current health and attack power.
Evil Wizard: The Evil Wizard will attack after each of your turns. It can regenerate health each round to make the fight more challenging.
Victory or Defeat: The battle ends when either the Evil Wizard or your character’s health reaches 0. If the wizard is defeated, you win!
Installation
To run this game, you only need Python installed on your machine.

Download or clone this repository.

Open a terminal and navigate to the directory where the game files are located.

Run the game with the following command:

Copy code
python rpg_battle_game.py
The game will start in your terminal or command prompt.

Code Structure
Character Class: Base class with common attributes like health, attack_power, and methods for attacking, healing, and displaying stats.
Warrior, Mage, Archer, Paladin Classes: Subclasses that inherit from Character and add unique abilities (e.g., Power Attack, Cast Spell, etc.).
EvilWizard Class: Represents the enemy in the game with special regeneration abilities.
Battle System: The main game loop runs in the battle() function, allowing you to take turns with the wizard until either you or the wizard loses all health.
Example of Gameplay
bash
Copy code
Choose your character class:
1. Warrior
2. Mage
3. Archer
4. Paladin
Enter the number of your class choice: 1
Enter your character's name: Aragorn

--- Your Turn ---
1. Attack
2. Use Special Ability
3. Heal
4. View Stats
Choose an action: 1
Aragorn attacks The Dark Wizard for 25 damage!
The Dark Wizard attacks Aragorn for 15 damage!

--- Your Turn ---
1. Attack
2. Use Special Ability
3. Heal
4. View Stats
Choose an action: 3
Aragorn heals for 20!
The Dark Wizard attacks Aragorn for 15 damage!

...
