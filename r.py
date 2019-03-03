import random

c = True
while c:
   r = random.randint(299, 799)
   print(r)
   uc = input('continue (Y/n)? ') 
   if uc.lower() == 'n':
       c = False

