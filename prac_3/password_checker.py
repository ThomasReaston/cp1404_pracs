
def main():

    password = str(input("Please enter your password:- "))

    print(password)

    if len(password) < 4:
        print("Your password is too short - Must be more than 4 characters")
        password = str(input("Please enter your password:- "))

    else:
        return password
main()





