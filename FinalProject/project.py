"""
File: project.py
-----------------------
idea of this program is that I'm the person
who can hardly choose what to eat or what to cook
or sometimes I get bored of the menu and
cannot think of some new dished
-----------------------
This program gives you back a random dish
based on what did you choose to scope the category
-----------------------
!!!!Disclaimer!!!!!
All of the recipes which appear here are based on my preferences
I didn't include all of them because this is just a prototype and
because I'm still a beginner at Python
I didn't mean to say that food from others nationalities are not good
They are all delicious and worth to try!
"""


import random


def random_nationality():
    nationalities = ['thai', 'chinese', 'japanese', 'korean', 'italian', 'french', 'spanish', 'indian', 'mexican']
    return nationalities[random.randint(0, len(nationalities))]


def random_ingredient():
    ingredients = ['chicken', 'pork']


def main():
    print("Welcome to the program, which will help you choose what to eat/cook today")
    print("Please enter e to let the program choose what to eat")
    print("or enter c to let the program choose what to cook")
    choice = input("Enter e or c (in lower case) : ")
    while (choice != 'e') and (choice != 'c'):
        print("Please enter only e or c")
        choice = input("Enter e or c (in lower case) : ")
    if choice == 'e':
        random_nationality()
    elif choice == 'c':
        random_ingredient()


if __name__ == '__main__':
    main()
