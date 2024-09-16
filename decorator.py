'''def box(func):
    def paper ():
        print("cover")
        func()
        print("cover")
    return paper

@box
def chicken():
    print("grill chicken")

def icecream():
    print("ice cream")

@box
def friedrice():
    print("fried rice")


chicken()
icecream()
friedrice()
'''


#property
'''class edex():
    name="python"

    @property
    def display1(self):
        print("display1")

        def display1(self):
            print("display1")


o1=edex()
o1.display1

'''
#static
class edex():
    name="python"

    @staticmethod
    def display2():
        print("display2")


o1=edex()
o1.display2()
