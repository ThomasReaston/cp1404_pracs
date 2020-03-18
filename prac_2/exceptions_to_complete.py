"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""


try:
    user_input = int(input("Enter a number:- "))
    print("Thanks for entering you number. ",user_input," is a great number")

except ValueError:
          print("Please enter a valid integer.")

print("Valid result is:", user_input)