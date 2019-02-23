# Chapter 04 - Unit 07 - email check using regex
import re

email = input()
print('WRONG' if re.search(r'^\w+@\w+\.\w+$', email.strip()) == None else 'OK')
