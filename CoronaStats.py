import time

from pandas import ExcelWriter
import smtplib
import urllib.request
from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd
import os
from openpyxl import Workbook

main_path = '/Users/gn377164/Desktop'
os.chdir(main_path)
os.environ["LANG"] = "en_US.UTF-8"


original_html = 'https://worldometers.info/coronavirus/'
urlpage = str(original_html)
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
page = requests.get(urlpage, headers=header).text
soup = BeautifulSoup(page, 'html.parser')
table = soup.find("table", {"id":"main_table_countries_today"})

tr_table = table.tbody.find_all("tr")
table_length = tr_table.__len__()
t_headers = []

table_data = []
data = {}
td_table = []
i = 0;
t_row = {}
rows = []
for tr in soup.select('tr'):
    rows.append([td.get_text(strip=True) for td in tr.select('th, td')])
rows = [*zip(*rows)]    # transpose values
df = pd.DataFrame()

for row in rows:
    # print(''.join(r'{: <25}'.format(d) for d in row))
    # df = df.append(pd.DataFrame(row))
    df[row[0]] = row
# df.drop(df.index[:1])
df=df.tail(-1)
df=df.head(202)
print(df)
result_path = '/Users/gn377164/Desktop'
time1 = time.strftime("%m%d-%H%M")
folder_name = "coronaStats" + time1
writer = ExcelWriter(folder_name + '.xlsx')
df.to_excel(writer, index=False)
writer.save()





