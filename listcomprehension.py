print("i need you to enter five numbers")
a=int(input("enter number one: "))
b=int(input("enter number two: "))
c=int(input("enter number three: "))
d=int(input("enter number four: "))
e=int(input("enter number five: "))
list=[a, b, c, d, e]


odd=[x for x in list if x%2==1]
print("the numbers that are odd are: ", odd)