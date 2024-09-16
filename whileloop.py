#WHILE LOOP
#ini condition inc/dec
'''n=1
while n<=5:
    print(n)
    n+=1'''

#DECREMENT
'''n=5
while n<=1:
    print(n)
    n-=1'''

#SUM OF N NUMBERS
'''num = int(input("enter a value:"))
i=1
sum=0
while i<=num:
    sum=sum+i
    i+=1
print(sum)'''


#FACTORIAL OF N NUMBER
'''num = int(input("Enter a value: "))
i = 1
fact = 1
while i <= num:
    fact=fact*i
    i += 1
print(fact)

num = int(input("Enter a value: "))'''

#  while loop to find even numbers
'''num = int(input("Enter a value: "))
i = 1
while i <= num:
    if i % 2 == 0:
        print("Even numbers are", i)
    i += 1
#  while loop to find odd numbers
i = 1
while i <= num:
    if i % 2 != 0:
        print("Odd numbers are", i)
    i += 1'''

# Reversing the Integer
'''num = 123
rev = 0
while num > 0:
    server = num % 10
    rev = rev * 10 + server
    num = num // 10  # Use integer division
print(rev)'''

#SUM OD DIGITS //   REVERSING PRG + SUM OF N PRG
'''num=int(input("enter a value"))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)'''

#SUM OF EVEN NUMBERS

'''num= int(input("enter a value:"))
sum=0
for i in range(1,num+1):
    if i%2==0:
        sum=sum+i
print(sum)'''

#SUM OF EVEN NUMBERS DISPLAY WITH OPERATORS

'''num= int(input("enter a value:"))
sum=0
for i in range(1,num+1):
    if i%2==0:
        print(i,end="+")
        sum=sum+i
print("\b=",sum)'''


#5.Write a program to check if a number is divisible by both 2 and 3.
# Step 1: Input the number from the user
number = int(input("Enter an integer: "))

# Step 2: Check if the number is divisible by both 2 and 3
if number % 2 == 0 and number % 3 == 0:
    print(f"{number} is divisible by both 2 and 3")
else:
    print(f"{number} is not divisible by both 2 and 3")

    

    





