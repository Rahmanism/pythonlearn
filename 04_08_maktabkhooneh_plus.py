# Chapter 04 - Unit 08 - maktabkhooneh_plus
from bs4 import BeautifulSoup
import requests

r = requests.get('https://maktabkhooneh.org/plus/')
soup = BeautifulSoup(r.text, 'html.parser')
courses = soup.find_all('div', {'class':'course-name'})

maktabxune_courses = list()
for course in courses:
    children = course.findChildren('span', {'id':'org'})
    if children[0].text.strip() == 'مکتب‌خونه':
        name_span = course.findChildren('span', {'id':'name'})
        name = name_span[0].findChildren('a')[0].text.strip()
        maktabxune_courses.append(name)

for course in maktabxune_courses:
    print(course)
