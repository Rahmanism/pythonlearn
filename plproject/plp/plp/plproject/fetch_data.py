from bs4 import BeautifulSoup
import requests

# It should fetch data from a website!
def fetch():
    r = requests.get('https://bama.ir/car')
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find('title')
    return title.text

