from bs4 import BeautifulSoup
import requests

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

GOOGLE_IMAGE = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

print("enter query: ")
query = input()

if not query:
    print("query is invalid!")
    exit(1)

URL = GOOGLE_IMAGE + query
print(URL)

resp = requests.get(URL)
soup = BeautifulSoup(resp.text)

print(soup.title.name)

anchors = soup.find_all('a')

print("number of anchor tags : %d" % len(anchors))

for a in anchors:
    print(a.get("href"))
    print()

print("---end---")