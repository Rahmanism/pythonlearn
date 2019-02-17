# Chapter 02 

# lambda functions:
myfunc = lambda x: x * 2
print(myfunc(3))

a = [(3,4), (7,1), (5,9), (2,2)]
a.sort()
print(a)

a = [(3,4), (7,1), (5,9), (2,2)]
a.sort(key = lambda x: x[1])
print(a)

# double elements using map and lambda
a = [1, 3, 4, 0.5]
print(list(map(lambda x: x*2, a)))

# say big or small using map and lambda
a = [10, 11, 25, 7, 9, 100, 6]
print(list(map(lambda x: 'big' if x > 10 else 'small', a)))

# filter even numbers using filter and lambda
a = [10, 11, 25, 7, 9, 100, 6]
print(list(filter(lambda x: x%2 == 0, a)))

# quiz
array = [(1,4,5), (3,2,7), (8,3,6), (9,2,3)]
array.sort(key = lambda a:a[2])
print(array)

mylist = [2,3,5,8,11,14,17,102,44]
print(list(map(lambda x:'Yes' if  x%2==1 else 'No',mylist)))

mylist = [2,15,26,8,11,14,17,102,44]
map_list = map(lambda x:x%10,mylist)
filter_list = list(filter(lambda x: x<=4,map_list))
print(filter_list)

mylist = ['yellow', 'red', 'blue','red','yellow','red','blue','purple']
mylist.sort()
mylist = list(map(lambda x: 'color' if x=='red' else x,mylist))
output = list(filter(lambda x: x=='red',mylist))
print(output)

###########################################
print("#######generators")
# generator functions yeild
def firstn():
    return (1,2,3)

print(firstn())

def firstn2():
    yield 1
    yield 2
    yield 3

for i in firstn2():
    print(i)

def firstn3(n):
    num = 0
    while (num < n):
        yield num
        num += 1

for i in firstn3(4):
    print(i)

