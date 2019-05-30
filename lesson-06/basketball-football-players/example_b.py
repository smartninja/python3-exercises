class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2,
                          rebounds=7.4, assists=7.2)

kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2,
                           rebounds=7.1, assists=4)


print(lebron.first_name)
print(lebron.height_cm)

print(kev_dur.last_name)
print(kev_dur.rebounds)

bball_players = [lebron, kev_dur]

for player in bball_players:
    print(player.last_name + ", " + player.first_name)


# dictionary
lebron_dict = {"first_name": "Lebron", "last_name": "James", "height_cm": 203, "weight_kg": 113, "points": 27.2,
               "rebounds": 7.4, "assists": 7.2}

print(lebron_dict["first_name"])
print(lebron_dict["height_cm"])


# converting kg to lbs
print(lebron.weight_to_lbs())
print(kev_dur.weight_to_lbs())


# football
ronaldo = FootballPlayer(first_name="Cristiano", last_name="Ronaldo", height_cm=184, weight_kg=79, goals=586,
                         yellow_cards=95, red_cards=11)

messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575,
                       yellow_cards=67, red_cards=0)

print(ronaldo.first_name)
print(ronaldo.goals)
print(messi.first_name)
print(messi.goals)
print(messi.weight_to_lbs())

print(lebron.__dict__)

# user can enter data
print()  # empty line
print("Enter some football player's data!")
f_name = input("Enter player's first name: ")
l_name = input("Enter player's last name: ")
height = input("Enter player's height: ")
weight = input("Enter player's weight: ")
goals = input("Enter the number of player's goals: ")
y_cards = input("Enter the number of player's yellow cards: ")
r_cards = input("Enter the number of player's red cards: ")

new_player = FootballPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight),
                            goals=int(goals), yellow_cards=int(y_cards), red_cards=int(r_cards))

with open("football_players.txt", "w") as football_file:
    football_file.write(str(new_player.__dict__))

print("Player successfully entered!")
print("Player's data: {0}".format(new_player.__dict__))
