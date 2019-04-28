#%%
import time

#%%
def t1(n = 10):
    time.sleep(2)
    return n * 100

def gen1():
    n = 0
    while n < 100:
        yield t1(n)
        n += 1

b = gen1()

#%%
next(b)

#%%
r = range(10)
list(r)
