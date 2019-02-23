# Chapter 04
import requests

try:
    print('before request')
    r = requests.get('http://google.com')
    print(r)
except:
    print('test')