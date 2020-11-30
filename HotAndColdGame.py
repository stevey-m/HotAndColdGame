import random


def start_game():
    print("Guessing game for a random number between 1 and 100")
    print("  Hot or Cold!!")
    print("--------------------")
    random_number = random.randint(1, 100)
#    random_number = 2
    print (random_number)
    guess = -1
    number_of_guesses = 0
# while guess does not equal number

    while guess != random_number:
        guess = int(input('Guess the number: '))

        number_of_guesses = number_of_guesses + 1
#       if guess < random_number:
        if abs(guess - random_number) > 30:
            print('Cold!')
        elif abs(guess - random_number) > 20:
#        if guess > random_number:
            print('Warm!')
        elif abs(guess - random_number) > 10:
            print('Hot!')
#        elif abs(guess - random_number) in range(5,10):
        elif abs(guess - random_number) > 5:
            print('Lava!')
        elif abs(guess - random_number) in range(3,6):
            print('Very Close!')
        elif abs(guess - random_number) in range(1,3):
            print('So Very Very Close!')
        if guess == random_number:
            print('Congratulations!')
            break

    if guess == random_number:
        if number_of_guesses < 3:
            print('Great! It took you ' + str(number_of_guesses) +  ' tries to guess the number!')
            print('Superhuman! It took you ' + str(number_of_guesses) +  ' tries to guess the number!')
        elif number_of_guesses in range(3,5):
            print('Great! It took you ' + str(number_of_guesses) +  ' tries to guess the number!')
        elif number_of_guesses in range(5,10):
            print('Good! It took you ' + str(number_of_guesses) +  ' tries to guess the number!')
        elif number_of_guesses > 10:
            print('You can do better! It took you ' + str(number_of_guesses) +  ' tries to guess the number!')
    else:
        print('You did not guess the number. The number was ' + str(random_number))
        print()
    again()

def again():
# we will need to take input form user
    restart_game = input("Do you want to play again (y or n): ")

# if the usr selects Y, then call start_game function
# we can make the program accept Y or y by adding the .upper()
    if restart_game.upper() == 'Y':
        print("Lets play again!")
        print()
        start_game()
# if the user types N, say thanks and goodbye
# we can make the program accept N or n by adding the .upper()
    elif restart_game.upper() == 'N':
        print('See you later.')
# if the user types any other key aside N, call again until Y or N is entered
    else:
        again()    

if __name__ == "__main__":
    start_game()
    print()




# Hot and Cold!
# Have a function to generate a random numnber between 1 to 100. Create a simple startup menu screen to start the game. Take a user input to guess the number. If they are with a greater range than 30, print "Cold!". If they are within a 20 range, print "Warm!". If they are within a 10 range, print "Hot!". If they are within a 5 range, print "Lava!". If they guess the number, print "Congratulations!". Record the number of tries it took them to get the answer. Print the number of tries. If it took them less than 3 tries, print "Superhuman!". If it took them less than 5 tries, print "Great!", If it took them less than 10 tries print "Good!". If it took more than 10 tries, print "You can do better!". Ask them if they want to play again. Make sure they enter numbers only. Put a blank line before starting a new game
# Sample output:
# Hot and Cold!
# --------------------
# Guess the number: 34
# Cold!
# Guess the number: 88
# Hot!
# Guess the number: 99
# Lava!
# Guess the number: 100
# Great! It took you 4 tries to guess the number!
# Do you want to play again (y or n): y
# Lets play again!
# Hot and Cold!
# --------------------
# Guess the number: 90
# Cold!
# Guess the number: 80
# Cold!
# Guess the number: 85
# Cold!
# Guess the number: 100
# Cold!
# Guess the number: 70
# Cold!
# Guess the number: 60
# Cold!
# Guess the number: 50
# Cold!
# Guess the number: 30
# Warm!
# Guess the number: 20
# Warm!
# Guess the number: 10
# Lava!
# Guess the number: 8
# You can do better! It took you 11 tries to guess the number!
# Do you want to play again (y or n): n
# Thank you for playing!