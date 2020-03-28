numbers = []

for i in range (5):
    number = int(input("Please enter a number:- "))
    numbers.append(number)

print("Your first number is:-",numbers[0])
print("Your second number is:-",numbers[1])
print("Your third number is:-",numbers[2])
print("Your forth number is:-",numbers[3])
print("Your fifth number is:-",numbers[4])

print("The first number you entered was:- ", numbers[0])
print("The last number you entered was:- ", numbers[-1])
print("The smallest number you entered was:- ", min(numbers))
print("The largest number you entered was:- ", max(numbers))
print("The average of the numbers you entered is:- ", sum(numbers)/len(numbers))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username_entered = str(input("Please enter your username:- "))

if username_entered in usernames:
    print("Access Granted")

else:
    print("Access Denied")