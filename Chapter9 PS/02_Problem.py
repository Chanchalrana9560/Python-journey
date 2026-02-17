import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 62)

    # Read hiscore safely
    try:
        with open("hiscore.txt", "r") as f:
            hiscore = f.read()
            hiscore = int(hiscore) if hiscore != "" else 0
    except FileNotFoundError:
        hiscore = 0

    print(f"Your score: {score}")

    # Write new hiscore if score is higher
    if score > hiscore:
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()
