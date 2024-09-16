#CONSTRUCTOR
'''class Edex():
    def __init__(self):
        print("I am Harini")

    def display(self):
        print("From dindigul")

harini = Edex()
harini.display()'''


#CONSTRUCTOR -1
'''class Edex:
    def __init__(self):
        print("I am Harini")



harini = Edex()
harini = Edex()
harini = Edex()

'''

#CONSTRUCTOR ARRRGUMRNT  PASSING
#TASK-1
'''
print("\t\t\t\t" " WELCOM")
print("-----------------------------------------------------------------------------------------------")
class Mobiles():
    def __init__(self, bname, mname,mram, price):
        self.brand_name = bname
        self.model_name = mname
        self.ram=mram
        self.price = price

    def display(self):
        print("Brand name: ", self.brand_name)
        print("Mobile name: ", self.model_name)
        print("Storage:",self.ram)
        print("Price: ", self.price)

redmi = Mobiles("Redmi", "Note 10 Pro","4GB", 20000)
redmi.display()
print("\t\t\t\t" " WELCOM")
print("-----------------------------------------------------------------------------------------------")

vivo = Mobiles("Vivo", "V15 Pro","6GB", 30000)
vivo.display()
print("\t\t\t\t" " WELCOM")
print("-----------------------------------------------------------------------------------------------")
iphone = Mobiles("Iphone", "15 Pro","8GB", 100000)
iphone.display()
print("\t\t\t\t" " WELCOM")
print("-----------------------------------------------------------------------------------------------")
poco = Mobiles("poco", "note15","6GB", 40000)
poco.display()
print("\t\t\t\t" " WELCOM")
print("-----------------------------------------------------------------------------------------------")
IQOO = Mobiles("IQOO", "note3","8GB", 50000)
IQOO.display()'''


#CONSTRUCTOR TASK-2

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print("\t\t\t\tWELCOME")
        print("---------------------------------------")
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient balance")
            return self.balance
    
    def display(self):
        print("Account no : ", self.account_number)
        print("Balance    : ", self.balance)
        print("---------------------------------------")

# Creating an instance of BankAccount
account = BankAccount("1234556678", 1000)

# Display initial balance
account.display()

# Asking (deposit or withdraw)
action = input("\nEnter action (Deposit/Withdraw): ").lower()

if action == "deposit":
    deposit_amount = float(input("Enter amount to deposit: "))
    account.deposit(deposit_amount)
    print("Deposit successful.")
    account.display()
    
elif action == "withdraw":
    withdraw_amount = float(input("Enter amount to withdraw: "))
    if withdraw_amount <= account.balance:
        account.withdraw(withdraw_amount)
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")
    account.display()
    





































    


        


        
