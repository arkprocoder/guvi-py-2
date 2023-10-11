def employeeDetails(**mydict):
    print(type(mydict))
    for key,value in mydict.items():
        print(key,value)
        print(type(key),type(value))


mydict={
    "employeeName":"Rohan",  #key:value
    "employeeSalary":15000.52,
    "isActive":True,
    "role":"Front end dev",
    "address":['bangalore','devenhalli'],
    "phoneNumber":9874563210,
    "hobbies":("dance","sing"),
    "skills":{"python","django"},  
}


employeeDetails(**mydict)