# read data from csv
import csv
from statistics import mean

f = open('grades.csv')
reader = csv.reader(f)
grades = dict()
for row in reader:
    these_grades = list()
    for grade in row[1:]:
        these_grades.append(int(grade))
    grades[row[0]] = these_grades

print('Averages:................')
for item in grades:
    print('%12s => %.2f' % (item, mean(grades[item])))
