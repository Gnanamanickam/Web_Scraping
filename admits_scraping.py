import pandas as pd
import time
from bs4 import BeautifulSoup
import scrapy
from urllib.request import Request,urlopen
import requests
from pandas import ExcelWriters
import os
from lxml import html
main_path = 'D:\PycharmProjects\YocketAdmits'
os.chdir(main_path)
os.environ["LANG"] = "en_US.UTF-8"

#from selenium.webdriver import Chrome
# webdriver = "D:\Browserdriver\chromedriver"
# driver = Chrome(webdriver)

#college_list = ['124-state-university-of-new-york-at-buffalo', '360-university-of-north-carolina-at-charlotte',
              #  '305-university-of-illinois-at-chicago', '153-university-of-cincinnati']
login_url = 'https://yocket.in/account/login'
session_requests = requests.session()
result = session_requests.get(login_url)
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='_csrfToken']/@value")))[0]

payload = {
	"username": "gnanamanickam1995@gmail.com",
	"password": "*********",
	"csrfmiddlewaretoken": authenticity_token
}

result = session_requests.post(
	login_url,
	data = payload,
	headers = dict(referer=login_url)
)

college_list = ['124-state-university-of-new-york-at-buffalo']
college_summary = pd.DataFrame()
status = 2
#print(college_summary)
for college_index in range(0, len(college_list)):
    college_name = college_list[college_index]

    for page_no in range(2,3):


        original_html = 'https://yocket.in/applications-admits-rejects/'+ college_name + '/' + str(status) + '?page=' + str(page_no)
        #driver.get(original_html)
        urlpage = str(original_html)
       # print(urlpage)
       #  page = Request.get(urlpage, headers={'User-Agent': 'Mozilla/5.0'}).content();
       #  webpage = urlopen(page).read()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Content-Type': 'text/html',
        }
        webpage = requests.get(urlpage, headers = headers).text
        # webpage = driver.get(urlpage)
        print(webpage)
        # with urllib.request.urlopen(urlpage) as response:
        #     html = response.read()
        #     print(html)

        soup = BeautifulSoup(webpage, 'html.parser')
        print(webpage)
        all_gre = []
        all_gpa = []
        all_name = []



        work_exp = []
        names = soup.find_all('div', attrs={'class': 'col-sm-9'})
        for i in range(0,len(names)):
            name = names[i]
            # print(name)

            # if names['href'].startswith('/players'):
            # if(names.has_attr('href')):
        # names = soup.find_all('div', attrs={'class' : 'col-sm-9'})
        # for name_list in range(0, len(names)):
        #     name = str(names[name_list].text)
        #     name = name.strip()
        #     all_name.append(name)
        #
        # print(all_name)










