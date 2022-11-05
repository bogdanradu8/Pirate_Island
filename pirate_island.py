print(f'''
######  ### ######     #    ####### #######    ###  #####  #          #    #     # ######  
#     #  #  #     #   # #      #    #           #  #     # #         # #   ##    # #     # 
#     #  #  #     #  #   #     #    #           #  #       #        #   #  # #   # #     # 
######   #  ######  #     #    #    #####       #   #####  #       #     # #  #  # #     # 
#        #  #   #   #######    #    #           #        # #       ####### #   # # #     # 
#        #  #    #  #     #    #    #           #  #     # #       #     # #    ## #     # 
#       ### #     # #     #    #    #######    ###  #####  ####### #     # #     # ######  
''')

print("Welcome to Pirate Island.\n")
print("The storm has sunken your ship and, luckily, has brought you to the shore of an island...")
print("Unfortunately, the island is occupied by savage pirates who will do anything\nto protect their treasure.")
print("You have to reach the house where the pirates live and steal their clothes.\nWith the new disguise you can steal one of their ships and escape!")
print("Good luck!")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a cave entrance. It looks like a shortcut to the place where the pirates are. Type "enter" to get inside the cave. Type "detour" to climb the mountain. \n').lower()
  if choice2 == "enter":
    choice3 = input("You arrive at the other side of the cave. 200 feet away is a house with 3 doors. One red, one yellow and one blue. Inside one of these 3 rooms you can find some pirate's clothes.  Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of drunk pirates. They are not happy to see you. Game Over.")
    elif choice3 == "yellow":
      print("You found the clothes! You Win!")
    elif choice3 == "blue":
      print("You enter and suddenly a big parrot starts shouting: 'Intruder!!!'  . Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry bear. Game Over.")
else:
  print("You meet face to face with One-Leg Nellie. He takes his gun out.\nGame Over.")