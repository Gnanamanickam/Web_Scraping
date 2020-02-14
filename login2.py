import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html

USERNAME = ""
PASSWORD = ""

login_url = "https://yocket.in/account/login"
URL = "https://yocket.in/applications-admits-rejects/124-state-university-of-new-york-at-buffalo/2?page=2"

def main():
    session_requests = requests.session()
    result = session_requests.get(login_url)
    tree = html.fromstring(result.text)
    hidden_inputs = tree.xpath(r'//form//input[@type="hidden"]')
    payload = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
    payload['email'] = USERNAME
    payload['password'] = PASSWORD

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Content-Type': 'text/html',
    }

    result1 = session_requests.post(login_url, data = payload, headers = header)
    result = session_requests.get(URL)
    print(result.text)
    # print('Campus' in result.text)



if __name__ == '__main__':
    main()
