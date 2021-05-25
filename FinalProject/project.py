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
I didn't include ALL of them because this is just a prototype and
because I'm still a beginner at Python
I didn't mean to say that food from others nationalities are not good
They are all delicious and worth to try!
And I didn't mean that these examples from each nationalities are the best
as I said, I didn't include ALL. There are a lot to try!
Moreover, some might say that, some dish belong whereelse. In my opinion,
foods are influenced by culture and they are mixed. So some dishes cannot
be exactly categorized, from which country it belongs to. I tried my best to not
include these not sure menus.
One more thing, which I want to mention, is I didn't say that, categorize by nationalities
are the best way to do and everyone should do. It's just my style to come up
with idea, what I want to eat.
"""


import random


# this part of the program is to random what to eat
def what_to_eat():
    print("\nOur choices are")
    print("Chinese, Italian, Japanese, Korean, Thai, Vietnamese and general")
    print("Do you have any preferences?")
    print("\nEnter the nationalities of your preference(all in lower case) or r for random")
    nationality = input("\nPlease enter your preference: ")
    if nationality == 'r':
        nationality = random_nationality()
    return nationality


def random_nationality():
    nationalities = ['chinese', 'italian', 'japanese', 'korean', 'thai', 'general']
    return nationalities[random.randint(0, len(nationalities) - 1)]


def specify_dish_to_eat(nationality):
    dishes = {
        'chinese': ["Mapo Tofu", "Baozi", "Peking Duck", "Gong Bao Ji Ding", "Hotpot"],
        'italian': ["Pizza", "Carbonara(no cream!)", "Risotto", "Lasagna", "Arancini"],
        'japanese': ["Onigiri", "Tonkatsu", "Okonomiyaki", "Soba", "Katsudon"],
        'korean': ["Dakgalbi", "Bibimbap", "Tteokbokki", "Kimchi Jjigae", "Kalguksu"],
        'thai': ["Padkaprao", "Somtam", "Padprikkaeng", "Kangsom", "Pupadpongkaree"],
        'general': ["Fried Noodle", "Fried Rice", "Fried Vegetable", "Omelette", "Fried Chicken"]
            }
    dish = dishes[nationality][random.randint(0, 5)]
    return dish


# this part of the program is to random what to cook
def what_to_cook():
    print("\nOur choices are")
    print("Chicken, Pork, Shrimp, Tofu, (only) Vegetable")
    print("Do you have any preferences?")
    print("\nEnter the ingredients of your preference(all in lower case) or r for random")
    ingredient = input("\nPlease enter your preference: ")
    if ingredient == 'r':
        ingredient = random_main_ingredient()
    return ingredient


def random_main_ingredient():
    ingredients = ['chicken', 'pork', 'shrimp', 'tofu', 'vegetable']
    return ingredients[random.randint(0, len(ingredients) - 1)]


def specify_dish_to_cook(ingredient):
    dishes = {
        'chicken': ["Green curry", "Dakbokkeumtang", "Tikka Massala", "Khaipadmedmamaung", "Chicken rice"],
        'pork': ["Moosatay", "Char Siu", "Padkaprao", "Pad See Ew", "Baked pork ribs"],
        'shrimp': ["Freid curry", "Tomyam", "Kaeng Liang", "Pad Thai", "Fried rice"],
        'tofu': ["Mapo Tofu", "Kaipalo", "Taohunamdang", "Sundubu Jjigae", "Fried tofu with sweet&sour sauce"],
        'vegetable': ["Bibimbap", "Fried Cabbage with fish sauce", "Kangsom", "Mushroom soup", "Lab Hed"],
            }
    dish = dishes[ingredient][random.randint(0, 5)]
    return dish


def main():
    print("Welcome to the program, which will help you choose what to eat/cook this meal")
    print("\nPlease enter e to let the program choose what to eat")
    print("or enter c to let the program choose what to cook")
    choice = input("\nEnter e or c (in lower case) : ")
    while (choice != 'e') and (choice != 'c'):
        print("Please enter only e or c")
        choice = input("\nEnter e or c (in lower case) : ")
    if choice == 'e':
        result = what_to_eat()
        print("\nThis is your random nationality of your dish this meal: " + result)
        print("\nDo you want to continue the program to specify the menu?")
        choice = input("Please enter y for yes, and n for no (in lower case): ")
        while (choice != 'y') and (choice != 'n'):
            print("Please enter only y or n")
            choice = input("Please enter y for yes, and n for no (in lower case): ")
        if choice == 'y':
            result = specify_dish_to_eat(result)
    elif choice == 'c':
        result = what_to_cook()
        print("\nThis is your random ingredient of your dish this meal: " + result)
        print("\nDo you want to continue the program to specify the menu?")
        choice = input("Please enter y for yes, and n for no (in lower case): ")
        while (choice != 'y') and (choice != 'n'):
            print("Please enter only y or n")
            choice = input("Please enter y for yes, and n for no (in lower case): ")
        if choice == 'y':
            result = specify_dish_to_cook(result)
    print("\nThis is your final result: " + result)
    print("Enjoy your meal!")


if __name__ == '__main__':
    main()
