import datetime
import json
import random


# Function for playing the game
def play_game(level="easy"):
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret and level == "easy":
            print("Your guess is not correct... try something smaller")
        elif guess < secret and level == "easy":
            print("Your guess is not correct... try something bigger")
        else:
            print("Your guess is not correct.")


# Get a list of all scores
def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


# Return top 3 scores
def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return top_score_list


# Run the game
while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if selection.upper() == "A":
        level = input("Choose your level (easy/hard): ")
        play_game(level=level)
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break
