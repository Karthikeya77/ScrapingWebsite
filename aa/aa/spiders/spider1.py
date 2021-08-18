import requests
import pandas as pd
import regex
from bs4 import BeautifulSoup
List=[]
name = 'goa'

def function():
    x = 0
    for i in c:
        l = i.text.strip()
        if regex.match('^Timings.*', l):
            d = l.strip('\nTimings : ')
            # print(d)
            p = {
                'Place': title.text,
                'city': name,
                'Timings': d,
            }
            List.append(p)
        else:
            x = x + 1
            if (x == length):
                r = {
                    'Place': title.text,
                    'city': name,
                    'Timings': 'Null',
                }
                List.append(r)

URL = f'https://www.holidify.com/places/{name}/sightseeing-and-things-to-do.html'
page1 = requests.get(URL)
soup1 = BeautifulSoup(page1.text, 'html.parser')
data1 = soup1.find_all('div',{'class':'card content-card'})
for item1 in data1:
    title = item1.find('h3',      {'class': 'card-heading'})
    if (title != None):
        # print(title.text)
        link = item1.find('a', {'class': ''})['href']
        page2 = requests.get(link)
        soup2 = BeautifulSoup(page2.text, 'html.parser')
        data2 = soup2.find('div', {'class': 'row no-gutters objective-information'})
        try:
            c = data2.find_all('div', {'class': 'col-12'})
            length = len(c)
            function()
        except:
            q = {
                'Place': title.text,
                'city':name,
                'Timings': 'Null',
            }
            List.append(q)

df=pd.DataFrame(List)
df.to_excel('goa.xlsx', index=False)