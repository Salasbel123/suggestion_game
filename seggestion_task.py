import random

# i wil generate random number by import random then limited it from 1 to 10 
# then make while loop to give user 3 times chance
#  inside the loop I will make check is the number that user entered is on of these status
# status one is larger then random number or smaller or equal
# to make loop condation I will initialize tow variable first_try = 0 last_try = 3


random_number = random.randint(1, 10)

def guessing_true_random_number():
    first_try = 0
    last_try = 3

    while first_try < last_try:
        try:
           
            user_insert_number = int(input("Insert a number from 1 to 10: "))

           
            if user_insert_number < 1 or user_insert_number > 10:
                print("The number has to be between 1 and 10.")
                # continue  # Skip the rest of the loop and run again

            if random_number > user_insert_number:
                print("You chose a number lower than the random number.")
            elif random_number < user_insert_number:
                print("You chose a number higher than the random number.")
            else:
                print("Congratulations! You chose the right number.")
                break  # Exit the loop if the guess is correct

            first_try += 1
            print(f"You have {last_try - first_try} try number left.")

        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    if first_try == last_try:
        print(f"Sorry! You've used all your chance. The random number was {random_number}.")


guessing_true_random_number()






























