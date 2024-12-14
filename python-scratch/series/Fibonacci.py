'''
Created on 2013. 3. 21.

@author: starblood
'''

def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)