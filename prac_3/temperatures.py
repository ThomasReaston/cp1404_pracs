"""Program to convert temperatires from C to F and vice versa"""


def celsius_to_fahrenheit(temperature_input):
    temperature_output = temperature_input * (9/5) + 32
    return temperature_output


def fahrenheit_to_celsius(temperature_input):
    temperature_output = (temperature_input - 32) * (5/9)
    return temperature_output


def main():

    user_choice = str(input("Temperature in C or F? (C/F)\n:- "))
    user_choice.upper()
    valid_choices = ["C", "F"]

    while user_choice not in valid_choices:
        print("Invalid choice - Please select C or F")
        user_choice = str(input("Temperature in C or F? (C/F)\n:- "))
        user_choice.upper()

    if user_choice == "C":
        temperature_input = float(input("Enter temperature in C:- "))
        temperature_output = celsius_to_fahrenheit(temperature_input)
        print("Temperature is {}F".format(temperature_output))

    elif user_choice == "F":
        temperature_input = float(input("Enter temperature in C:- "))
        temperature_output = fahrenheit_to_celsius(temperature_input)
        print("Temperature is {} degrees Celsius".format(temperature_output))


main()
