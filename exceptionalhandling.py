#ERROR HANDLING
#1-value error
#2-zer0 error

'''try:
    a = int(input("Enter a value: "))
    b = int(input("Enter a value: "))
    print(a / b)
except Exception :
    print("Something went wrong:", )

print("The end")

#TO MENTION WHAT KIND OF value ERROR PARTICULARY


try:
    a = int(input("Enter a value: "))
    b = int(input("Enter a value: "))
    print(a / b)
except Exception as e:
    print("Something went wrong:", e)

print("The end")
'''
#keywor using TRY,EXPECT,AS
'''try:
    a = "edex"
    b = int(input("Enter the value: "))
    print(a[b])
    
except ValueError as e:
    print("Value error:", e)

except IndexError as e:
    print("Index error:", e)
    
except TypeError as e:
    print("Type error:", e)

except Exception as e:
    print("Something went wrong:", e)

print("The end")'''

#keyword using ELSE,FINALLY
'''try:
    a = "edex"
    b = int(input("Enter the value: "))
    print(a[b])
except Exception as e:
    print("Something went wrong:", e)

else:
    print("elseblock")

finally: #error vanthalum varala nallum finally will work 
    print("the end")
    '''
#TO VIEW HOW MANY TYPES OF ERROR IN PYTHON 
'''print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))'''

class Treasure:
    def __init__(self): #initialize the instance
        self.goldcount = 0 #to count the total number of code 

    def box1(self):
        key1 = input("Key 1: ")
        try:
            key1 = int(key1)
            self.goldcount += 1
            print("Gold in Box 1!")
        except ValueError:
            print("Something went wrong, moving to Box 2.")
        self.box2()

    def box2(self):
        key2 = input("Key 2: ")
        try:
            key2 = int(key2)
            self.goldcount += 1
            print("Gold in Box 2!")
        except ValueError:
            print("Something went wrong, moving to Box 3.")
        self.box3()

    def box3(self):
        key3 = input("Key 3: ")
        try:
            key3 = int(key3)
            self.goldcount += 1
            print("Gold in Box 3!")
        except ValueError:
            print("Something went wrong")
        print(f"Total gold obtained by treasurer : {self.goldcount}")
#start methood :
        
    def start(self):
        self.box1() # this methood calls from starting box1



dora = Treasure()#instance of tresure class
dora.start()# initiate the treasure hunt

print("The End")

 



