import os
import time
from fileinput import filename

import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html

from selenium.webdriver import Chrome
webdriver = "D:\Browserdriver\chromedriver"
driver = Chrome(webdriver)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

...

# wait = WebDriverWait(driver, 120)
# element = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='081xxxxxxxx']")))
# element.send_keys('08100000000')


USERNAME = "***"
PASSWORD = "*****"

login_url = "https://yocket.in/account/login"
URL = "https://yocket.in/applications-admits-rejects/124-state-university-of-new-york-at-buffalo/2?page=2"
#https://www.deathbycaptcha.com/user/login--for captcha bypass

driver.get (login_url)
u = driver.find_element_by_name("email").send_keys(USERNAME)
driver.find_element_by_class_name("mt-4").click()
time.sleep(2)
p = driver.find_element_by_xpath("//input[@placeholder='********']").send_keys(PASSWORD)
driver.find_element_by_class_name("mt-4").click()

cookies = driver.get_cookies()

s = requests.Session()
for cookie in cookies:
    s.cookies.set(cookie['name'], cookie['value'])
    
        header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        'Content-Type': 'text/html',
    }
