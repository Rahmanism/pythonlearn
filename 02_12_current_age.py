# Chapter 02 - Unit 12 - Current Age
from datetime import datetime

"""
Example:
Input:
1995/02/03

Output:
23
"""

class Age:
    def __init__(self, birth_date):
        if (self.check_birth_date(birth_date)):
            self.birth_date = datetime.date(
                datetime.strptime(birth_date, '%Y/%m/%d'))
            self.correctBD = True
        else:
            self.correctBD = False

    def check_birth_date(self, birth_date):
        bds = birth_date.split('/')
        if int(bds[1]) > 12:
            return False
        if int(bds[2]) > 31:
            return False
        return True

    def get_age(self):
        if self.correctBD:
            age_date = datetime.date(datetime.now()) - self.birth_date
            return age_date.days // 365
        else:
            return 'WRONG'

bd = input()
age = Age(bd)
print(age.get_age())
