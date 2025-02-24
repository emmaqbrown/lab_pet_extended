################################
# interface for the Pet object
# ----------
# it's up to you to implement the logical flow
################################

from pet import Pet                             # imports the Pet class from pet.py
from helpers import menu                        # import menu 


print("-"*36)
print("-- 🐶 Welcome to Pet Simulator 🐱 --")
print("-"*36,"\n")


my_pet = Pet()                                  # creates the pet 

game_play = True

menu_options = ["Introduce", "Quit"]

while game_play == True:

    chosen_option = menu("Menu",menu_options)

    if chosen_option == 'Introduce':
        my_pet.introduce()

    elif chosen_option == 'Quit':
        game_play = False
