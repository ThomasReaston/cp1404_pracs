import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
print("")

#line 1
print(random.randint(5, 20))
print(random.randint(5, 20))
print(random.randint(5, 20))

#What did you see on line 1?
#It printeed a random interger between 5 and 20

#What was the smallest number you could have seen, what was the largest?
#5 Is the smallest and 19 is the largest
print("")

#line 2
print(random.randrange(3, 10, 2))
print(random.randrange(3, 10, 2))
print(random.randrange(3, 10, 2))

#What did you see on line 2?
#A number between 3 and 10 in jumps of 2

#What was the smallest number you could have seen, what was the largest?
#The smallest is 3 and the biggest is 9

#Could line 2 have produced a 4?
#It can not because that is only 1 spot away from 3 not 2
print("")

#line 3
print(random.uniform(2.5, 5.5))
print(random.uniform(2.5, 5.5))
print(random.uniform(2.5, 5.5))

#What did you see on line 3?
#A random float between 2.5 and 5.49999

#What was the smallest number you could have seen, what was the largest?
#Smallest is 2.5, largest is <5.5

#To do - Write code to produce a random number between 1 and 100 inclusive.

print(random.randint(1, 101))


