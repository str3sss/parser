import requests
from bs4 import BeautifulSoup

'''
Считает количество животных на каждую букву русского алфавита.
работает, но не оптимизировано.
'''

ABC = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ')
DICT = dict.fromkeys(ABC,0)

url = 'https://inlnk.ru/jElywR'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

while True:
    items = soup.find(id='mw-pages')
    
    h = items.find('h3')
    if h.text == 'A':break # только русские названия
    
    articles = items.find_all('li')
    
    for article in articles:
        for i in DICT:
            if article.text.startswith(i):
                DICT[i]+=1
                break
    
    nextpage = soup.find('a',string='Следующая страница')
    url = 'https://ru.wikipedia.org' + nextpage['href']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    
for i in DICT:
    print(f'{i}: {DICT[i]}')
