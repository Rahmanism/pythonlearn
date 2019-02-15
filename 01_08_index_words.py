# Chapter 01 - Unit 08 - Count of words starting with capital.

"""
Example:
Input:
The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship.This video was captured by one of our heroes who wishes peace.

Output:
2:Persian
3:League
15:Iran
17:Persian
18:League
"""

p = input()

words = p.split()
indices = list()
previous_was_end_of_sentence = False
for i in range(1, len(words)):
    if previous_was_end_of_sentence:
        previous_was_end_of_sentence = False
        continue
    if words[i][-1] == '.':
        previous_was_end_of_sentence = True
        words[i] = words[i][:-1]
    if words[i][-1] == ',':
        words[i] = words[i][:-1]
    if ord(words[i][0]) >= 65 and ord(words[i][0]) <= 90:
        indices.append((i+1,words[i]))

for i in range(len(indices)):
    print('%i:%s' % (indices[i][0], indices[i][1]))
