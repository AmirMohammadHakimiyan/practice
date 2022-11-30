import math
print("wellcome to my calcuiator")
one=int(input("عدد رو وارد کن"))
amaliat=input("عملیات مورد نظر")
if amaliat=="sin":
    b=(one/180)*math.pi
    print(math.sin(b))
elif amaliat=="cos":
    a=one/180*math.pi
    print(math.cos(a))
elif amaliat=="tan":
    c=one/180*math.pi
    print(math.tan(c))
elif amaliat=="cot":
    d=one/180*math.pi
    print(1/math.tan(d))
else :
    twe=int(input("عدد دوم دو وارد کن"))
    if amaliat=="+":
        print(one+twe)
    elif amaliat=="-":
        print(one_twe)
    elif amaliat=="*":
        print(one**twe)
    elif amaliat=="/":
        print(one/twe)
    else amaliat=="**":
        print(one**twe)
