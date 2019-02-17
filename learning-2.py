
#%%
import random
r1 = random.random()
r2 = random.randint(1, 100)
print(r1)
print(r2)


#%%
def calc(a, b):
    if (a > 10):
        return 'Error! "a" is too much big.'
    else:
        s = a + b
        return s
    
n1 = int(input("Give me the first one: "))
n2 = int(input("Now enter the second one: "))
print(calc(n1, n2))


#%%
name = input('Give me a name (end to end): ')
while name != 'end':
    print('Hello', name)
    name = input('Give me another name (end to end): ')


#%%
for i in range(1, 10):
    print(i)


#%%
for i in range(1, 10):
    print(i)
    i = i + 3
    print ('new i: ', i)


#%%
myFamily = ['Mostafa', 'Toktam', 'Ali', 'Hosein', 'Mahdi']
for one in myFamily:
    print('Hello', one)


#%%
import random

answer = random.randint(1, 99)
correct = False

c = 1
guess = int(input('Guess No. ' + str(c) + ' - What\'s your guess? '))

while guess != answer and c < 10:
    if guess > answer:
        print('Answer\'s smaller.')
    else:
        print('Answer\'s bigger.')
    c += 1
    guess = int(input('Guess No. ' + str(c) + ' - What\'s your next guess? '))
    

if c < 10:
    print("Wow! You did it. :)")
else:
    print("You're out of guesses. :(")


#%%
import random

bigger = 'b'
smaller = 's'
correct = 'c'

c = 1
minimum = 1
maximum = 100
guess = int(maximum / 2)
result = input('My guess is ' + str(guess) + '. Is your number (b)igger or (s)maller? Or my guess is (c)orrect? ')
while result != 'c' and c < 10:
    if result == 'b':
        minimum = guess
    elif result == 's':
        maximum = guess
    guess = minimum + int((maximum - minimum) / 2)
    c += 1
    result = input('My guess is ' + str(guess) + '. Is your number (b)igger or (s)maller? Or my guess is (c)orrect? ')

if c < 10:
    print("Yay! I did it :)")
else:
    print("I'll try better next time...")


