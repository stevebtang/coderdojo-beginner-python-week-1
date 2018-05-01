import random

# Finish the Game
# 1. Ask the user for his name 
# 2. Print a welcome message introducing the game and a goodbye message when user leaves 
# 3. Use random so it doesn't ask 1 x 1 every time (look at the number guessing game for an example)
# 4. How can you repeat the code so it asks 10 questions in a row?
#    You could use a for loop that repeats code a specific number of times. This line will repeat the indented code 10 times:
#        for num in range(0,10):
# Bonus 1. Can you count how many times they got questions wrong and tell them at the end of the game?
# Bonus 2. Can you add another level with a harder num range?
# Bonus 3. Can you add addition and subtraction problems as well?
# Bonus 4. Can you ask to multiply/add/subtract 3 numbers instead of 2?
# Bonus 5. What other games can you do with user input?  
# Bonus 6. Can you build a calculator ?

# ---- code below this line ------------

#print your welcome message here


for num in range(0,1):
    #pick the numbers to multiply
    number1 = 1
    number2 = 1
    answer = number1 * number2

    guess = 0
    print ("What is", number1, "x", number2, "?")

    while guess != answer:
        guess = int(input("Answer: "))
        if guess != answer:
            print ("No, try again")

    print ("You got it!")
