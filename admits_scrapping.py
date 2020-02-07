import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import Request,urlopen
from pandas import ExcelWriter
import os

main_path = 'D:\PycharmProjects\YocketAdmits'
os.chdir(main_path)

#driver = webdriver.Chrome("D:\Programs\chromedriver")

#college_list = ['124-state-university-of-new-york-at-buffalo', '360-university-of-north-carolina-at-charlotte',
              #  '305-university-of-illinois-at-chicago', '153-university-of-cincinnati']
college_list = ['124-state-university-of-new-york-at-buffalo']
college_summary = pd.DataFrame()
status = 2
#print(college_summary)
for college_index in range(0, len(college_list)):
    college_name = college_list[college_index]

    for page_no in range(1,12):

        original_html = 'https://yocket.in/applications-admits-rejects/'+ college_name + '/' + str(status) + '?page=' + str(page_no)
        #driver.get(original_html)
        urlpage = str(original_html)
        #print(urlpage)
        page = Request(urlpage, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(page).read()
        # with urllib.request.urlopen(urlpage) as response:
        #     html = response.read()
        #     print(html)

        soup = BeautifulSoup(webpage, 'html.parser')
        # print(soup)
        all_gre = []
        all_gpa = []
        all_name = []
        work_exp = []
        scores = soup.find_all('div', attrs={'class': 'row text-center'})
        names = soup.find_all('div', attrs={'class' : 'col-sm-9'})
        for name_list in range(0, len(names)):
            name = str(names[name_list].text)
            name = name.strip()
            all_name.append(name)

        print(all_name)










