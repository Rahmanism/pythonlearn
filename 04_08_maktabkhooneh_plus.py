# Chapter 04 - Unit 08 - maktabkhooneh_plus
from bs4 import BeautifulSoup
import requests

r = requests.get('https://maktabkhooneh.org/plus/')
soup = BeautifulSoup(r.text, 'html.parser')
courses = soup.find_all('div')

for c in courses:
    # print(f.attrs.get('id'))
    if c.attrs.get('class') == 'course-name':
        spans = c.find_all('span')
        for s in spans:
            print(s)
            if s.attrs.get('id') == 'name':
                print(s.text.strip())
            if s.attrs.get('id') == 'org':
                print('it\'s maktabkhooneh')
