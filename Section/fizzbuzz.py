"""
Prints the Fizz Buzz sequence up to a given number.
"""


def main():
    fizz = 0
    buzz = 0
    fizzbuzz = 0
    n = int(input("Number to count to: "))
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
            fizzbuzz += 1
        elif i % 5 == 0:
            print("Buzz")
            buzz += 1
        elif i % 3 == 0:
            print("Fizz")
            fizz += 1
        else:
            print(str(i))
    print("Num fizzed: " + str(fizz))
    print("Num buzzed: " + str(buzz))
    print("Num fizzbuzzed: " + str(fizzbuzz))


if __name__ == '__main__':
    main()