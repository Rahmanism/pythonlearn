# Chapter 01 - Unit 06 - Movie genres statistics

"""
Example:

4
hossein Horror Romance Comedy
mohsen Horror Action Comedy
mina Adventure Action History
sajjad Romance History Action

4
h Horror Romance History
h Horror Action
h Adventure Action
h Romance History
"""

base_genres= ['Action', 'Adventure', 'Comedy', 'History', 'Horror', 'Romance']
number_of_people = int(input())
data_list = list()

for i in range(number_of_people):
    data_list.append(input().split())

numbers_list = dict()
for i in range(number_of_people):
    for j in range(1, len(data_list[i])):
        numbers_list[data_list[i][j]] = numbers_list.get(
            data_list[i][j], 0) + 1

for i in range(len(base_genres)):
        numbers_list[base_genres[i]] = numbers_list.get(base_genres[i], 0)

sorted_1st = list()
sorted_keys = list()
sorted_values = list()
for k, v in sorted(numbers_list.items(), key=lambda item: (item[1], item[0]), reverse=True):
    sorted_1st.append({k: v})
    sorted_keys.append(k)
    sorted_values.append(v)
    #print("%s : %s" % (k, v))

sorting = list(range(6))
n = len(sorted_1st)

for i in range(n):
    for j in range(n-i-1):
        if sorted_values[j] == sorted_values[j+1]:
            if sorted_keys[j] > sorted_keys[j+1]:
                sorted_values[j], sorted_values[j+1] = sorted_values[j+1], sorted_values[j]
                sorted_keys[j], sorted_keys[j+1] = sorted_keys[j+1], sorted_keys[j]
                sorting[j], sorting[j+1] = sorting[j+1], sorting[j]

for i in range(n):
    print('%s : %i' % (sorted_keys[i], sorted_values[i]))
