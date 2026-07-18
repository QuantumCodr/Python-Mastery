# Program: While Loops - Repeat this code until I tell you to stop.
# Author: David
# Lesson: 11

count = 1
while count <= 5:
    print(count)
    count = count + 1

password = ""
while password != "python123":
    password = input("Enter password: ")
print("Access Granted")

number = 5
while number > 0:
    print(number)
    number -= 1
print("Blast Off!")

# EXcercise 1 - Count From 1 - 10
count = 1
while count <= 10:
    print(count)
    count += 1

# Excercise 2 - Countdown
timer = 10
while timer > 0:
    print(timer)
    timer -= 1
print("Lift Off")

# Excercise 3 - Password Checker
password = ""
while password != "python123":
    password = input("Enter password: ")
print("Access Granted")

# Excersise 4 - Number Sum
count = 1
sum_count = 0
number = int(input("Enter a number: "))
while count <= number:
    sum_count += count
    count += 1
print(f"Sum_Count: {sum_count} ")

# Challange 1 - Mulplication Table
count = 1
number = int(input("Enter number: "))
while count <= 10:
    print(f"{number} * {count} = {number * count}")
    count += 1

# Challange 2 - ATM
balance = 500
running = True

while running:
    withdrawal_amount = float(input("Withdraw amount (0 to exit): "))
    if withdrawal_amount < 0:
        print("Invalid Amount")
    elif withdrawal_amount == 0:
        print("Program Exited.")
        running = False
    elif withdrawal_amount <= balance:
        balance -= withdrawal_amount
        print("Withdrawal Successful")
        print(f"Balance: {balance}")
    else:
        print("Insufficient Funds")

# Challange 3 - Guess The Secret Number
secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input("Guess secret number: "))
    if guess != secret_number:
        print("Try Again")
print("Correct")

'''
Think like a programmer:
1. 1 2 3
2. 3 2 1 Done
3. 1 1 1 ...
4. 6
5. count keeps getting lower than 5
'''

# Mini Challange
password = ""
while password != "python123":
    password = input("Enter password: ")
    if password == "python123":
        print("Welcome to BaseAPI")
        logout = input("Do you want to logout (yes/no): ")

        while logout != "yes":
            logout = input("Do you want to logout (yes/no): ")
        print("Goodbye!")