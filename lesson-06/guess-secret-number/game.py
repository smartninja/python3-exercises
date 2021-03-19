import datetime
import json
import random


class Result:
    def __init__(self, attempts, player_name, date):
        self.attempts = attempts
        self.player_name = player_name
        self.date = date


# Function for playing the game
def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()
    player_name = input("Please enter your name: ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            result_obj = Result(attempts=attempts, player_name=player_name, date=str(datetime.datetime.now()))

            score_list.append(result_obj.__dict__)

            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")


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
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            result_obj = Result(attempts=score_dict.get("attempts"),
                                player_name=score_dict.get("player_name", "Anonymous"),
                                date=score_dict.get("date"))

            print("Player: {name}; Attempts: {attempts}; Date: {date}".format(name=result_obj.player_name,
                                                                              attempts=result_obj.attempts,
                                                                              date=result_obj.date))
    else:
        break
