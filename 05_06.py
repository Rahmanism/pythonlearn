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

newData = [[175, 88, 42], [168,60, 39]]
answer = clf.predict(newData)
print(answer)
