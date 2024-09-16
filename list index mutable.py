#indexing / slicing
'''list1 = ["apple","orange","mango",1,2,3]
print(list1[1])
print(list1[0:1])
print(list1[1:5])
print("--------------------------------------------------------------------------")

# REVERSING indexing / slicing
list1 = ["apple","orange","mango",1,2,3]
print(list1[1])
print(list1[0:-2])
print(list1[1::-1])
print("---------------------------------------------------------------------------")'''


#LIST MUTABLE (change,add,remove)
'''list1 = ["apple","orange","mango"]
#CHANGE
list1[1]='graphs'
print(list1)
print("---------------------------------------------------------------------------")
'''

#ADD--->append(),insert(),extend(),concatnation +
#append-->added the value in the list last
list1 = ["apple","orange","mango"]
list1.append("gooseberry")
print(list1)

#insert--> values can be indexed using index 
list1 = ["apple","orange","mango"]
list1.insert(1,"gooseberry")
print(list1)

#extend---> we can add more values
list1 = ["apple","orange","mango"]
list2=[1,2,3,4,5]
list1.extend(list2)
print(list1)

#concatination
list1 = ["apple","orange","mango"]
list2=[1,2,3,4,5]
list1=list1+list2
print(list1)
print("---------------------------------------------------------------------------")'''

'''#REMOVE(value)
list1 = ["apple","orange","mango"]
list1.remove("orange")
print(list1)
print("--------------------------------------------------------------------------")

#pop(normal+index value)
list1 = ["apple","orange","mango"]
'list1.pop()'
list1.pop(1)#index value use pani delete panalam 
print(list1)
print("--------------------------------------------------------------------------")

#clear(whole value in the variable is cleared )
list1 = ["apple","orange","mango"]
list1.clear
print(list1)
print("--------------------------------------------------------------------------")

#delete (whole variable is deleted )
list1 = ["apple","orange","mango"]
del list1
print(list1)
print("--------------------------------------------------------------------------")
'''

#COPY
orginal_vishal=["apple","orange","mango","graphs","edex"]
vishal1=orginal_vishal
vishal2=orginal_vishal.copy()
orginal_vishal.remove("edex")
print(vishal1)
print(vishal2)






























               


