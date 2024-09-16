#Lambda function:- (keyword)


#Lambda:----(return statement):

#syntax:
   #lambda argument : expression

#eg:1
'''name=lambda a,b:a+b

print(name(5,5))

   #(OR)

def add(a,b):
    print(a+b)

add(5,5)


print("_")'''

#eg:2
'''name=lambda a : a**2

print(name(2))
print(name(4))
print(name(5))

#eg:3
name=lambda a : a**a

print(name(2))
print(name(4))
print(name(5))

print("_")'''


#Lambda Three type:-
  #(1).map
  #(2).filter  -------> One liners
  #(3).reduce


#(1).map:-->(func,iterable)

#fun ---> 1 Argu : exp
#if we need to print convert into list and print

'''list1 = [1,2,3,4,5]
mlist = map(lambda a:a+10,list1)
print(list(mlist))#--->list converting
print("------------------------------------------------------------")

#storing as a list while storing its self
list1 = [1,2,3,4,5]
mlist = list(map(lambda a:a+10,list1))#--->Storing as list
print(mlist)
print("-------------------------------------------------------------")
      '''

#(2).filter:-->(func,iterable)--->Only return true value
#fun---->1 Argu : condition

'''list1 =[1,2,3,4,5]
flist=filter(lambda a: a%2==0,list1)
print(list(flist))'''


#(3).Reduc:--->need to import the reduce fun
'''from functools import reduce 
list1=[1,2,3,4,5]
rlist =reduce(lambda a,b :a+b,list1)
print(rlist)'''


#ALL THREE LAMBDA FUNCTION :
from functools import reduce 
list1=[1,2,3,4,5,6,7,8,9,10]

mlist = map(lambda a:a**2,list1)
flist = filter(lambda a :a>=3,list1)
rlist = reduce(lambda a,b : a+b ,list1)
print(list(mlist))
print(list(flist))
print(rlist)






























