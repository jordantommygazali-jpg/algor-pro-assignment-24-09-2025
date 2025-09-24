import random

def number_guessing_game():
    print("guess a number between 1 - 100")
    print("you have 7 tries. good luck\n")

    secret_number = random.randint(1, 100)
    attempts = 7

    while attempts > 0:
        try:
            guess = int(input(f"guess, you still have ({attempts} tries left): "))
        except ValueError:
            print("a valid number please")
            continue  
        
        if guess == secret_number:
            print("congrats! u guessed it... yay")
            break
        elif guess < secret_number:
            print("too low")
        else:
            print("too high")

        attempts -= 1  

    else:
        print(f"\nout of tries. the number was {secret_number}.")

number_guessing_game()