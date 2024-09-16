#Write # 1. Python program to calculate the factorial of a given number using a while loop.
'''num = int(input("Enter a value: "))
i = 1
fact = 1
while i <= num:
    fact=fact*i
    i += 1
print(fact)'''

#2. Write a Python program to reverse a given number using a while loop.
'''num = 123
rev = 0
while num > 0:
    server = num % 10
    rev = rev * 10 + server
    num = num // 10  # Use integer division
print(rev)'''

#3. Write a Python program to check if a given integer number is a palindrome using a while loop.
'''number = int(input("Enter an integer: "))
original= number
rev = 0
while number > 0:
    remainder = number % 10
    rev = rev* 10 + remainder
    number = number // 10
    
#rev=0 ---> 321
#num=123 --->0
#original=123
# if the original number and the reversed number are the same, and print the result
if original == rev:
    print("it is Palindrome")
else:
    print("it is not a Palindrome")'''


#4. Write a Python program to calculate the sum of digits of a given number using a while loop.
'''num=int(input("enter a value"))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)'''


#5.Write a program to check if a number is divisible by both 2 and 3.
'''number = int(input("Enter a number: "))
if number % 2 == 0 and number % 3 == 0:
    print("The number is divisible by both 2 and 3")
elif number % 2 == 0:
    print("The number is divisible by 2 but not by 3")
elif number % 3 == 0:
    print("The number is divisible by 3 but not by 2")
else:
    print("The number is not divisible by either 2 or 3")'''


#6.Write a program to count the number of vowels and consonants in a given string.


a = input("Enter a string: ").lower()
vowels= 'aeiou'
v, c = 0, 0
for i in a:
    if i in vowels:
        v += 1
    else:
        c += 1

print(f"The given string contains {v} vowels and {c} consonants")




#7 Write a program to replace a substring in a given string with another substring.

name1="Hello World"
print(name1)
print(name1.replace("World","Universe"))
print()
name2="Hello World"
print(name2)
print(name2.replace("Hello World","HelloWorld"))


#8.TRIANGLE IN NUMBERS
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print() 


#9. TRIANGLE
row=int(input("row:"))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    for j in range(1,i+1):
        print("* " ,end="")
    print()

#10 PYRAMID PATTERN

rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(' ', end=' ')
    for k in range(2 * i - 1):
        print('*', end=' ')
    print()


#11 INVERSE PYRAMID PATTERN
rows = int(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(' ', end=' ')
    for k in range(2 * i - 1):
        print('*', end=' ')
    print()

    








