#conditionals

# secret_number = 9
# guess = int(input("Guess a number from 1-10: "))

# #check if something is true or false/
# if guess > secret_number:
#     print("you guess is too high")
# elif guess < secret_number:
#     print("your guess is too low")
# else: 
#     print("YAAY! you guessed correctly!")

#####################Try it Yourself##################
#1 Weather Check: Build a program that:
#Write a program that asks the user if the forecast for the day is  rain, snow or sun. Store their answer in a variable called "weather".  
#Then start checking:
#If weather is rain then have your program print "Remember your umbrella!"
#If weather is snow then have your program print "Remember your wooly gloves!"
#Otherwise (else) have your program print "Remember your sunglasses!"

#2. Alien Color: Imagine an alien was just shot down in a game. Create a variable called alien_color and make it equal to  "green", "yellow" or "red" (your pick)
#Write a conditional to test the alien's color. 
#If the alien's color is green, print a message that the player just earned 5 points. 
#If the alien's color is red, your program should print a message that the player just earned 10 points
#If the color is yellow, the player should earn 15 points.

alien_color = "red"

if alien_color == "green":
    print("You just earned 5 points!")
elif alien_color == "red":
    print("You just earned 10 points!")
elif alien_color == "yellow":
    print("You earned 15 points!")
else:
    print("You earned 0 points :(")

#3: Build a program that asks the user for their age
#stores that age in a variable 
#prints out whether or not they are old enough to vote
#Stretch: add an additional condition that checks for whether or not they are old enough to drive, 
#rent a car, or get a senior discount. 

#MEGA-STRETCH: Write a program starts by asking someone to input their age. 
#Based on their age, your program will need to print out what stage of their life they're in. 
# If the person if less that 2 years old: print a message that the person is a baby.
# If the person is at least 2 years old but less than 4 : print a message that the person is a toddler.
# If the person is at least 4 years old but less that 13 : print a message that the person is a kid
# If the person is at least 13 years old but less than 20 : print a message that the person is a teenager
# If a person is at least 20 years old but less that 65 : print a message that the person is an adult
# If the person is age 65 or older : print a message that the person is an elder

# age = 5
# if age < 2:
#     print("You are a baby")
# if age >= 2:
