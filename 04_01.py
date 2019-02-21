# Chapter 04

import re

s = 'salam mostafa. salam mahdi. Salam toktam. Salam Soleiman.'
result = re.search(r'salam', s)
print(result.span())
print(result.start())

em = 'mostafa@gmail.com'

def check_email(e):
    if re.search(r'.+@.+\..{2,8}', e) == None:
        print('not an email')
    else:
        print('it\'s an email')

check_email(em)
check_email(input('enter your email: '))

pr_line = 'price of 4 gln of oil is 120$'
result = re.findall(r'price of (\d+) gln of oil is (\d+)\$', pr_line)
print(result)

gln, price = result[0]
print(gln)
print(price)

pr_line = '''price of 4 gln of oil is 120$ on 9/3
price of 4 gln of oil is 138$ on 9/4
price of 4 gln of oil is 118$ on 9/5'''
result = re.findall(r'price of (\d+) gln of oil is (\d+)\$ on (.*)', pr_line)
print(result)

print('gln\tprice\tdate')
print('-----------------------')
for gln, price, date in result:
    print('%s\t%s\t%s' % (gln, price, date))

s = 'salam mostafa. salam mahdi. Salam toktam. Salam Soleiman.'
print(re.sub(r'[sS]alam', 'bye', s))
print(re.sub(r'price of (\d+) gln of oil is (\d+)\$ on (.*)', '\g<3>,\g<1>,\g<2>', pr_line))
