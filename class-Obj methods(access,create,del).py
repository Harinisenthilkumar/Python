1#METHOD :
#1.CLASS INSTANCE
#2.OBJECT INSTANCE



#1.CLASS INSTANCE
'''class calculator():
    a=5
    b=5
    def add():
        print("hello")
    def sub():
        print("world")
print(calculator.a)
print(calculator.b)
calculator.add() #Class name and function kuduthu call panalam 
calculator.sub()'''


#IF CALL ADD/SUB METHOOD THE OPERATION NEED TO PERFORM

'''class calculator():
    a=5
    b=5
    def add():
        print(calculator.a+calculator.b) # INSTANCE NAME MUST
    def sub():
        print(calculator.a-calculator.b)
calculator.add()  
calculator.sub()'''


#ARRGUMENT PASSING
'''class calculator():
    a=5 #CLASS ATTRIBUTE
    b=5
    def add(name): #METHOD ATTRIBUTES 
        print(calculator.a+calculator.b) # INSTANCE NAME 
        print(name)
    def sub(name):
        print(calculator.a-calculator.b)
        print(name)
calculator.add("hello")  
calculator.sub("friend")'''

#2.OBJECT INSTANCE

'''class calculator():
    a=5
    b=5
    def add(self):#VELIYA IRUNTHA OBJ ULLA VANTHA SELF
        print("Hello") 
    def sub(self):
        print("world")
edex=calculator()  #CREATION OBJ instance
print(edex.a,edex.b)
edex.add()
edex.sub()'''
              
# IF CALL ADD/SUB METHOOD THE OPERATION NEED TO PERFORM
'''class calculator():
    a=5
    b=5
    def add(self):
        print(self.a+self.b) #self is the instance 
    def sub(self):
        print(self.a-self.b)
edex=calculator()  #CREATION OBJ instance
edex.add()
edex.sub() '''

#TASK-1 :
'''a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))

class Calculator:
    def values(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        print(self.a + self.b)
    
    def sub(self):
        print(self.a - self.b)
        
    def mul(self):
        print(self.a * self.b)
        
    def div(self):
        print(self.a / self.b)

calc = Calculator()
calc.values(a,b)
calc.add()
calc.sub()
calc.mul()
calc.div()'''


#TASK-2
class cal():
    def value(self,value1,value2):
        self.a=value1
        self.b=value2
    def add(self):
            print(self.a+self.b)
    def sub(self):
            print(self.a-self.b)
    def mul(self):
            print(self.a*self.b)
    def div(self):
        if self.b != 0:
            print(self.a // self.b)
        else:
            print("Error: Division by zero is not allowed")

x=int(input("Enter a number :"))
y=int(input("Enter a number :"))
z=input("select any one :")
calc=cal()
calc.value(x,y)
if (z=="add"):
    calc.add()
elif (z=="sub"):
    calc.sub()
elif (z=="mul"):
    calc.mul()
elif (z=="div"):
    calc.div()
else:
    print("Worng Input")










    










































    

































