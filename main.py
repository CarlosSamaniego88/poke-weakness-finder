import requests
from bs4 import BeautifulSoup
from colors import colors
from get_weaknesses import *

def main():
    pokemon_to_exploit = input('Enter a Pokemon for its weaknesses:\n')
    url = 'https://pokemondb.net/pokedex/' + pokemon_to_exploit
    response = requests.get(url)

    weak_color_dict = {'Normal':colors.fg.darkgrey,'Fire':colors.fg.lightred,'Water':colors.fg.cyan,
                       'Electric':colors.fg.yellow,'Grass':colors.fg.green,'Ice':colors.fg.cyan,
                       'Fighting':colors.fg.red,'Poison':colors.fg.purple,'Ground':colors.fg.orange,
                       'Flying':colors.fg.cyan,'Psychic':colors.fg.pink,'Bug':colors.fg.lightgreen,
                       'Rock':colors.fg.orange,'Ghost':colors.fg.blue,'Dragon':colors.fg.blue,
                       'Dark':colors.fg.darkgrey,'Steel':colors.fg.darkgrey,'Fairy':colors.fg.pink
                      }
    print('')

    weaknesses = []
    if response.status_code == 200:
        weaknesses = get_weaknesses(response)

        if len(weaknesses) == 0:
            print('{} has no weaknesses!!!!!'.format(pokemon_to_exploit).upper())
        else:
            print('WEAKNESSES: ')
            for weakness in weaknesses:
                if 'ultra' in weakness:
                    weakness = weakness.split()
                    weakness = weakness[0]
                    print(weak_color_dict[weakness], weakness, colors.fg.lightgrey, '(ultra)')
                else:
                    print(weak_color_dict[weakness], weakness)

    elif response.status_code == 404:
        print('Pokemon Not Found. Try Again')
    
if __name__ == '__main__':
    main() 
