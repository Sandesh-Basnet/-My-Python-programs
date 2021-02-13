# buid a simple guessing game 
# the guess value
value = 79
#getting input from the user
entered = int(input("Guess the value: " ))
#to chect if the winner won or lost  by using if and elif statements
if entered == value:
    print("YOU WON ")
else:
    print("YOU LOST")
