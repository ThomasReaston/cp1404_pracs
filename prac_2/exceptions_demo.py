"""
CP1404/CP5632 - Practical
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    #Add the if statement so 0 can not be entered

    if denominator == 0:
        print("Input can not be 0")
        denominator = int(input("Enter the denominator: "))

    else:

        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#Answer the following questions:
#1. When will a ValueError occur?
#When the input for either is not an integer.

#2. When will a ZeroDivisionError occur?
#When a zero is put as the denomiatior as you can not dive by 0.

#3. Could you change the code to avoid the possibility of a ZeroDivisionError?
