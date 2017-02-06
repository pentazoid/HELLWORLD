def main():
    import random
    name=input("What is your name?")
    print("Hello" + name + "!Im a rock paper scissors game.")
    choice=input("Would you like to play")
    if choice==("yes"):
       print("Ok lets begin!")
       answer=input("rock, paper or scissors")
       rand=random.randint(1,3)
       if answer==("rock"):
           if rand==(1):
               print("Tie game!")
           elif rand==(2):
               print ("Your opponents paper covered your rock. You lose.")
           elif rand==(3):
               print ("You smashed your opponents scissors with a rock !")
               
       if answer==("paper"):
           if rand==(2):
               print ("Tie game!")
           elif rand==(1):
               print ("Your paper covered your opponents rock  with paper. You paper you win.")
           elif rand==(3):
               print ("Your opponents scissors cut your scissors with rock, you lose")
       if answer==("scissors"):
           if rand==(3):
               print ("Tie game!")
           elif rand==(2):
               print ("Your ssissors cut opponents paper.  you win.")
           elif rand==(1):
               print ("Your opponents rock smashed your scissors you lose, you lose")

main()
