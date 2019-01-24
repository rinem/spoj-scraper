from bs4 import BeautifulSoup
import requests
url = 'https://www.spoj.com/problems/classical/sort=6'
res = requests.get(url, timeout = 5)
soup = BeautifulSoup(res.content, "html.parser")