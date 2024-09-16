


'''def display():
    print("hello")
display()


#RETURN
def display1():
    return ("world")
print (display1())

#INTEGER IN RETURN()
def display2():
    return 23
print (display2())





#ARGUMENTS
#ARRGUMENT USING PRINT FUNCTION 

def display2(a,b):
    print(a+b)
display2(4,5)
#display2(4,5,6)---> dont pass the extra values


#ARRGUMENT USING RETURN FUNCTION 

def display2(a,b):
    return a+b
print (display2(4,5))

#TYPES:

#NO RETURN WITH ARGUMENTS:

print("NO RETURN WITH ARGUMENTS")

def add(a,b):
    print(a+b)
add(7,8)
print("--------------------------------------------------------")

#NO RETURN WITHOUT ARGUMENTS

print("NO RETURN WITHOUT ARGUMENTS")
def display():
    a=10
    b=20
    print (a+b)
display()
print("--------------------------------------------------------")

#RETURN WITH ARGUMENT:

print("RETURN WITH ARGUMENT")
def display2(a,b):
    return a+b
print (display2(4,5))
print("--------------------------------------------------------")

# RETURN WITHOUT ARGUMENTS

print("RETURN WITHOUT ARGUMENTS")

def display():
    a=10
    b=34
    return(a*b)
print (display())
print("--------------------------------------------------------")



#ARGUMENT BASED TYPES:
print("ARBITARY ARGUMENTS:")
def stu(*data):
    print(data)
stu("vijay",)
stu("vijay","madurai")
stu("vijay","madurai","MCA")


def add(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print(sum)
add(5)
add(5,10)
add(5,10,20)'''


#KEYWORD ARGUMENTS
'''print("KEYWORD ARGUMENTS")
def stu (name,loc):
    print("name: ",name)
    print("loc: ",loc)
stu(loc="madurai",name="vijay",)'''


#ARIBATARY KEYWORD ARGUMENTS
print("ARIBATARY KEYWORD ARGUMENTS:")
def employee(**data):
    print(data)
employee(name="vijay",)
employee(name="vijay",loc="madurai")
employee(name="vijay",loc="madurai",degree="MCA")

    



















