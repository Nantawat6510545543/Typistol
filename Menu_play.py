import json
import os
import Game

"""
Run this file to get started.
"""
while True:
    print("Select 0 to start the tutorial\n"
          "Select 1 to play the game\n"
          "Select 2 to view the leaderboard.\n"
          "Select 3 to find a player\n"
          "Type 'exit' to quit the program")
    choose = input("please select: ")

    if choose == "0":
        print("Click the screen to view the tutorial or")
        Game.tutorial()

    elif choose == "1":
        name = input("User name: ")

        try:
            with open("record.json") as data_file:
                user_record = json.load(data_file)
            while name in user_record.keys():
                os.system('cls')
                print("invalid user name.\nPlease try again.")
                name = input("User name: ")

        except FileNotFoundError:
            new_data = {
                name: {
                    "score": 0,
                    "time": 0
                }
            }
            with open("record.json") as data_file:
                json.dump(new_data, data_file)
        os.system('cls')
        Game.typistol(name)

    elif choose == "2":
        try:
            with open("record.json") as data_file:
                user_record = json.load(data_file)
            user_record = sorted(user_record.items(),
                                 key=lambda x: x[1]['score'],
                                 reverse=True)
            n = 15
            print("-" * (3 * n + 4))
            print(f"|{'User':^{n}}|{'Score':^{n}}|{'Time':^{n}}|")
            for i in user_record:
                print(f"|{i[0]:^{n}}|"
                      f"{i[1]['score']:^{n}}|"
                      f"{i[1]['time']:^{n}}|")
            print("-" * (3 * n + 4))

        except FileNotFoundError:
            print("Not found leaderboard")

    elif choose == "3":
        name = input("uses name: ")
        try:
            with open("record.json") as data_file:
                user_record = json.load(data_file)
            try:
                print(f"User's name : {name}")
                print(f"Score : {user_record[name]['score']}")
                print(f"Time : {user_record[name]['time']}")
            except KeyError:
                print(f"User {name} not found")

        except FileNotFoundError:
            print("Not found leaderboard")

    elif choose == "exit":
        break

    else:
        os.system('cls')
        print("INVALID CHOICE")
        continue

    input("enter to go next : ")
    os.system('cls')
