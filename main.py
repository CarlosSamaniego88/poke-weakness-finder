import requests
from bs4 import BeautifulSoup
from colors import colors
from get_weaknesses import *

def main():
    pokemon_to_exploit = input('Enter a Pokemon for its weaknesses:\n')
    exceptions = {"farfetch'd": "farfetchd", "sirfetch'd":"sirfetchd",
                  "mr.mime": "mr-mime", "mime jr.":"mime-jr",
                  "type: null": "type-null", "tapu koko":"tapu-koko",
                  "tapu lele":"tapu-lele", "tapu bulu": "tapu-bulu",
                  "tapu fini": "tapu-fini"
                 }

    weak_color_dict = {'Normal':colors.fg.darkgrey,'Fire':colors.fg.lightred,'Water':colors.fg.cyan,
                       'Electric':colors.fg.yellow,'Grass':colors.fg.green,'Ice':colors.fg.cyan,
                       'Fighting':colors.fg.red,'Poison':colors.fg.purple,'Ground':colors.fg.orange,
                       'Flying':colors.fg.cyan,'Psychic':colors.fg.pink,'Bug':colors.fg.lightgreen,
                       'Rock':colors.fg.orange,'Ghost':colors.fg.blue,'Dragon':colors.fg.blue,
                       'Dark':colors.fg.darkgrey,'Steel':colors.fg.darkgrey,'Fairy':colors.fg.pink
                      }
 
    for pokemon in exceptions:
        if pokemon == pokemon_to_exploit:
            pokemon_to_exploit = exceptions[pokemon_to_exploit]
            url = 'https://pokemondb.net/pokedex/' + pokemon_to_exploit
            response = requests.get(url) 
        else:
            pass

    if pokemon_to_exploit == 'nidoran':
        m_or_f = input('Male or Female? (m/f):\n')
        if m_or_f == 'm':
            url = 'https://pokemondb.net/pokedex/nidoran-m'
            response = requests.get(url)
        
        elif m_or_f == 'f':
            url = 'https://pokemondb.net/pokedex/nidoran-f'
            response = requests.get(url)

    else:
        url = 'https://pokemondb.net/pokedex/' + pokemon_to_exploit
        response = requests.get(url)

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
