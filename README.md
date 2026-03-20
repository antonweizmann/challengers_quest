This is a game implemented for our third assigment in the Concepts of Programming course in Year 1 of the Artificial Intelligence bachelor at Radboud University.

Core requirements are:

Prerequisites of the project
 to be met by each student individually 
Your project needs to tick all the boxes in Checklist 1, and at least 2 boxes of
Checklist 2.
Checklist 1:
□ Implement at least 3 classes in your application;
□ Implement at least 5 methods;
(in total; getters, setters, the str representation and overloaded operators do
not count for this prerequisite)
□ Implement at least 3 encapsulated attributes (with getters and/or setters);
(some attributes might only have a getter or a setter, depending on your appli-
cation)
□ Use (built-in) decorators (@property, @classmethod, @staticmethod, ...);
□ Among all the data attributes, implement at least one private, one protected
and one public (data) attribute;
(not every class needs to have the three access modifiers. Notice that methods
of your classes do not count for this prerequisite)
□ Implement str representation of your classes (__str__() method);
Checklist 2:
□ Use static/class methods and class attributes
1
□ Use at least 3 operator overloading of the following operators: +, -, *, /, >, <,
==, !=, >= and <=
□ Implement at least 1 derived class and at least 2 overridden methods (excluding
__str__ methods)

Core Game Idea:

This game consists ouf three main elements: the dungeons containing the game logic, the players containing different classes and weapons and the enemies represeenting a number of different npc to fight against.

Players and Enemies Stats:
	Health : int
	Max Health : int
	Stamina : int
	Max Stamina : int
	Weapon : Weapon Class

Dungeon Attributs:
	Enemy number: int
	Enemies : list of Enemy class
	Player: Player class



Game Logic:
Game Class - responsible for handling main game loop
	tasks include starting game environment, holding player, loading dungeon floors, output logging, death handling

	Attributes:
		dungeon: Dungeon Class
		log_file: fd

	Methods:
		__init__: setup game environment,  open log_file in append.

		game_loop: handles main game loop

		game_start: welcome message to player, choose class, choose difficulty, initialize dungeon, start game_loop:

		game_exit: says taunting goodbye message, closes log_file


Dungeon class
	tasks include holding enemies, determining difficulty, spawning shops and rest pools

Shop class - holds 4 random items min 2 weapons
	tasks include handeling buying items

Inherited Dungeon Classes (Easy and Hard)



Ideas to add ?
Crafting - Lootdrops


This project was done by Taj Jursa, Luuc Koojiman and Anton Weizmann
