import os
import save_load_game
import character_creation as character

from my_coloring import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

ch_data = character.create_character()








# save_load_game.save_game(ch_data)
# print(ch_data)
