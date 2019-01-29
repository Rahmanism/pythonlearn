# Chapter 01 - Unit 06 - Movie genres statistics

"""
Example:

4
hossein Horror Romance Comedy
mohsen Horror Action Comedy
mina Adventure Action History
sajjad Romance History Action
"""

number_of_people = int(input())
data_list = list()

for i in range(number_of_people):
    data_list.append(input().split())

numbers_list = dict()
for i in range(number_of_people):
    for j in range(1, 3):
        numbers_list[data_list[i][j]] = numbers_list.get(
            data_list[i][j], 0) + 1

#numbers_list = sorted(numbers_list.iteritems(), key=lambda (k, v): (v, k), reverse=True)

#numbers_list.sort(key=lambda x: x[1], reverse=True)
sorted_1st = list()
for k, v in sorted(numbers_list.items(), key=lambda item:(item[1], item[0]), reverse=True):
    sorted_1st.append({k: v})
    #print("%s : %s" % (k, v))

sorting = list()
n = len(sorting)
for i in range(len(list(numbers_list.keys()))):
    sorting.append(i)

print("1:--------")
for i in range(n):
    # for j in range(n-i-1):
        print(i, j)
        print (sorted_1st[i])

print("--------")
print(sorted_1st)
