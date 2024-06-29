import random
l2 = ["ROCK", "PAPER", "SCISSORS"]
print("LET'S PLAY A GAME OF ROCK PAPER SCISSORS CHOOSE YOUR MOVE BELOW BY INPUTTING YOUR VALUE")
PLAYER_1 = str(input("Enter your choice:- ROCK PAPERS SCISSORS:- ")).upper()
CPU = random.choice(l2)

print(f"PLAYER_1:--{PLAYER_1}")
print(f"CPU:--{CPU}")

if PLAYER_1 == "ROCK" and CPU == "SCISSORS":
    print(f"{PLAYER_1} WINS against {CPU}")
elif PLAYER_1 == "ROCK" and CPU == "PAPER":
    print(f"{PLAYER_1} LOSES against {CPU}")
elif PLAYER_1 == "ROCK" and CPU == "ROCK":
    print(f"{PLAYER_1} DRAWS against {CPU}")
    print("DRAW AGAIN... NOBODY WINS!!")
elif PLAYER_1 == "SCISSORS" and CPU == "ROCK":
    print(f"{PLAYER_1} lose against {CPU}")
elif PLAYER_1 == "SCISSORS" and CPU == "SCISSORS":
    print(f"{PLAYER_1} DRAWS against {CPU}")
    print("DRAW AGAIN... NOBODY WINS!!")
elif PLAYER_1 == "SCISSORS" and CPU == "PAPER":
    print(f"{PLAYER_1} WINS against {CPU}")
elif PLAYER_1 == "PAPER" and CPU == "SCISSORS":
    print(f"{PLAYER_1} LOSES against {CPU}")
elif PLAYER_1 == "PAPER" and CPU == "ROCK":
    print(f"{PLAYER_1} WINS against {CPU}")
elif PLAYER_1 == "PAPER" and CPU == "PAPER":
    print(f"{PLAYER_1} DRAWS against {CPU}")
    print("DRAW AGAIN... NOBODY WINS!!")
else:
    print("try again:- INVALID INPUT")
