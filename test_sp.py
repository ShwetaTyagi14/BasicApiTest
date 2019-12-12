
x=int(input("Enter x value \n "))
y=int(input("Enter y value \n "))

def add(x,y=3):  #default valuy y:3
    return x+y
# def sub(x,y):
#     return x-y
def test_cal():
    assert add(x,4)==7;"Fail"  #run time valye y:4
    # assert sub(x,y)==0

test_cal()

#NOte - Y: its gonna prefernce run time value