
#%%
a = 'Hello'
len(a)
a[4]


#%%
for i in range(0, len(a)):
    print(i, a[i])


#%%
for l in a:
    print(l)


#%%
c = 0
for l in a:
    print(c, l)
    c += 1


#%%
c = 0
for l in a:
    if l == 'l':
        c += 1
print('There are ' + str(c) + ' ls in the string.')


#%%
print (a[:])
print (a[:3])
print (a[3:])
print (a[-1])
print (a[-3:-1])


#%%
a = 'HE' + a[2:]
print(a)


#%%
'll' in a
'e' in a
'E' in a
'HEllo' == a
'Hello' == a
'a' < 'b'
'A' < 'a'


#%%
a.upper()
'Mostafa'.upper()
dir(a)
help(str.count)


#%%
print(a)
print(a.count('l'))
print(a.count('l', 0, 3))


#%%
print(a.find('l'))
print(a.find('l', 3))
print('  sdfdf  '.strip())
print(a.lower().startswith('h'))


#%%
name = 'Mostafa'
print('%s, %s' % (a, name) )


#%%
l = [5, 4, -1, 'Mostafa']
print(l[1])
print(l[3:])
print(l[-2])


#%%
l2 = [l, 4.5, 'Ali']
print(l2[-1])
print(l2[0])
print(l2[0][1])
for i in l2:
    print(i)
print(len(l2))
l3 = [l, 5, 'Ali', ['Hosein', 'Mahdi']]
for i in range(0, len(l3)):
    print(i, l3[i])
l2[1] = 4.6
print(l2)


#%%
l4 = l2 + l3
print(l4)
print(l2 * 2)

print(type(l4))
dir(l4)
help(l4.append)

l4.append('Rahmani')
print(l4)

l4[-2].append('Ali')
print(l4)

help(list.extend)
help(list.remove)
# l.remove('Mostafa')
print(l)
l.sort()
print(l)
print(l2)
print(l4)
# del l2[1]
print(l2)
# print(l3)
# l3[-1].pop()
# l3[-1].pop()
print(l3)
print(l4)


#%%
n = [4, 8, 2, -1, 5]
print(max(n))
print(min(n))
print(sum(n))
print(sum(n) / len(n))


#%%
phrase = 'this is a phrase'
phrase_words = phrase.split()
print(phrase_words)
phrase_words_joined = '_'.join(phrase_words)
print(phrase_words_joined)


#%%
a = 'test'
b = 'test'
print(a == b)
print(a is b)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)
print(list1 is list2)

list3 = list1
print(list1 is list3)


#%%
d1 = dict()
print(d1)
d1['hi'] = 'سلام'
d1['me'] = 'من'
d1['you'] = 'تو'
print(d1)
print(d1['me'])
d1[2] = '۲'
print(d1[2])
print(d1)
d2 = { 1 : 'One', 2 : 'Two', 3 : 'Three' }
print(d2)
print(d2[2])
print(d2.keys())
print(list(d2.values()))
print(1 in d2)
print('me' in d1)


#%%
some_string = 'this string is just to learn about dictionary in python'

counter = dict()

for letter in some_string:
    if letter in counter:
        counter[letter] += 1
    else:
        counter[letter] = 1
        
for item in counter:
    print('%s appeared %s times' % (item, counter[item]))


#%%
print(counter['a'])
print(counter.get('z'))
print(counter.get('z', 0))


#%%
some_string = 'this string is just to learn about dictionary in python'

counter = dict()

for letter in some_string:
    counter[letter] = counter.get(letter, 0) + 1
        
for item in counter:
    print('%s appeared %s times' % (item, counter[item]))


#%%
t = (3, 4, 2, 4)
print(t)
print(t[1])
print(t.count(4))
print(t.index(2))


#%%
a = [1, 2]
x, y = a
print(x, y)
x, y = 6, 8
print(x, y)
x = 3
y = 4
x, y = y, x
print(x, y)

email = 'mymail@gmail.com'
name, domain = email.split('@')
print(name, domain)


#%%
weights = { 'Mostafa' : 95, 'Ali' : 48, 'Hosein' : 42, 'Mahdi' : 27 }
for name, weight in list(weights.items()):
    print('%s weighs %s kg' % (name, weight))


