# write a program to find a person can vote or not
# 1. he can vote if age > 18
# 2. he can vote if age is < 80
# 3. if age is == 18 he can vote if he has voter id

age=int(input("Enter your age: \n"))

if(age>18 and age<80):
    print("you can vote")

elif (age==18):
    print("you can vote if you have the voter id")

elif (age>=80):
    print("you cannot vote because of government policy")

else:
    print("You cannot vote because your age is < 18")

