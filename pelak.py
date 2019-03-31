import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('http://saten.ir/124471/%D8%B4%D9%85%D8%A7%D8%B1%D9%87-%D9%BE%D9%84%D8%A7%DA%A9-%D9%85%D8%A7%D8%B4%DB%8C%D9%86-%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C-%D9%85%D8%AE%D8%AA%D9%84%D9%81-%D8%A7%D8%B3%D8%AA%D8%A7%D9%86%D9%87%D8%A7/', headers={'User-Agent': 'Mozilla/5.0', 'Content-type': 'text/plain; charset=utf-8'})
soup = BeautifulSoup(page.text, 'html.parser')

def write_csv(data):
    file = open("pelak.txt", "a", encoding='utf-8')
    for d in data:
        file.write(d + ';')
    file.write('\n')
    file.close()

tables = soup.find_all('table', attrs={'class':'wikitable'})
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        row_data = []
        cols = row.find_all('td')
        if len(cols)==3:
            for col in cols:
                p = col.find('p')
                if p:
                    row_data.append(p.text.strip())
        write_csv(row_data)
