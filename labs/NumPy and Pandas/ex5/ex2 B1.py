import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Programming_language' #просто помещаем ссылку
response = requests.get(url)    #добавляем содержимое ссылки, но не распаковываем
soup = BeautifulSoup(response.text, 'html.parser') #распаковываем текст в переменную soup

search_python = soup.find_all('a', title='Python (programming language)')
search_C = soup.find_all('a', title='C++')

if len(search_python) > len(search_C):
    print('Python')
elif len(search_python) == len(search_C):
    print('Python = C++')
else:
    print('C++')
















