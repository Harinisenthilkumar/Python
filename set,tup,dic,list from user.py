#1.set,list,tuple

'''num= int(input("Enter the number of elements: "))
list1 = []
for i in range(num):
    value = int(input("Enter a value: "))
    list1.append(value)
    tup=tuple(list1)
    s1=set(list1)
print("List:", list1)
print("Tuple:", tup)
print("Set:", s1)'''


#2 dictionary
num = int(input("Enter the number of elements: "))
dict1 = {}
for i in range(num):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dict1.update({key: value})
print("Dictionary:", dict1)

