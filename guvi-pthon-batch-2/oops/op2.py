class Company():
    companyName="GUVI"
    def __init__(self,empid,empName,empRole,empSalary):
        self.empid=empid
        self.empName=empName
        self.empRole=empRole
        self.empSalary=empSalary
        print("I have set the values")

    def employeeDetails(self):
        print(f"\nEmployee Id is {self.empid}\nEmployee Name is {self.empName}\nEmployee Role {self.empRole}\nEmployee Salary is {self.empSalary}\nEmployee Company is {self.companyName}")

emp1=Company(1001,"Rahul","Full Stack Developer",150000)
emp2=Company(1002,"Anees","MERN Stack Developer",50000)


emp1.employeeDetails()
emp2.employeeDetails()

'''
We are creating the emp1 object for the class Company
A class Company has a constructor which is expecting 4 arguements
So pass the 4 arguement data to the class Company
Whenever we create the object for this there is a default constructor will ge called i.e init() that is constructor
Constructor is going to set the values of an specific object data members '''