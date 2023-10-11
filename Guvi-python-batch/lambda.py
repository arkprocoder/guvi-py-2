# def minus(a,b):
#     return a-b

# res=minus(10,5)
# print(res)

minus=lambda x,y:x-y
add=lambda x,y,z:x+y+z
mul=lambda x,y:x*y
div=lambda x,y:x/y
flordiv=lambda x,y:x//y
modulo=lambda x,y:x%y
print("output minus",minus(25,5))
print("output add",add(25,5,10))
print("output mul",mul(25,5))
print("output div",div(25,5))
print("output floordiv",flordiv(25,5))
print("output modulo",modulo(25,5))