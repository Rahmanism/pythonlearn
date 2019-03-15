# test request for estekhare
import sys
import requests
from bs4 import BeautifulSoup

def estekhare(show_comment):
	r = requests.get('http://estekhare.net/index2.php')
	soup = BeautifulSoup(r.text, 'html.parser')
	resultContainer  = soup.find('div', {'id':'newboxes1'})
	result = resultContainer.find('h1')
	resultComment = resultContainer.find('h2')
	address = resultContainer.find('h6')
	ret = result.text
	if show_comment:
		ret += '\n%s' % resultComment.text.replace('\n', '')
		ret += '\n%s' % address.text
	return ret

again = True
while again:
	showComment = len(sys.argv) > 1 and sys.argv[1] == '-c'
	print(estekhare(showComment))
	again_input = input('\nAgain (y/N)? ')
	again = again_input.lower() == 'y'
	print('\n')
	
print('bye')
