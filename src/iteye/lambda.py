#-*-coding:utf-8-*- 
# lambda.py

def fun1(n):
    return lambda m: m**n

def fun2(m, n):
    return m + n

f1 = lambda x, y, z: x * 2 + y + z
print  f1(1, 2, 3)

f2 = fun1(2)
print f2(4)

print fun2(3, (lambda x: x+1)(2))


