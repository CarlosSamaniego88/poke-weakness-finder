import requests
from bs4 import BeautifulSoup
from colors import colors
from get_weaknesses import *
from get_pokemon_type import *
from exploit_pokemon import *

def main():
    print('', colors.fg.lightgrey)
    print('WELCOME TO POKEMON WEAKNESS FINDER', colors.fg.lightred)
    print('Type CTRL-C to exit', colors.fg.lightgrey)
    print('', colors.fg.lightgrey)
    try:
        while True:
            pokemon_to_exploit = input('Enter a Pokemon for its weaknesses:\n')
            print('')
            print("{} TYPING:".format(pokemon_to_exploit).upper())
            get_pokemon_type(pokemon_to_exploit)
            print('', colors.fg.lightgrey)
            exploit_pokemon(pokemon_to_exploit)
            print('',colors.fg.lightgrey)
            print('------------------------------------------------')

    except KeyboardInterrupt:
        print('interrupted!')

if __name__ == '__main__':
    main() 
