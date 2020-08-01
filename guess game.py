n = 18
number_of_guesses=1
print("number of guesses is limited only 9 times:")
while (number_of_guesses<=9):
    guess_number = int(input("guess the number : \n"))
    break
if guess_number<=18:

    print("you entered lesser number please input greater number.\n")

elif guess_number>18:

    print("you entered greater number please input smaller number.\n")

else:
    print("you won.\n")
    print(number_of_guesses, "no. of guesses he took to finish")

print(9 - number_of_guesses, " no. of guesses left")
number_of_guesses = number_of_guesses + 1
if (number_of_guesses>9):
        print("better luck, next time")

