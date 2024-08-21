import random

choices=['rock','paper','scissor']

playing = True
while playing:

    Player=None
    computer=random.choice(choices)

    while Player not in choices:
        Player=input("\nEnter your choice('rock','paper','scissor'):")

    print(f"You : {Player} | Computer : {computer}")

    if Player==computer :
        print("No points! It's a tie!")
    elif Player=='rock' and computer=='paper' :
        print("1 point for Computer!")
    elif Player=='paper' and computer=='scissor' :
        print("1 point for Computer!")
    elif Player=='scissor' and computer=='rock' :
        print("1 point for Computer!")
    else:
        print("1 point for You!")

    play_again = input("Play again (yes/no):").lower()
    if not play_again == 'yes':
        playing = False
        
print("\nThanks for playing!")
