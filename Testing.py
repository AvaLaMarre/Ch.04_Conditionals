a=4
b=3
c=6
if a < b and a < c:
    print("a is the smallest")
elif b < a and b < c:
    print("b is the smallest")
else:
    print("c is the smallest")

name="Marc"
if name == "Marc" or name=="Jerry" or name=="Truman":
    print("yes these people are geniuses")

A=True
if not A:
    print("A wasn't True")
else:
    print("A wasn't False ")
x= input("Tell me your name")
if x.lower()=="marc":
    print("Hello", x)