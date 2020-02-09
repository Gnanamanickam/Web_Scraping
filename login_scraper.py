import requests
from lxml import html

USERNAME = "gnanamanickam1995@gmail.com"
PASSWORD = "*******"

LOGIN_URL = ""
URL = ""

def main():
    session_requests = requests.session()
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    payload = {
        "username": USERNAME,
        "password": PASSWORD,
        "csrfmiddlewaretoken": authenticity_token
    }

    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    print(bucket_names)

if __name__ == '__main__':
    main()