# test bubble sort

a = [1,2,8,5,4,3]
print(a)

n = len(a)

for i in range(n):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
