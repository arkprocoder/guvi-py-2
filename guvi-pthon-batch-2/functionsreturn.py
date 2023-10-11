def interest(money):
    rate=10
    principleamount=money
    total=principleamount*rate/100
    # print(total)
    return total

p1=interest(1000)
p2=interest(2000)
p3=interest(3000)
p4=interest(5000)
print("P1 profit is",p1)
print("P2 profit is",p2)
print("P3 profit is",p3)
print("P4 profit is",p4)

print("Over all profit by p1,p2,p3,p4 is ",p1+p2+p3+p4)
