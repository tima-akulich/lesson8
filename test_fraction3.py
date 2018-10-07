from fraction_homework import Fraction

try:
    x= Fraction(1.1,2.2)
    print("Fail")
except:
    print("Pass")

x=Fraction(99,100)
y=Fraction(95,100)
answer=Fraction(4,100)
z = x-y
if (z==answer):
    print("Pass")
else:
    print("Fail")

if(str(z)=="4/100"):
    print("Pass")
else:
    print("Fail")

answer=Fraction(194,100)
z=x+y
if(z==answer):
    print("Pass")
else:
    print("Fail")

x= Fraction(1,2)
y= Fraction(2,3)

answer=Fraction(2,6)
z=x*y
if(z==answer):
    print("Pass")
else:
    print("Fail")


x=Fraction(3,2)
y=Fraction(4,5)

answer = Fraction (15,8)
z=x/y
if(z==answer):
    print("Pass")
else:
    print("Fail")