import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'


def main():
    file = open(FILE_NAME, 'r')
    words = file.readlines()
    chosen_value = random.choice(words)
    print(chosen_value.strip())
    keyboard_button = input("Press enter to continue, press q to quit: ")
    while keyboard_button == '':
        chosen_value = random.choice(words)
        print(chosen_value.strip())
        keyboard_button = input("Press enter to continue, press q to quit: ")
    print("End")


if __name__ == '__main__':
    main()