# Chapter 02 - Unit 11 - health

"""
Example:
Input:
5
16 17 15 16 17
180 175 172 170 165
67 72 59 62 55
5
15 17 16 15 16
166 156 168 170 162
45 52 56 58 47

Output:
16.2
172.4
63.0
15.8
164.4
51.6
A
"""

class Student:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

class Class:
    def __init__(self, name):
        self.name = name
        self.students = list()
    def age_average(self):
        s = 0
        for i in self.students:
            s += i.age
        return float(s / len(self.students))
    def height_average(self):
        s = 0
        for i in self.students:
            s += i.height
        return float(s / len(self.students))
    def weight_average(self):
        s = 0
        for i in self.students:
            s += i.weight
        return float(s / len(self.students))
    def info(self):
        print(self.age_average())
        print(self.height_average())
        print(self.weight_average())

def set_class(n, c):
    ages = input()
    heights = input()
    weights = input()

    ages = ages.split()
    heights = heights.split()
    weights = weights.split()

    for i in range(n):
        a = int(ages[i])
        h = int(heights[i])
        w = int(weights[i])
        std = Student(a, h, w)
        c.students.append(std)

n = int(input())
A = Class('A')
set_class(n, A)

n = int(input())
B = Class('B')
set_class(n, B)

A.info()
B.info()
ah = A.height_average()
aw = A.weight_average()
bh = B.height_average()
bw = B.weight_average()
if ah > bh:
    print(A.name)
elif ah == bh:
    if aw < bw:
        print(A.name)
    elif aw == bw:
        print('Same')
    else:
        print(B.name)
else:
    print(B.name)
