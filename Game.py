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
tur = ["Welcome to Typistol",

       "This is a typing game.",

       "But you will role-play as a\n"
       "  cowboy who fights with\n"
       "          criminals.",

       "   In order to attack the\n"
       "enemy thief you will need\n"
       "to type the text that comes\n"
       "     up on this screen.",

       "But be careful, enemies can\n"
       " attack you and if you type\n"
       "  incorrectly, the gun will\n"
       "     fire at you instead.",

       "This is an example of an\n"
       "      upcoming word.",

       "\n".join(Stage(100).typist()),

       "However, the further you\n"
       "play, the harder the game\n"
       "      difficulty will be.",

       "You can see the status of\n"
       "enemies near themselves.\n"
       "It will show two values,\n"
       "health and real-time attack.",

       "Health",

       "Real-time attack",

       "   And don't worry if you can\n"
       "type all the words on the screen\n"
       "     before being attacked.\n"
       "Enemies will reset attack time.",

       "When you defeat an enemy\n"
       " you gain experience and\n"
       "  if you reach a certain\n"
       "amount you will level up.",

       "You can see your stats\n"
       "at the top of the screen.",

       "   In the sun area you will\n"
       "see the number 0 representing\n"
       "the score. The score is based\n"
       "   on enemy difficulty and\n"
       "     elimination speed.",

       "In addition to the\n"
       "experience You also\n"
       "have a chance to get\n"
       "equipment and items.",

       "Items are disposable,\n"
       "you can use them by\n"
       " typing S , M , or L\n"
       "      to use them.\n"
       "  Their effect is to\n"
       "   increase health.",

       " Equipment has a maximum\n"
       "   value increase feature,\n"
       "  but the chance of getting\n"
       "it is lower than that of items.",

       "  You can check available\n"
       "equipment and items next\n"
       "     to your character.",

       "item",
       "equipment",

       " Be careful using items\n"
       " that you don't have,\n"
       "will count as misspelling",

       "Tutorial End"]


def tutor(x, y):
    global index, tur
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(0, -200)
    turtle.clear()

    stage = Stage(100)
    user = Player("tur", 100)

    if "cowboy" in tur[index]:
        cowboy.showturtle()
        monster.showturtle()

    elif "Health" == tur[index]:
        monster.showturtle()
        text(enemy_hp, f"HP: {stage.enemy.health}")

    elif "Real-time attack" == tur[index]:
        monster.showturtle()
        text(enemy_time, f"Attack in: {stage.enemy.attack_speed:.1f}")

    elif "reset" in tur[index]:
        monster.hideturtle()
        enemy_hp.clear()
        enemy_time.clear()

    elif "score" in tur[index]:
        text(score, 0)

    elif "equipment" == tur[index]:
        text(equipment, user.equipment)

    elif "item" == tur[index]:
        cowboy.showturtle()
        text(item, user.item)

    elif "stats" in tur[index]:
        text(player_status, user)

    elif "misspelling" in tur[index]:
        equipment.clear()
        item.clear()

    else:
        cowboy.hideturtle()
        monster.hideturtle()

    turtle.write(tur[index], font=("Verdana", 20, "normal"), align="center")
    if len(tur) > index + 1:
        index += 1
    else:
        text(title, "Enter to return\nto the menu")


def tutorial():
    title.clear()
    screen.onclick(tutor)
