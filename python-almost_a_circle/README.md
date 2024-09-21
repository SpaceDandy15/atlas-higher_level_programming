Python - Almost a Circle
Overview
This project focuses on exploring advanced Python concepts, especially in object-oriented programming (OOP).
 It involves creating base classes and derived classes while applying key OOP principles like inheritance,
 encapsulation, and polymorphism. The project also emphasizes writing clean, maintainable
 code with unit testing and following PEP 8 style guidelines.

Key Concepts
Object-Oriented Programming (OOP) principles
Class inheritance and method overriding
Encapsulation (private attributes, getter/setter methods)
Static and class methods
*args and **kwargs
Serialization and deserialization using JSON
File handling (read/write operations)
Unit testing with the unittest module
Structure
Base class: The foundation class for managing IDs and JSON serialization.
Rectangle class: A class inheriting from Base, implementing rectangle-specific properties and behaviors,
including methods like area, display, and update.
Square class: Inherits from Rectangle, with added behavior and validation for square-specific attributes.
Testing
All methods and classes are tested using Python’s unittest module,
ensuring correctness and handling edge cases. Tests are organized in the tests/ directory.