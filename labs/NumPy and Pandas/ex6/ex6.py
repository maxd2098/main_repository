from bs4 import BeautifulSoup
import math

'''xml=open('map2.osm','r',encoding='utf8').read()
soup = BeautifulSoup(xml,'lxml')

#задание 1 
print(len(soup.find_all('node')))

#задание 2
one_tag = 0
not_tag = 0
node_all = soup.find_all('node')
for node in node_all:
    if node.find_all('tag'):
        one_tag += 1
    else:
        not_tag += 1
print(not_tag, one_tag, sep = ' ')

#задание 3
fuel = 0
for node in node_all:
    for tag in node('tag'):
        if tag['k'] == 'amenity' and tag['v'] == 'fuel':
            fuel += 1
print(fuel)

#задание 4
for way in soup.find_all('way'):
    for tag in way('tag'):
        if tag['k'] == 'amenity' and tag['v'] == 'fuel':
            fuel += 1
print(fuel)'''

def getsqr(coordlist):
    baselat = coordlist[0][0]
    baselon = coordlist[0][1]
    degreelen = 111300
    newcoord = []
    for now in coordlist:
        newcoord.append(((now[0] - baselat) * degreelen, (now[1] - baselon) * degreelen * math.sin(baselat)))
        sqr = 0
        for i in range(len(newcoord) - 1):
            sqr += newcoord[i][0] * newcoord[i + 1][1] - newcoord[i + 1][0] * newcoord[i][1]
            sqr += newcoord[-1][0] * newcoord[0][1] - newcoord[0][0] * newcoord[-1][1]
    return abs(sqr)

#задание 5
xml=open('mapcity.osm','r',encoding='utf8').read()
soup = BeautifulSoup(xml,'lxml')
node = soup.find_all('node')
dict_node = {}
for xy in node:
    dict_node[xy['id']] = (float(xy['lat']), float(xy['lon'])) #добавляем координаты в словарь
#print(dict_node, '\n')
dict_way = {}
S = 0
id_S = 0
for way in soup.find_all('way'):
    check = False

    if way('nd')[0] == way('nd')[-1]:
        for tag in way('tag'):
            if tag['k'] == 'building':
                check = True
    if check==True:
        #print('\n', way['id'], sep='')
        arr = []
        for idnum in way('nd'):
            arr.append(dict_node[idnum['ref']])
        #print(arr)
        new_S = getsqr(arr)
        #print(new_S)
        if S < new_S:
            S = new_S
            id_S = way['id']
print(id_S, S)

            
#print(len(dict_way))


















