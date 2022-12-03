import turtle
import time
import json
from Player import Player
from Stage import Stage
from threading import Timer, Thread


def set_image(picture, x, y):
    obj = turtle.Turtle(shape=picture, visible=False)
    obj.penup()
    obj.setpos(x, y)
    return obj


def text(obj, msg):
    obj.clear()
    obj.write(msg, font=("Verdana", 20, "normal"), align="center")


word = ""


def get_input():
    global word
    word = input()


while True:
    print("Select 1 to play the game\n"
          "Select 2 to view the leaderboard.\n"
          "Select 3 to find a player")
    choose = input("please select: ")
    if choose == "1":
        name = input("User name: ")
        try:
            with open("record.json") as data_file:
                user_record = json.load(data_file)
                while name in user_record.keys():
                    print("invalid user name.\nPlease try again.")
                    name = input("User name: ")
                user = Player(name)

        except FileNotFoundError:
            new_data = {
                name: {
                    "score": 0,
                    "time": 0
                }
            }
            with open("record.json") as data_file:
                json.dump(new_data, data_file)

        break

    if choose == "2":
        try:
            with open("record.json") as data_file:
                user_record = json.load(data_file)
            print(user_record)

        except FileNotFoundError:
            print("Not found leaderboard")

    if choose == "3":
        name = input("uses name: ")
        try:
            with open("record.json") as data_file:
                user_record = json.load(data_file)
            try:
                print(name)
                print(f"score = {user_record[name]['score']}")
                print(f"time = {user_record[name]['time']}")
            except KeyError:
                print(f"User {name} not found")

        except FileNotFoundError:
            print("Not found leaderboard")

    else:
        print("invalid choice")

screen = turtle.Screen()
screen.setup(width=1071, height=509, startx=0, starty=20)
screen.bgpic("background.png")

screen.addshape("cowboy.gif")
screen.addshape("enemy.gif")

cowboy = set_image("cowboy.gif", -270, -140)
player_status = set_image("turtle", 0, 190)
equipment = set_image("turtle", -170, -250)
item = set_image("turtle", -170, -120)
score = set_image("turtle", 130, 110)

monster = set_image("enemy.gif", 270, -90)
enemy_hp = set_image("turtle", 150, -150)
enemy_time = set_image("turtle", 200, -240)
stage = Stage()

cowboy.showturtle()
monster.showturtle()

text(score, 0)
text(equipment, user.equipment)
text(item, user.item)
text(player_status, user)
text(enemy_hp, f"HP: {stage.enemy.health}")
text(enemy_time, f"Attack in: {round(stage.enemy.attack_speed)}")

whole_time = time.time()
player_input = Thread(target=get_input)
while True:
    word_list = stage.typist()
    display = {word_list[i]: set_image("turtle", 0, -15 - i * 50)
               for i in range(len(word_list))}
    [text(v, k) for k, v in display.items()]

    speed = stage.enemy.attack_speed
    enemy_attack = Timer(speed, stage.fight, (stage.enemy, user))
    enemy_attack.start()

    start = time.time()
    one = time.time()
    while True:
        end = time.time()
        if end - start > speed:
            text(player_status, user)
            enemy_attack = Timer(speed, stage.fight, (stage.enemy, user))
            enemy_attack.start()
            start = end

        if not player_input.is_alive():
            player_input = Thread(target=get_input)
            player_input.start()

            if word in word_list:
                stage.fight(user, stage.enemy)
                word_list.remove(word)
                display[word].clear()
                if stage.next(user, time.time() - whole_time):
                    enemy_attack.cancel()
                    text(score, stage.score)
                    text(equipment, user.equipment)
                text(enemy_hp, f"HP: {stage.enemy.health}")
            elif word.upper() in ["S", "M", "L"]:
                user.use_item(word.upper())
            else:
                user.misspell(stage.difficulty)

            text(item, user.item)
            text(player_status, user)

        two = time.time()
        if two - one >= 0.1:
            attack_in = stage.enemy.attack_speed - (time.time() - start)
            text(enemy_time, f"Attack in: {attack_in:.1f}")
            one = two

        if not word_list:
            enemy_attack.cancel()
            break

        if user.health <= 0 or word == "OVER":
            break

    if user.health <= 0 or word == "OVER":
        break

stage.record(user.name, round(time.time() - whole_time))
text(player_status, user)
text(score, f"score = {stage.score}\ngame_over")
screen.mainloop()
