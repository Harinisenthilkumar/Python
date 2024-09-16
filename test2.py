#1 Python program to print list elements in different ways

'''list1=['edex',1,4,5]
list2=['tech',3,4,5]
print(list1)
print(list1[0])
print(list1[2:5])
print(list1[1:5])
print(list2+list2)
print(list1+list2)'''

#2. Program for Adding, removing elements in the list

'''list1=[10,20,30,'New Delhi', 'Mumbai']
print(list1)

list1.extend({40,50,'chennai'})
print(list1)

list1.pop()
print(list1)
list1.pop(6)
print("-------------------------------------------------")'''

#3. Program to print a list using 'FOR and IN' loop and sum the given elements in the list 
#without using sum().

'''list=[10,20,30,40,50]
sum=0
print("list elements are:")
for i in list:
    print(i)
    sum+=i
print("sum is:",sum)    
print("-------------------------------------------------")'''

#4. Program to remove first occurrence of a given element in the list.

'''list1 = [10, 20, 30, 40, 30]
print("Original list:", list1)
if 30 in list1:
    list1.remove(30)
print("List after removing 30:", list1)
if 10 in list1:
    list1.remove(10)
print("List after removing 10:", list1)'''


#5
'''list1=[10,20,10,30,10,40,10,50]
num=int(input(" Enter the value:"))
for i in list1:
    if i==num:
        list1.remove(num)
print("list after removing:",list1)
print("-------------------------------------------------")'''



#6 
'''list1=[10,20,30,40,50]
print("orginal list",list1)
list1.pop(1)
list1.pop(1)
print("update the list after deleting the element",list1)
print("-------------------------------------------------")'''



#7 Program to Print the index of first matched element of a list

'''list1 = [10, 20, 10, 20, 30, 40, 50]
name = int(input("Enter the element to find: "))

if name in list1:
    index = list1.index(name)
    print("Index of first matched", name, "is:", index)
else:
    print("Element not found in the list.")
print("-------------------------------------------------")'''

#8.Program to input, append and print the list elements
'''num = int(input("Enter the limit: "))
list1 = []  # Initialized the list
for i in range(1, num + 1):
    n = int(input("Enter an integer: "))
    list1.append(n)
print(list1)
print("-------------------------------------------------")'''

#9.program to remove the duplicate element from the list without using set

'''
`list1 = [10, 20, 10, 20, 30, 40, 30, 50]
list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)
print("-------------------------------------------------")'''


#10.Program to Create two lists with EVEN numbers and ODD numbers from a list
'''List1 = [11, 22, 33, 44, 55]
evennumbers = []
oddnumbers = []
for number in List1:
    if number % 2 == 0:
        evennumbers.append(number)
    else:
        if number % 2 != 0:
            oddnumbers.append(number)
print("List with EVEN numbers:", evennumbers)
print("List with ODD numbers:", oddnumbers)'''
 
#11. Program to print all numbers which are divisible by M and N in the List
'''List = [10, 15, 20, 25, 30]
M = 3
N = 5
for number in List:
    if number % M == 0 and number % N == 0:
        print(number)'''
#12.Create three lists of numbers, their squares and cube
'''Start = 1
End = 10
numbers = []
squares = []
cubes = []
for number in range(Start, End + 1):
    numbers.append(number)       
    squares.append(number ** 2) 
    cubes.append(number ** 3)
print("numbers:", numbers)
print("squares:", squares)
print("cubes  :", cubes)'''


#14.Create two lists with first half and second half elements of a list
'''inputlist = [10, 20, 30, 40, 50, 60]
list1 = inputlist[:3]
list2 = inputlist[3:]
print("list1:", list1)
print("list2:", list2)'''

#15.Print list after removing EVEN numbers.

'''list = [11, 22, 33, 44, 55]
oddnumbers = []
for number in list:
    if number % 2 != 0:
        oddnumbers.append(number)
print("list after removing EVEN numbers")
print("list =", oddnumbers)'''


#16. Convert a string to integers list



#17. Check all elements of a list are the same or not in Python




#18.POSITIVE AND NEGATIVE NUMBER
list1 = [4, -1, 5, 9, -6, 2, 9, 8]
positive = []
negative = []

for i in list1:
    if i < 0:
        negative.append(i)
    else:
        positive.append(i)

print("Positive numbers:", positive)
print("Negative numbers:", negative)

#19.Python program to multiply all numbers of a list
'''numbers = [4, 1, 6, 3, 9]
result = 1
for num in numbers:
    result *= num
print(result)'''

#20.How to find the length of a list in Python without using len().
'''list = [3, 6, 9, 8, 1,]
count = 0
for i in list:
  if i:  
    count += 1
if count:
  print(count)
else:
  print("The list is empty.")'''

#21. Python program to check if an element is present in list
'''list = [4, 2, 9, 5, 1, 0, 7]
elem = 5
if elem in list:
    print("Present")
else:
    print("Not Present")'''

#22.
'''list1 = [[2, 3, 4], [3, 2, 4], [5, 8]]
outputlist = []
for list in list1:
    outputlist += list
print(outputlist)'''



