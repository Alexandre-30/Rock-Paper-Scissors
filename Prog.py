import random
import time

Salty_Answers=["I win, You loose 😂 \n Imagine loosing to an AI!","To eazyy!😂","U thought you'd win 😂🤣","Try again later, but I'll always win 🫵   👎"]
Sad_Answers=["That was just luck🥀😅","Oh no!😭","You win😔","Hnoahahaha... Lucky Human 👨","That's just PURE LUCK 😡","Humans are luckyer than AI bots 😂🤣"]
AI_Choice_list=["Rock","Paper","Scissors"]

while True:
    UI=input("Enter your choice. It can either be Rock, Paper or Scissors. \n").strip().lower()
    AI_Choice = random.choice(AI_Choice_list)
    if UI in ("rock","🪨") and AI_Choice == "Paper":
        print(AI_Choice)
        print(random.choice(Salty_Answers))
    elif UI in ("rock","🪨") and AI_Choice == "Scissors":
        print(AI_Choice)
        print(random.choice(Sad_Answers))
    elif UI in ("paper","📃") and AI_Choice == "Scissors":
        print(AI_Choice)
        print(random.choice(Salty_Answers))
    elif UI in ("paper","📃") and AI_Choice == "Rock":
        print(AI_Choice)
        print(random.choice(Sad_Answers))
    elif UI in ("scissors","scissor","✂️","✂") and AI_Choice == "Rock":
        print(AI_Choice)
        print(random.choice(Salty_Answers))
    elif UI in ("scissors","scissor","✂️","✂") and AI_Choice == "Paper":
        print(AI_Choice)
        print(random.choice(Sad_Answers))
    elif UI == AI_Choice.lower():
        print(AI_Choice)
        print("It's a tie! Try again!")
    else:
        print("What? Check your spelling and try again :)")
        continue

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again  in ("no", "No","NO","n0"):
        print("Thanks for playing! Goodbye.")
        break
    else:
        continue

