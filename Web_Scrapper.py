import profile
import requests
from bs4 import BeautifulSoup

github_user = input('Input The Target GitHub user please:')
url = 'https://github.com/'+github_user
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
profile_image = soup.find('img',{'alt':'Avatar'})['src']
print(profile_image)