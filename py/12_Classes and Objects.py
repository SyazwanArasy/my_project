#basic class definition
class Person:
    #Class attribute (shared by all instances)
    species = "Homo sapiens"

    # Constructor Method
    def __init__(self, name, age):
        #Instance attributes (unique to each instance)
        self.name = name
        self.age = age

    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name}, and I'm {self.age} years old."

    # Method with parameters
    def celebrate_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! You are now {self.age}."

    # Create objects (instances)
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)

    # Accessing Attributes
    print(person1.name) # Alice
    print(person2.age) # 30

    # Calling Instance Methods
    print(person1.introduce()) # Hi, I'm Alice, and I'm 30 years old.
    print(person2.introduce()) # Hi, I'm Bob, and I'm 25 years old.
    print(person1.celebrate_birthday()) # Happy birthday Alice! You are now 31.
    print(person2.celebrate_birthday()) # Happy birthday Bob! You are now 26.

    # Class Attributes
    print(Person.species) # Homo sapiens
    print(person1.species) # Homo sapiens
    print(person2.species) # Homo sapiens