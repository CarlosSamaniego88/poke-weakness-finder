import requests
from bs4 import BeautifulSoup

def get_weaknesses(response):
    weaknesses_html = []
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

    return poke_weaknesses
