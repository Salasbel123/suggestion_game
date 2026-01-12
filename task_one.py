import random



choices={"one":"coin","tow":"rock"}
# ///you can use this method by def method

# def suggestion_coin_rock():
#      random_choice = random.choice(list(choices.keys()))
#      print(random_choice)
# suggestion_coin_rock()

# ///////////

#///// but by lambda method you can make it in one line I preffer that
suggestion_coin_rock = lambda: random.choice(list(choices.values()))
# true_chance = suggestion_coin_rock()
# print(true_chance)

# ///////////

def gessed():
    print("Chocie coint or rock select one of them!!")
    selected_value=" "
    true_chance="_"
    while selected_value!=true_chance:
          true_chance = suggestion_coin_rock()
          selected_value= str(input("Enter your guessing word coin or rock: "))
          if selected_value!=true_chance:
          
             print("try agin the the true "+true_chance)
          else:
             print("Your select true "+selected_value)


gessed()




