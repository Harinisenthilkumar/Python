#OVER RIDING
'''class a():
    def display(self):
        print("A class")
class b(a):
    def display(self):
        print("B class")

o1=b()
o1.display()
print("_________________________________________________")

class A():
    def display1(self):
        print("A class")
    def hello(self):
        print("HELLO WORLD")
class B(A):
    def display(self):
        super().display1()
        print("B class")
        super().hello()
        
o1=B()
o1.display()
print("_________________________________________________")

class A():
    def display1(self):
        print("A class")
    def hello(self):
        print("HELLO WORLD")
class B(A):
    def display(self):
        super().display1()
        super().hello()
        print("B class")
        
o1=B()
o1.display()
print("_________________________________________________")


class A():
    def display(self):
        print("A class")
class B(A):
    def display(self):
        super().display()
        print("B class")
class C(B):
    def display(self):
        super().display()
        print("C class")
O1=C()
O1.display()
print("_________________________________________________")

class A():
    def __init__(self,name,loc):
        self.name=name
        self.loc=loc
        print("name:",self.name)
        print("loc:",self.loc)
class B(A):
    def __init__(self,salary):
        super().__init__("harini","dindigul")
        print("salary:",salary)
        print(self.name,self.loc,salary)
o1=B(30000)

'''
#METHOD OVERLOADING

'''class MOL():
    def add(self,*a):
        sum=0
        for i in a :
            sum=sum+i
        print(sum)
o1=MOL()
o1.add(5)
o1.add(5,10)
o1.add(5,10,10)'''
#OPERATOR OVERLOADING
class edex():
    def __init__ (self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a
    def __sub__(self,other):
        return self.a-other.a
    def __mul__(self,other):
        return self.a*other.a
    def __truediv__(self,other):
        return self.a/other.a
    

o1= edex(5)
o2=edex(10)


print(o1+o2)
print(o1-o2)
print(o1*o2)
print(o1/o2)
    








































