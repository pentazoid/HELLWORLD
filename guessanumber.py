def main():
    import random
    guess=input("Guess a number between 1 and 1000")
    number=random.randint(1,100)

    attempts=0

    while guess!=number:
        attempts=attempts+1
        guess=input('Attempt')
        guess=int(guess)

        if guess>number:
            print('too low')
        elif guess<number:
            print("Too high")
        elif answer==number:
            print('you got it in %i tries'%(attempts))
    print('number is',number)


main()    
