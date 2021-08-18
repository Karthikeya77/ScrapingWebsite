import requests
import pandas as pd
from bs4 import BeautifulSoup

df = pd.read_excel(r"C:\Users\karth\OneDrive\Desktop\CAPSTONE\HotelsSouthIndia - Copy.xlsx")

urls1 = df['pageurl'].values
urls = urls1.tolist()
a = []
# print(urls)
# page = requests.get('https://www.goibibo.com/hotels/detail/Anantapur/hn/3996681253492714114/1287616541988898049/na/hq/')
# soup = BeautifulSoup(page.text, 'html.parser')
# data1 = soup.find('div', {'class': 'width100 fl'})
# data = data1.find('h1' ,{'class':'greyDr ico30 fl width100'})
# print(data.text)
c = []
for url in urls:
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        data1 = soup.find('div', {'class': 'width100 fl'})
        data = data1.find('h1', {'class': 'greyDr ico30 fl width100'})
        c.append(data.text)
    except:
        c.append('Hotel')
        a.append(url)

print(c)
