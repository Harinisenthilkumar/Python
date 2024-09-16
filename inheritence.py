#INHERITENCE 

'''class father(): # parent class 
    house="fathers bike"

    def display1(self):
        print(self.house)


class son (father):#argument passed to child class to access parent
    bike="sons bike"

    def display2(self):
        print(self.bike)


o1=son() #obj created only for son(sub class)
print(o1.bike)
o1.display2()

print(o1.house)
o1.display1()'''

#TYPE OF INHERITENCE
#SINGLE INHERETENCE
'''class father(): # parent class 
    house="fathers bike"

    def display1(self):
        print(self.house)


class son (father):#argument passed to child class to access parent
    bike="sons bike"

    def display2(self):
        print(self.bike)


o1=son() #obj created only for son(sub class)
print(o1.bike)
o1.display2()

print(o1.house)
o1.display1()'''


#MULTI-LEVEL INHERETENCE

'''class A():
    def display1(self):
        print("A class")

class B(A):
    def display2(self):
        print("B class")


class C(B):
    def display3(self):
        print("C class")


o1=A()
o2=B()
o3=C()

o1.display1()
o2.display2()
o3.display3() ''' 

#MULTIPLE INHERITANCE
'''class A():
    def display1(self):
        print('A class')
class B():
    def display2(self):
        print('B class')
class C():
    def display3(self):
        print('C class')

class D(A,B,C):
    def display4(self):
        print('D class')

o1=D()
o1.display1()
o1.display2()
o1.display3()
o1.display4()'''

#HIERARiCHCAL INHERITANCE:
'''class A():
    def display1(self):
        print('A class')
class B(A):
    def display2(self):
        print('B class')
class C(B):
    def display3(self):
        print('C class')
class D(C):
    def display4(self):
        print('D class')

a = A()
b = B()
c = C()
d = D()
a.display1()  
b.display2()  
c.display3()  
d.display4()
'''

#MRO(:
'''class A():
    def display(self):
        print('A class')

class B(A):# hierichal inherit A
    def display(self):
        print('B class')

class C(A): # hierarichal inherit a
    def display(self):
        print('C class')

class D(B, C):#multiple inherit
    def display(self):
        print('D class')

a = A()
b = B()
c = C()
d = D()

a.display() 
b.display()  
c.display()  
d.display()'''
#   METHOOD RESOLUTION ORDER (MRO)

'''class A():
    def display(self):
        print('A class')

class B(A):
    def display(self):
        print('B class')

class C(B): 
    def display(self):
        print('C class')

class D(C,B,A):#
    def display(self):
        print('D class')

o1 = D()

o1.display() 
o1.display()  
o1.display()  
o1.display()'''










