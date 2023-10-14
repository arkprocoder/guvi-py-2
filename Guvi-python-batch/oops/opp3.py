# single level inhertance

class Parent:
    familyName="chettys"

    def property(self):
        print("parents property")

    def business(self):
        print("parents business")

class Child(Parent):

    childname="chandan"

    def childproperty(self):
        print("child property")

    def childbusiness(self):
        print("child business")


obj=Child()
obj.business()
obj.childbusiness()
obj.property()
obj.childproperty()


obj2=Parent()
obj2.business()
obj2.property()