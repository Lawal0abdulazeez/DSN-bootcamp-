'''s= "django"
print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[4:])
print(s[::-1])

l = [3,7,[1,4,'hello']]
l[2][2]= 'Goodbye'
print(l)

d1= {'simple_key':'hello'}
d2= {'k1':{'k2':'hello'}}
d3= {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1])

a =  4

name ="Sammy"

print("Hello my dog's name is {} and he is {} years old".format(name,a))


def arrayCheck(nums):
    if nums[1:4] == [1,2,3]:
        print(True)
    else:
        print(False)

arrayCheck([1,1,2,4,1])


def stringBits(str):
    print(str[::2])

stringBits('Hello')
stringBits('Hi')
stringBits('Heeololeo')

def end_other(a,b):
    a=a.lower()
    b=b.lower()
    if a[-3:] == b[-3:]:
        print(True)
    else:
        print(False)

end_other('Hiabc','abc')
end_other('Abc', 'HiaBc')
end_other('abc', 'abXabc')
a='kakak'

def doubleChar(str):
    for i in str:
        str = str.replace(i, i*2)
    print(str)


doubleChar('The')
doubleChar('AAbb')
doubleChar('Hi-There')



def fix_teen(n):
    if n in range(11,20):
        n =0
        return n
    else:
        n = n
        return n
    print(n)
fix_teen(13)

def no_teen_sum(a,b,c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    print(a+b+c)

no_teen_sum(1,2,3)
no_teen_sum(2,13,1)
no_teen_sum(2,1,14)

print('hello')
def count_evens(a):
    i=0
    for x in a:
        if x%2 == 0:
            i+=1

    print(i)


count_evens([2,1,4,6,3,7,8])

import random
print('Welcome Code Breaker! lets see if you can guess my 3 digit number!')
gen=random.randrange(100,999)
print(gen)
print("Code has  been generated, please guess a 3 digit number")
guessed = input('What is your guess?')
print(guessed)
def match():
    while str(guessed) == str(gen):
            if i in str(guessed):
                if str(gen).index(i) != str(guessed).index(i):
                    print('closed')
                elif str(gen).index(i) == str(guessed).index(i):
                    print('match')
            elif i not in str(guessed):
                print('nope')


print('Here is the result of your guess')
match()
'''
import pyreadr
print("Done")
