import random

num = random.randint(1, 100)

print("WELCOME TO GUESS THE NUMBER!\n""Let me select a number between 1 and 100 \n" "If your guess is larger than my number, I will tell more\n"
      "If your guess is less than my number, I will tell less\n"
      "You have 7 chances to guess my number\n"
      "LET'S PLAY!")

guesses = [0]
while (True):
    guess = int(input('Make your guess\n'))
    if guess < 1 or guess > 100:  # to ensure guess lies within the range
        print("OUT OF BOUNDS!")
        continue

    if guess == num:
        print('CONGRATULATIONS!, you guessed the correct answer in {} attempts.\n'.format(len(guesses)))
        break
    guesses.append(guess)  # all the incorrect guesses are added to  list
    if len(guesses) > 7:  # after nine trials player may choose to know the answer
        x = int(input('YOU LOSE!!! \nDo you want to know the answer?\nPress 1 for Yes and 0 to No\n'))
        if x == 1:
            print(num)
            print('Try next time, Cheers!')

            break
        if x==0:
            print('Try next time, Cheers!')
            break

    else:
        if num>guess:
            print('MORE!', 8-len(guesses),' chances left')
        else:
            print('LESS!', 8-len(guesses),' chances left')
