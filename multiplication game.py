import random

#print your welcome message here


for num in range(0,10):
    #pick the numbers to multiply
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    answer = number1 * number2

    guess = 0
    print ("What is", number1, "x", number2, "?")

    while guess != answer:
        guess = int(input("Answer: "))
        if guess != answer:
            print ("No, try again")

    print ("You got it!")
