# -*- coding: utf-8 -*-
#coding=utf-8


'''
int()是Python的一个内部函数,可以将一个数转化为整数
这里有两个地方要注意：
1）12要以字符串的形式进行输入，如果是带参数base的话
2）这里并不是将12转换为16进制的数，而是说12就是一个16进制的数，int()函数将其用十进制数表示
'''
print int(1)
print int(12.0)  
print int('12',16)  
print int('0xa',16)
print int('10',8)