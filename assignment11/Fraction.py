class Fraction():
    def __init__(self,s,m):
        self.s=s
        self.m=m
        # methods
    def simplify(self):
        while True:
            if self.s % 2==0 and self.m % 2==0:
                self.s//=2
                self.m//=2
            elif self.s % 3==0 and self.m % 3==0 :
                self.s//=3
                self.m//=3
            elif self.s % 5==0 and self.m % 5==0:
                self.s//=3
                self.m//=3
            elif self.s % 11==0 and self.m % 11==0:
                self.s//=11
                self.m//=11
            elif self.s % 13==0 and self.m % 13==0:
                self.s//=13
                self.m//=13
            elif self.s % 17==0 and self.m % 17==0:
                self.s//=17
                self.m//=17
            elif self.s % 19==0 and self.m % 19==0:
                self.s//=19
                self.m//=19
            else:
                break
        return self
    def show(self):
        if self.m==0:
            print("it's not fraction")
        else:
            print(self.s,"/",self.m)
    def add(self,frac2):
        m=self.m*frac2.m
        s1=self.m*frac2.s
        s2=frac2.m*self.s
        s=s1+s2
        return Fraction(s,m)
    def multiply(self,frac2):
        s=self.s*frac2.s
        m=self.m*frac2.m
        return Fraction(s,m)
    def subtract(self,frac2):
        m=self.m*frac2.m
        s1=self.m*frac2.s
        s2=frac2.m*self.s
        s=s1-s2
        return Fraction(s,m)
    def divide(self,frac2):
        m=self.m*frac2.s
        s=self.s*frac2.m
        return Fraction(s,m)
    def fraction_to_number(self):
        number=self.s/self.m
        return number
    @staticmethod
    def number_to_fraction(number):
        return Fraction(number,1)


f1=Fraction(8,8)
f1.show()
f1.simplify()
f1.show()
f1=f1.add(Fraction(2,6))
f1.simplify()
f1.show()
f1=f1.divide(Fraction(3,1))
f1.show()
print(f1.fraction_to_number())
t2=Fraction.number_to_fraction(30)
t2.show()
f1=f1.multiply(Fraction(2,0))
f1.show()
