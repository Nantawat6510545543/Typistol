import turtle
import time
import os
from threading import Timer, Thread

from Player import Player
from Stage import Stage

word = ""


def get_input():
    global word
    word = input()


def set_image(picture, x, y):
    obj = turtle.Turtle(shape=picture, visible=False)
    obj.penup()
    obj.setpos(x, y)
    return obj


def text(obj, msg):
    obj.clear()
    obj.write(msg, font=("Verdana", 20, "normal"), align="center")


screen = turtle.Screen()
screen.setup(width=1071, height=509)
screen.bgpic("background.png")

title = turtle.Turtle(shape="turtle", visible=False)
title.penup()
title.setpos(0, -100)
title.write("Typistol", font=("Verdana", 30, "bold"), align="center")

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


def typistol(name):
    stage = Stage()
    title.clear()
    user = Player(name)

    cowboy.showturtle()
    monster.showturtle()
    text(score, 0)
    text(equipment, user.equipment)
    text(item, user.item)
    text(player_status, user)
    text(enemy_hp, f"HP: {stage.enemy.health}")

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
            if not enemy_attack.is_alive():
                text(player_status, user)
                enemy_attack = Timer(speed, stage.fight, (stage.enemy, user))
                enemy_attack.start()
                start = time.time()

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
                    user.use_item(word.upper(), stage.difficulty)

                else:
                    user.misspell(stage.difficulty)

                os.system('cls')

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
                stage.record(user.name, round(time.time() - whole_time))
                text(player_status, user)
                text(score, f"score = {stage.score}\ngame_over")
                [display[k].clear() for k, v in display.items()]
                text(title, "Enter to return\nto the menu")
                return None


index = 0
tur = ["man", "go", "test"]


def tutor():
    global index, tur
    turtle.hideturtle()
    turtle.clear()
    turtle.write(tur[index])
    index += 1
    if index == 3:
        return None


def tutorial():
    stage = Stage()
    title.clear()
    screen.onclick(tutor)
