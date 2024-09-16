#ABSTRACTION
'''class stu():
    def name(self):
        pass
    def course(self):
        pass

class s1(stu):
    def name(self):
        print("harini")
    def course(self):
        print("python")

student = s1()
student.name() 
student.course()'''

#STEP1-IMPORT
#STEP2-INHERIT
#STEP3-DECEROATION

from abc import ABC,abstractmethod #IMPORTING FROM ABC
class product(ABC):
    @abstractmethod #DECORATE METHOOD 
    def product_type(self):
        pass
    @abstractmethod
    def price(self):
        pass

class mobile(product): #INHERIT THE CLASS PRODUCT
    def product_type(self):
        print("product type : mobile")

    def brand_name(self):
        print("Brand name : Redmi")

    def price (self):
        print("price: ",2000)

o1=mobile()
o1.product_type()
o1.brand_name()
o1.price()

o1=mobile()
o1.product_type()
o1.brand_name()
o1.price()
