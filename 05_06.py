# Chapter 5 - Unit 6 - Machine Learning
from sklearn import tree
import csv

x = []
y = []
with open('05_06_data.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        x.append(line[0:3])
        y.append(line[3])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

h = int(input('Height? '))
w = int(input('Weight? '))
s = int(input('Shoe size? '))
newData = [[h, w, s]]
answer = clf.predict(newData)
answer = 'male' if answer[0] == 'm' else 'female'
print('\nYou probably are %s.' % answer)
