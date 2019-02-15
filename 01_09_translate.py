# Chapter 01 - Unit 09 - Translation

"""
Example:
Input:
4
man I je ich
kheili very très sehr
alaghemand interested intéressé interessiert 
barnamenevisi programming laprogrammation Programmierung
I am very interested in programming

Output:
man am kheili alaghemand in barnamenevisi
"""

def get_key(d, v):
    """
    d is the dictionary to look in.
    v is the value we search for
    and values are list but v is just an item in a list.
    """
    k = list(d.keys())
    for i in range(len(k)):
        l = d[k[i]]
        if v in l:
            return k[i]
    return v


dict_n = int(input())

dictionary = dict()
for i in range(dict_n):
    w = input()
    w = w.split()
    dictionary[w[0]] = w[1:]

sentence = input()
sentence_words = sentence.split()
translation = list()

for i in range(len(sentence_words)):
    translation.append(get_key(dictionary, sentence_words[i]))

for i in range(len(translation)):
    print(translation[i], end=" ")
