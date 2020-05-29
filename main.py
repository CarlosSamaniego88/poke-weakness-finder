import requests
from bs4 import BeautifulSoup

class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

def main():
    pokemon_to_exploit = input('Enter a Pokemon for its weaknesses:\n')
    url = 'https://pokemondb.net/pokedex/' + pokemon_to_exploit
    response = requests.get(url)
    print('')
    weaknesses_html = []
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tables = soup.find_all(class_='type-table type-table-pokedex')
        i = 0        #need to add mega implementation
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                if i < 5:
                    target_column = row.find_all('td', 'type-fx-cell type-fx-200')
                    weaknesses_html.append(target_column)    
                    i+= 1
    
        for item in weaknesses_html:
            if item == []:
                weaknesses_html.remove(item)
            else:
                #item = item.replace('<td class="type-fx-cell type-fx-200" title=','')
                pass
        poke_weaknesses = []
        for weakness in weaknesses_html:
            for inner in weakness:
                inner = str(inner)
                left_item = inner.replace('<td class="type-fx-cell type-fx-200" title="','')
                right_item = left_item.replace(' = super-effective">2</td>','')
                #print(right_item)
                item_array = right_item.split()
                #print(item_array)
                poke_weaknesses.append(item_array[0])
        print('WEAKNESSES:')

        weak_color_dict = {
            'Normal':colors.fg.darkgrey,
            'Fire':colors.fg.red,
            'Water':colors.fg.cyan,
            'Electric':colors.fg.yellow,
            'Grass':colors.fg.green,
            'Ice':colors.fg.lightcyan,
            'Fighting':colors.fg.lightred,
            'Poison':colors.fg.purple,
            'Ground':colors.fg.orange,
            'Flying':colors.fg.lightcyan,
            'Psychic':colors.fg.pink,
            'Bug':colors.fg.lightgreen,
            'Rock':colors.fg.orange,
            'Ghost':colors.fg.blue,
            'Dragon':colors.fg.blue,
            'Dark':colors.fg.darkgrey,
            'Steel':colors.fg.darkgrey,
            'Fairy':colors.fg.pink
            
        }

        for weakness in poke_weaknesses:
            print(weak_color_dict[weakness], weakness)

    elif response.status_code == 404:
        print('Pokemon Not Found. Try Again')
    
if __name__ == '__main__':
    main() 
