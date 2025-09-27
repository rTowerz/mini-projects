name = input("Type your name: ")
print("Hello " + name + "! Welcome to my game!")

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "y" or should_we_play == "yes":
    print("Lets play!!")

    direction = input("You are in a dark room. There is a door to your left and right. Whicn one do you take? (left/right) ").lower()
    if direction == "left":
        choice = input("You have come to the kitchen. On the table there is a cake. It look delicious. Do you want to eat it? (yes/no) ").lower()
        if choice == "yes":
            print("You ate a poisonus cake. You lose! try again")
        else: 
            print("You live another day. You win!")
    elif direction == "right":
        choice = input("You have come to the room with a monster. It looks hungry. Do you want to fight it or run away? (fight/run) ").lower()
        if choice == "fight":
            print("You lost the fight. You lose! Try again.")
        elif choice == "run":
            print("You run away and scaped the monter. You win!")
        else:
            print("You stumble around the room and the monster eats you. You lose! Try again.")
    else:
        print("You fell asleep and never woke up. Game Over!")

else:
    print("Goodbye")