# args:arguements : *
def sorting(*args):
    for i in args:
        print(i)
        print(type(i))

values=([1,2,3,4],[5,6,7,8])

sorting(values)