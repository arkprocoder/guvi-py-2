class Employee():
    company="Infosys"
    # constructor
    def __init__(self,empid,efirstName,elastName,erole,esalary,equalification):
        self.empid=empid
        self.efirstName=efirstName
        self.elastName=elastName
        self.erole=erole
        self.esalary=esalary
        self.equalification=equalification
        print("i have set the values")

    def employeeDetails(self):
        print(f"\nCompany name is {self.company}\nEmployee Id is {self.empid}\nEmployee name is {self.efirstName} {self.elastName}\nEmployee role is {self.erole}\nEmployee salary is {self.esalary}\nEmployee Qualification is {self.equalification}")

    @staticmethod
    def publicHolidays():
        print("15th August is Holiday")

empl1=Employee(1001,"Sayara","banu","programmer",50000,"btech")
empl2=Employee(1002,"Sandhya","S","developer",60000,"btech")
empl1.employeeDetails()
empl1.publicHolidays()
empl2.employeeDetails()
empl2.publicHolidays()


'''
We are creating the empl1 object for the class Employee
A class employee has a constructor which is expecting 6 arguements
So pass the 6 arguement data to the class employee
Whenever we create the object for this there is a default constructor will ge called i.e init() that is constructor
Constructor is going to set the values of an specific object data members '''