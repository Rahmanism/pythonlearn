
#%%
f = open('scores.txt')
counter = 0
for line in f:
    counter += 1
    print('%i> %s' % (counter, line.strip()))


#%%
f = open('scores.txt')
counter = 0
sum = 0
for line in f:
    counter += 1
    this_number = line.strip()
    sum += float(this_number)
average = float(sum / counter)
print('Average: %.2f' % average)
f_out = open('average.txt', 'w')
f_out.write(str(average))
f_out.close()


#%%
import csv
from statistics import mean

with open('grades.csv', 'r') as f:
    reader = csv.reader(f)
    grades = dict()
    for row in reader:
        these_grades = list()
        for grade in row[1:]:
            these_grades.append(int(grade))
            grades[row[0]] = these_grades
        
    print('Averages:--------------')
    for item in grades:        
        print('%12s => %.2f' %(item, mean(grades[item])))


