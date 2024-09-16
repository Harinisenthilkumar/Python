#ATTRIBUTES
#ACCES MODIFIER

class edex():
    name ="edex" #public
    _loc="madurai" #protected
    __year=2024 #private
    def display(self):
        print()
        print("INSIDE CLASS")
        print(self.name)
        print(self._loc)
        print(self.__year)
#-----------------------------SUB CLASS------------------------------------------------
    
class tech(edex):
    def display2(self):
        print()
        print("SUB CLASS")
        print(self.name)#public
        print(self._loc)#protrcted
#-----------------------------OUTSIDE CLASS------------------------------------------------
o1=tech()
print()
print("OUTSIDE CLASS")
print(o1.name)#public
print(o1._loc)#protected
o1.display()
o1.display2()
print("---------------------------------------------------------------------------")

#METHOODS
#ACESS MODIFIER
#if a method is private we need to store in another method
class edex():
    __year = 2024
    def method1(self):
        print("public method")
        
    def __method2(self):
        print("private method")
        
    def method3(self):
        print(self.__year)
        
    def method4(self):
        return self.__method2()
    
class tech(edex):
    def display(self):
        print("hii")

o1=edex()
o1.method3()
o1.method4()



        
    

        
    




        
    

        
    


        


        
    

        
    


        


        
    

        
    
