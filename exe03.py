from random import randint


name = input("Welcom to Rock, Paper, Scissors game!\n\
Enter your name:")

final_score = int(input("How many points will determine the winner?"))


items = {1: "Rock", 2:"Paper", 3: "Scissors"}
user_score = 0
computer_score = 0

def winner(num1, num2):

    if ((items[num1] == items[1]) and (items[num2] == items[2])):
        win = {num2: items[num2]}
    elif ((items[num2] == items[1]) and (items[num1] == items[2])):
        win = {num1: items[num1]}
    elif ((items[num1] == items[1]) and (items[num2] == items[3])):
        win = {num1: items[num1]}
    elif ((items[num2] == items[1]) and (items[num1] == items[3])):
        win = {num2: items[num2]}    
    elif ((items[num1] == items[2]) and (items[num2] == items[3])):
        win = {num2: items[num2]}
    elif ((items[num2] == items[2]) and (items[num1] == items[3])):
        win = {num1: items[num1]}

    return win


while True:

    user_num = int(input("Enter number between 1 nad 6:"))
    sys_num = randint(1, 6)
    print(f"System chooses random number: {sys_num}")
        
    if user_num > sys_num:
        user_item = int(input("Select one of these items:\n\
                            1) Rock \
                            2) Paper \
                            3) Scissors"))

        sys_item = randint(1, 3)
        print(f"System item is: {sys_item}) {items[sys_item]}")

        if user_item != sys_item:
            win = winner(user_item, sys_item)
            if list(win.keys())[0] == user_item:
                user_score +=1
            elif list(win.keys())[0] != user_item:
                computer_score +=1
        else:
            continue
        
    elif sys_num > user_num:
        sys_item = randint(1, 3)

        user_item = int(input("Select one of these items:\n\
                            1) Rock \
                            2) Paper \
                            3) Scissors"))
        
        print(f"System item is: {sys_item}) {items[sys_item]}")

        if sys_item != user_item:
            win = winner(sys_item, user_item)
            if list(win.keys())[0] == user_item:  
                user_score +=1
            elif list(win.keys())[0] != user_item:
                computer_score +=1
        else:
            continue
    else:
        continue

    if user_score == final_score:
        print(f"User {name} is win")
        break
    elif computer_score == final_score:
        print("Computer is win")
        break