import random

# user's choice
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

# Randomly  computer's choice
computer_choice = random.choice(['rock', 'paper', 'scissors'])

if user_choice == computer_choice:
    result = "It's a tie!"
elif user_choice == 'rock' and computer_choice == 'scissors':
    result = "You win!"
elif user_choice == 'paper' and computer_choice == 'rock':
    result = "You win!"
elif user_choice == 'scissors' and computer_choice == 'paper':
    result = "You win!"
else:
    result = "Computer wins!"


print("You chose: " + user_choice)
print("Computer choose: " + computer_choice)
print(result)
