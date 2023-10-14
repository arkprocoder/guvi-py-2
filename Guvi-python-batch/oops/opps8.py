class Human:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")

    def perform_activity(self):
        pass

class Teacher(Human):
    def perform_activity(self):
        print(f"{self.name} is teaching.")

class Student(Human):
    def perform_activity(self):
        print(f"{self.name} is learning.")

# Create instances of different humans
john = Teacher("John")
alice = Student("Alice")

# Polymorphism in action
people = [john, alice]

for person in people:
    person.introduce()
    person.perform_activity()
