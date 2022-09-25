import string
import random

letters = list(string.ascii_letters)
numbers = ['1', '2', '3' , '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#' , '$', '%', '&']

print("Welcome to the password generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers?\n"))
nr_symbols = int(input("How many symbols would you like to have?\n"))

password = ""

for _ in range(nr_letters):
  password += random.choice(letters)

for _ in range(nr_numbers):
  password += random.choice(numbers)

for _ in range(nr_symbols):
  password += random.choice(symbols)

password = ''.join(random.sample(password,len(password)))

print(f"\nGenerated password:\n{password}")