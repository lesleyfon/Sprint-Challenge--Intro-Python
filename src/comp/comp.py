# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")

a = [human.name for human in humans if human.name[0] == "D"]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [human.name for human in humans if human.name[-1] == "e"]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
string_range = ['C', 'D', 'E', 'F', 'G']
c = [human.name for human in humans if human.name[0] in string_range]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")

d = [person.age + 10 for person in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f'{person.name}-{person.age}' for person in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(person.name, person.age)
     for person in humans if person.age >= 27 and person.age <= 32]
print(f)


# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
'''
    Thought Process:
        Step one:
            Iterate through the length of the humans List
        step two:
            Create an index for every Human created in the Human List.
        step Three:
            Instantiate a new Human by calling the Human class
        Step Four:
            get the name and age of a human from the list at a specific index and pass it to the new Human class instance
        step Five:
            User the 'upper' Method to capitalize the Names
'''
g = [Human(humans[index].name.upper(), humans[index].age + 5)
     for index in range(len(humans))]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = [math.sqrt(person.age) for person in humans]

print(h)
