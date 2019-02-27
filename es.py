# test request for estekhare
import sys
import requests
from bs4 import BeautifulSoup

r = requests.get('http://estekhare.net/index2.php')
soup = BeautifulSoup(r.text, 'html.parser')
resultContainer  = soup.find('div', {'id':'newboxes1'})
result = resultContainer.find('h1')
resultComment = resultContainer.find('h2')
address = resultContainer.find('h6')
print(result.text)
if len(sys.argv) > 1 and sys.argv[1] == '-c':
    print(resultComment.text.replace('\n', ''))
    print(address.text)
input()
