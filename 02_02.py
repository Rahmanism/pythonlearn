# Chapter 02 - 02

# OOP

class Person:
    __count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.__count += 1

    def get_name(self):
        return str('Name is %s.' % self.name)

    def __str__(self):
        return str('Name: %s, Age: %i' % (self.name, self.age))

    def birthday(self):
        self.age = self.age + 1
        print('Happy birthday %s!!' % self.name)
    
    def person_count():
        return Person.__count

me = Person('Mostafa', 37)
print(me.get_name())
print(str(me))
me.birthday()
print(me.age)

ali = Person('Ali', 10)
print(str(ali))

print('We have %i persons now.' % Person.person_count())


################# quiz
class maktabkhooneh:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print ("my name is %s and my age is %i" % (self.name,self.age))

 

Maktabkhooneh = maktabkhooneh('maktabkhooneh',7)
Maktabkhooneh.get_name()

########
class university:
    def __init__(student, name, number_of_grade, grade1, grade2, grade3):
        student.name = name
        student.number_of_grade = number_of_grade
        student.grade1 = grade1
        student.grade2 = grade2
        student.grade3 = grade3

    def get_name(student):
        print("Student name is %s" % student.name)
        
    def get_grades(student):
        total_grade = student.grade1+student.grade2+student.grade3
        average = total_grade/student.number_of_grade
        print ("The Average is %i" % average)

Information = university("Hossein",3,16,12,18)
Information.get_name()
Information.get_grades()

############

#color = input()

class Vehicle:
    def __init__(model, name):
        model.name = name

    def get_name(model):
        print("Vehicle name is %s" % model.name)
 
    def get_color(model):
        pass
        # print("Vehicle color is %s" % color) 

Information = Vehicle("Hossein")
Information.get_name()
Information.get_color()


########### Unit 08
print("######################## UNIT 08 ")
class Computer:
    count = 0
    def __init__(self, ram, hard, cpu):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu
        Computer.count += 1

    def value(self):
        return self.ram + self.hard + self.cpu

class Laptop(Computer):
    def value(self):
        return self.ram + self.hard + self.cpu + self.size

pc1 = Computer(12, 2, 4)
print(pc1.value())

laptop1 = Laptop(12,1,4)
laptop1.size = 13
print(laptop1.value())
