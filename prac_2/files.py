
file = open('name.txt','w')

user_name = str(input("Please enter your name:- "))

file.write(user_name)

file.close()


file = open('name.txt','r')

print("Your name is ",user_name)

file.close()





