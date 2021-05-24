from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    # move to beeper
    move()
    move()

    pick_beeper()

    # move to destination
    move()
    turn_left()
    move()
    move()

    put_beeper()

    # return to the start point
    turn_around()
    move()
    move()
    turn_right()
    move()
    move()
    move()

    # re-direction
    turn_around()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('Puzzle.w')
