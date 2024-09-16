#indexing,slicing 
'''tup=(1,2,3,4,5)
print(tup)
print(tup[2])#indexing
print(tup[2:])#slicing

#DUPLICATE VALUE
tup=(1,2,3,4,5,2,3)
print(tup)'''

#MUTABLE
#CHANGHE ,ADD,REMOVE ,EXTEND , --->CANT DO
#CONCAT-->WORKS

#UNPACKING
print("Unpacking")
tup=(1,2,3,4)
a,b,c,d = tup
print(a)
print(b)
print(c)
print(d)
#UNPACKING WITH STAR
print("unpacking with star")
tup=(1,2,3,4,6,7,8)
a,b,c,*d = tup
print(a)
print(b)
print(c)
print(d)
print()
#PACKING
print("Finding the data type")
a=(1)
b=("hello")
c=(1.89)
d=("apple","orange") #more then one value so its tuple
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print()

#PACKING
print("Packing")
empty_pocket =(1,2,3,"apple")
print(empty_pocket)
print()

print("converting tuple to list to do add,remove" )  
tup=(1,2,3,4,5)
change=list(tup)
change.remove(3)
change.append("apple")
new=tuple(change)
print(new)
print()













