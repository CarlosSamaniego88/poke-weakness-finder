import requests
from bs4 import BeautifulSoup
from colors import colors

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
                    target_column2 = row.find_all('td', 'type-fx-cell type-fx-400')
                    weaknesses_html.append(target_column)    
                    weaknesses_html.append(target_column2)
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
                if '200' in inner:
                    left_item = inner.replace('<td class="type-fx-cell type-fx-200" title="','')
                    right_item = left_item.replace(' = super-effective">2</td>','')
                    item_array = right_item.split()
                    poke_weaknesses.append(item_array[0])
                elif '400' in inner:
                    left_item = inner.replace('<td class="type-fx-cell type-fx-400" title="','')
                    right_item = left_item.replace(' = super=effective">4</td>','')
                    item_array = right_item.split()
                    poke_weaknesses.append(item_array[0]+' ultra')

        weak_color_dict = {'Normal':colors.fg.darkgrey,'Fire':colors.fg.lightred,'Water':colors.fg.cyan,
                           'Electric':colors.fg.yellow,'Grass':colors.fg.green,'Ice':colors.fg.cyan,
                           'Fighting':colors.fg.red,'Poison':colors.fg.purple,'Ground':colors.fg.orange,
                           'Flying':colors.fg.cyan,'Psychic':colors.fg.pink,'Bug':colors.fg.lightgreen,
                           'Rock':colors.fg.orange,'Ghost':colors.fg.blue,'Dragon':colors.fg.blue,
                           'Dark':colors.fg.darkgrey,'Steel':colors.fg.darkgrey,'Fairy':colors.fg.pink}

        if len(poke_weaknesses) == 0:
            print('{} has no weaknesses!!!!!'.format(pokemon_to_exploit).upper())
        else:
            print('WEAKNESSES: ')
            for weakness in poke_weaknesses:
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
