################################
# interface for the Pet object
# ----------
# edit the code below to implement the logical flow of the game
################################

from pet import Pet                             # imports the Pet class from pet.py
from helpers import menu                        # import menu 

game_play = True

menu_options = ["Introduce", "Quit"]

while game_play == True:

    chosen_option = menu("Menu",menu_options)

    if chosen_option == 'Quit':
        game_play = False

        