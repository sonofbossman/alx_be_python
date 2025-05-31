from random import randint

secret_number = randint(1, 10)
print(secret_number)

guess = int(input("Enter Your Guess: "))

match guess:
  case number if number == secret_number:
    print("Congratulations, you guessed it!")
  case _:
    print("Sorry, that's not correct.")