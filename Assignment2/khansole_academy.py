"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

MIN_RANDOM = 10
MAX_RANDOM = 99
total_correct = 0

# Prints out a randomly generated addition problem
# and checks if the user answers correctly.


def generate_problems():
    global total_correct
    num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
    num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
    total: int = num1 + num2
    print("What is", num1, "+", num2, "?")
    answer = input("Your answer: ")
    answer = int(answer)
    if answer == total:
        total_correct += 1
        print("Correct! You've gotten " + str(total_correct) + " correct in a row.")
    else:
        print("Incorrect. The expected answer is " + str(total))
        total_correct = 0


def main():
    while total_correct < 3:
        generate_problems()
    print("Congratulations! You mastered addition.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
