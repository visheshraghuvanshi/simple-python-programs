# My answer
import random
print("Welcome to PyPassword Generator!")
no_of_letters = int(input("How many letters would you like in your Password?"))
no_of_symbols = int(input("How many symbols would you like?"))
no_of_numbers = int(input("How many numbers would you like?"))
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!#$%&()*+"

#Password in Simple Order
password = ""
for i in range(no_of_letters):
    password += letters[random.randint(0,len(letters) - 1)]
for i in range(no_of_symbols):
    password += symbols[random.randint(0,len(symbols) - 1)]
for i in range(no_of_numbers):
    password += numbers[random.randint(0,len(numbers) - 1)]
print(f"Here is your Password: {password}")

#Password in Random 
password = list(password)
for i in range(len(password)):
    temp1 = random.randint(0,i)
    temp2 = password[i]
    password[i] = password[temp1]
    password[temp1] = temp2
password = ''.join(password)
print(f"Here is your Complex Password: {password}")