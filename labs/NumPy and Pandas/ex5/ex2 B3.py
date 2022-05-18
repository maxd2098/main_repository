from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

arr = []
code = soup.find_all('code')
for string in code:
    arr.append(string.text)
    #print(string.text)
#print(arr)
words_dict = dict()
for word in arr:
    if word in words_dict:
        words_dict[word] = words_dict[word] + 1
    else:
        words_dict[word] = 1
#print(words_dict, '\n\n')
words_dict = list(words_dict.items())
words_dict.sort(key=lambda x: x[1], reverse=True)
#for i in words_dict:
    #print(i)
#print('\n\n')
arr = []
for i in words_dict:
    if i[1]>2:
        arr.append(i[0])
        #print(i[0], end=' ')
arr.sort()
print(*arr, sep=' ')
