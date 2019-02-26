import random

for i in range(100):
    h = random.randint(50,220)
    w = random.randint(30,150)
    k = 0
    g = 'm'
    if h < 175:
        k = random.randint(20,40)
    else:
        k = random.randint(38, 50)
    if h > 175 and w > 65:
        g = 'm'
    else:
        g = random.choice(['f', 'm'])
    print('"%i","%i","%i","%s"' % (h,w,k,g))
