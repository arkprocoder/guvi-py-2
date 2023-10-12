class Human():
    # data members of the class
    name="human_name"
    age="human_age"
    gender="human_gender"

    # create the methods
    def speak(self):
        print(f"{self.name} Speaks")

    def eat(self):
        print(f"{self.name} Eats")

    def sleep(self):
        print(f"{self.name} Sleeps")

    def code(self):
        print(f"{self.name} Code")

p1=Human()
p1.name="Anees"  #setting the data members values
p1.age=25
p1.gender="Male"
print("\n")
p1.speak()  #calling the methods of the class Human
p1.eat()
p1.sleep()
p1.code()


p2=Human()
p2.name="Rohan"
p2.age=26
p2.gender="Male"
print("\n")
print(p2.name)
print(p2.age)
print(p2.gender)
p2.speak()
p2.sleep()
p2.eat()
p2.code()