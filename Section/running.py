"""
Prompts the user to enter numbers and prints
the running total until the user enters 0.
"""


def main():
    total = 0
    my_max = 0
    my_min = 0
    input_value = int(input("Enter a value: "))
    total += input_value
    my_max = check_my_max(my_max, input_value)
    my_min = check_my_max(my_min, input_value)
    while input_value != 0:
        print("Running total is " + str(total))
        print("maximum so far is " + str(my_max))
        print("minimum so far is " + str(my_min))
        input_value = int(input("Enter a value: "))
        my_max = check_my_max(my_max, input_value)
        my_min = check_my_min(my_min, input_value)
        total += input_value



def check_my_max(my_max, val):
    if my_max < val:
        my_max = val
    return my_max


def check_my_min(my_min, val):
    if my_min > val:
        my_min = val
    return my_min


if __name__ == '__main__':
    main()
