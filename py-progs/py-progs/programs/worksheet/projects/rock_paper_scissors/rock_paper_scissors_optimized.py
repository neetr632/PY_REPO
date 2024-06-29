import random

def determine_winner(player, cpu):
    if player == cpu:
        return "DRAW AGAIN... NOBODY WINS!!"
    elif (
        (player == "ROCK" and cpu == "SCISSORS") or
        (player == "SCISSORS" and cpu == "PAPER") or
        (player == "PAPER" and cpu == "ROCK")
    ):
        return f"{player} WINS against {cpu}"
    else:
        return f"{player} LOSES against {cpu}"

def main():
    print("LET'S PLAY A GAME OF ROCK PAPER SCISSORS. CHOOSE YOUR MOVE BELOW BY INPUTTING YOUR VALUE")
    player_1 = str(input("Enter your choice (ROCK, PAPER, SCISSORS): ").upper())
    cpu = random.choice(["ROCK", "PAPER", "SCISSORS"])

    print(f"PLAYER_1:--{player_1}")
    print(f"CPU:--{cpu}")

    result = determine_winner(player_1, cpu)
    print(result)

if __name__ == "__main__":
    main()
