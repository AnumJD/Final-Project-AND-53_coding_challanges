"""Problem Statement: Guess My Number

I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

Enter a new number: 25 Your guess is too low

Enter a new number: 40 Your guess is too low

Enter a new number: 45 Your guess is too low

Enter a new number: 48 Congrats! The number was: 48"""

#Solution:
import random 
def main():
    secret_No = random.randint(1,99)
    print("I am thinking of a number between 0 and 99...")
    guess = int(input("Enter a guess: "))
    while guess != secret_No:
        if guess < secret_No:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        print()
        guess = int(input("Enter a new guess: "))
    print("Congrats! Number was: {secret_No}") 
if __name__=="__main__":
    main()
        