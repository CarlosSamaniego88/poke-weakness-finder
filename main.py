import requests
from bs4 import BeautifulSoup

def main():
    pokemon_to_exploit = input('Enter a Pokemon for its weaknesses:\n')
    url = 'https://pokemondb.net/pokedex/' + pokemon_to_exploit
    response = requests.get(url)
    weaknesses_html = []
    if response.status_code == 200:
        print('Success!')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tables = soup.find_all(class_='type-table type-table-pokedex')
        # print(tables)
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                target_column = row.find_all('td', 'type-fx-cell type-fx-200')
                weaknesses_html.append(target_column)    
    
    elif response.status_code == 404:
        print('Not Found.')
    
    for item in weaknesses_html:
        if item == []:
            weaknesses_html.remove(item)
        else:
            pass
    print(weaknesses_html)
if __name__ == '__main__':
    main() 
