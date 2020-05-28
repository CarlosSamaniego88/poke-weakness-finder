import requests

def main():
    response = requests.get('https://pokemondb.net/pokedex/sceptile')
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')
    print(response.content)
if __name__ == '__main__':
    main() 
