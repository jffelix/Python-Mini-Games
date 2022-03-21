import random

print("Welcome to dice roll!")
print("Press 'Enter' to roll the dice.")

while True:
    input("Hit Enter")

    randomNum = random.randrange(1, 7)

    if randomNum == 1:
        print("[               ]")
        print("[       o      ]")
        print("[               ]")
    elif randomNum == 2:
        print("[   o           ]")
        print("[                ]")
        print("[           o   ]")
    elif randomNum == 3:
        print("[   o           ]")
        print("[       o       ]")
        print("[           o   ]")
    elif randomNum == 4:
        print("[   o       o   ]") 
        print("[                 ]")
        print("[   o       o   ]")
    elif randomNum == 5:
        print("[   o       o   ]")
        print("[       o        ]")
        print("[   o       o   ]")
    elif randomNum == 6:
        print("[   o   o   o   ]")
        print("[                  ]")
        print("[   o   o   o   ]")

    print("Roll again? (y/n)")
    response = input("Type 'y' or 'n'.")

    if response.lower() == "y":
        continue
    elif response.lower() == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. You need to choose 'y' or 'n'.")
        break