# program that asks users to role a 6 sided die

def main():
    import random
    name=input("What is your name?")
    print("Hello" + name +"Welcome to the roll dice game!")
    choice=input("Would you like to play?")
    if choice==("yes"):
        print("lets begin then!roll the dice")
        rand=random.randint(1,6)
        if rand==(6):
            print("Your die landed on 6")

        elif rand==(1):
            print("Your die landed on 1:")
        elif rand==(2):
            print("Your die landed on 2:")
        elif rand==(3):
            print("Your die landed on 3:")
        elif rand==(4):
            print("Your die landed on 4:")
        elif rand==(5):
            print("Your die landed on 5:")


main()
      
                    
            

        
