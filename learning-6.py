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

#%%
def memo(f):
    cache = {}
    def _f(*a):
        try:
            return cache[a]
        except KeyError:
            cache[a] = f(*a)
            return cache[a]
    return _f

@memo
def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n-1) + fib1(n-2)

#%%
fib1(5005)


#%%
@memo
def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    n1 = 0
    n2 = 1
    c = 1
    for i in range(n-1):
        c = n2 + n1
        n1 = n2
        n2 = c
    return c


#%%
fib2(8500)

#%%
