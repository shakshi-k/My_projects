import random

list = ["Rock", "Paper", "Scissors"]
lives = 3
print("\nGame started! You have 3 lives!\n")
while lives != 0:

    while True:
        print("Choice: Rock(r)  Paper(p)  Scissors(s)  Quit(q)\n")
        user_select = input("Enter the choice: ").lower()
        if user_select in ["r", "p", "s", "q"]:
            break


    comp_select = random.choice(list)
    print("computer move is " , comp_select, "\n")

    if user_select == "r" and comp_select =="Paper":
        print("You loose")
        lives = lives - 1
        print("lives" , lives)
        continue
    elif user_select == "s" and comp_select =="Rock":
        print("You loose")
        lives = lives - 1
        print("lives" , lives)
        continue
    elif user_select == "p" and comp_select == "Scissors":
        print("You loose")
        lives = lives - 1
        print("lives" , lives)
        continue
    elif user_select == "q":
        break

print("Game ended! Hope you have a great day! ")