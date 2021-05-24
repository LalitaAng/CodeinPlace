"""
File: nimm.py
-------------------------
The game of Nimm goes as follows:
    The game starts with a pile of 20 stones between the players.
    The two players alternate turns.
    On a given turn, a player may take either 1 or 2 stone from the center pile.
    The two players continue until the center pile has run out of stones.
    The last player to take a stone loses.
"""

TOTAL_STONES = 20


def main():
    remove_stone(TOTAL_STONES)


def remove_stone(stones):
    player = 1
    # how many stones are left. If there is still some, player can still play a game
    while stones != 0:
        print("\nThere are " + str(stones) + " stones left")
        print("Player", who(player))
        remove = int(input("would you like to remove 1 or 2 stones? "))
        # players can only remove 1 or 2 stone(s) at time
        while (remove != 1) and (remove != 2):
            remove = int(input("Please enter 1 or 2: "))
        check_winner(stones, who(player))
        stones -= remove
        player += 1
    print("\nGame over")


# check which player is playing this round
def who(player_num):
    if player_num % 2 == 1:
        return 1
    return 2


def check_winner(stones, player):
    if stones <= 2:
        print("\nPlayer" + str(player) + "wins!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
