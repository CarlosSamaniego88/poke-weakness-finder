import requests
from bs4 import BeautifulSoup
from colors import colors
import re

weak_color_dict = {'Normal':colors.fg.darkgrey,'Fire':colors.fg.lightred,'Water':colors.fg.cyan,
                   'Electric':colors.fg.yellow,'Grass':colors.fg.green,'Ice':colors.fg.cyan,
                   'Fighting':colors.fg.red,'Poison':colors.fg.purple,'Ground':colors.fg.orange,
                   'Flying':colors.fg.cyan,'Psychic':colors.fg.pink,'Bug':colors.fg.lightgreen,
                   'Rock':colors.fg.orange,'Ghost':colors.fg.blue,'Dragon':colors.fg.blue,
                   'Dark':colors.fg.darkgrey,'Steel':colors.fg.darkgrey,'Fairy':colors.fg.pink
                   }


def get_pokemon_type(searched_pokemon):
    url = 'https://pokemondb.net/pokedex/' + searched_pokemon
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find(class_='vitals-table')
        
        type_list = ['normal','fire','water','electric','grass','ice','fighting','poison','ground','flying',
                     'psychic', 'bug', 'rock', 'ghost','dragon','dark','steel','fairy'    
                ]
        class_list = 'type-icon type-'
        
        type_classes = []
        for item in type_list:
            new_item = class_list + item
            type_classes.append(new_item)

        
        pokemon_nature = []
        rows = table.find_all('a')
        for row in rows:
            row = str(row)
            if 'type-icon' in row:
                for nature in type_classes:
                    if nature in row:
                        #print(table.find('a', {'class':nature}).text)
                        a_nature = table.find('a', {'class':nature}).text
                        pokemon_nature.append(a_nature)
        
        for nature in pokemon_nature:
            print(weak_color_dict[nature], nature)

    elif response.status_code == 404:
        print('Pokemon Not Found. Try Again')

def main():
    searched_pokemon = input("Find this pokemon's type:\n")
    get_pokemon_type(searched_pokemon)

if __name__ == '__main__':
    main() 
