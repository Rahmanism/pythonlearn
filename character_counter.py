# We want to know how many from each character is in the following string.
myString = 'This is just a test text for learning dictionary in python.'

counter  = dict()

for letter in myString:
    counter[letter] = counter.get(letter, 0) + 1
    # the above line does the work of next four lines.
    #if letter in counter:
    #    counter[letter] += 1
    #else:
    #    counter[letter] = 1

keys = list(counter.key())
keys.sort()

for i in keys:
    print(i, ': ', end='')
    for j in range(counter[i]):
        print('+', end='')
    print('> %d' % counter[i])

