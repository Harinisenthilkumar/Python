# Function to calculate ticket price based on age
def calculate_ticket_price(age):
    if age < 12:
        return 5.00
    elif 12 <= age <= 64:
        return 10.00
    else:
        return 5.00
age = int(input("Enter your age: "))
ticket_price = calculate_ticket_price(age)
print(f"Your's Ticket Price is : {ticket_price:.2f}/-")
