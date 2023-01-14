import math
import time
import pyfiglet
t=pyfiglet.figlet_format ("Equvalent to third grade",font="slant")
print(t)
time.sleep(2)
def equvalent_to_third_grade(a,b,c):
    p=b-a**2//3
    q=(2*a**3/27)-(a*b/3)+c
    v=q**2/2+p**3/27
    if v>0:
        x=(-q/2+math.sqrt(v))**(1/3)+(-q//2-math.sqrt(v))**(1/3)-a/3
        print(x)
    elif v==0:
        x1=-2*(q/2)**(1/3)-a/3
        x2=(q/2)**(1/3)-a/3
        x3=x2
        print(x1**2,x2**2,x3**2)
    elif v<0:

        x1=2//math.sqrt(3)*math.sqrt(-(p))*math.sin(1//3*math.sin(3*math.sqrt(3)//2*(math.sqrt(-p)**3))**-1)-a/3
        x2=-2/math.sqrt(3)*math.sqrt(-p)*(1/3*math.sin((3*math.sqrt(3)*p)/(2*math.sqrt(-p)**3))+math.pi/3)**-1-a/3
        x3=2/math.sqrt(3)*math.sqrt(-p)*math.cos(1/3*math.sin(3*math.sqrt(3)*q/2*(math.sqrt(-p))**3)**-1)
        print(x1)
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
equvalent_to_third_grade(a,b,c)