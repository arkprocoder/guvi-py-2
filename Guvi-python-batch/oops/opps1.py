class Human():
    #data members
    name="human_name"
    age="human_age"
    gender="human_gender"

    #methods
    def sleep(self):
        print(f"{self.name} Sleeps")

    def talks(self):
        print(f"{self.name} Talks")

    def blink(self):
        print(f"{self.name} eyes blinks")

# object 1 as apsara
apsara=Human()
print(type(apsara))
apsara.name="Apsara"
apsara.age=22
apsara.gender="female"
print(apsara.name)
print(apsara.age)
print(apsara.gender)
apsara.talks()
apsara.sleep()
apsara.blink()

#object2
print("\n")
obj2=Human()
obj2.name="Apoorva"
obj2.age=20
obj2.gender="female"
print(obj2.name)
print(obj2.age)
print(obj2.gender)
obj2.talks()
obj2.sleep()
obj2.blink()
obj2.phonenumber=7854120369
print(obj2.phonenumber)