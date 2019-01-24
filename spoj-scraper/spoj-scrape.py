from bs4 import BeautifulSoup
import requests
# url = 'https://www.spoj.com/problems/AIBOHP/'
url = 'https://www.spoj.com/problems/AE00/'
res = requests.get(url, timeout = 5)
soup = BeautifulSoup(res.content, "html.parser")
data = soup.find('div', {'id': 'problem-body'})
img = data.find('img')
tag = soup.find('div', {'id': 'problem-tags'})
heading = soup.find('h2', {'id' : 'problem-name'})
print(heading.text)
print(tag.text)
print(data.text)
print(img['src'])