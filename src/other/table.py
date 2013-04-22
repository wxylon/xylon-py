# -*- coding: utf-8 -*-
#coding=utf8
##http://www.oschina.net/code/snippet_698945_20000
"""
print "\n".join(["\t".join("%d*%d=%d" % (a, b, a*b) for a in range(1, 10) for b in range(1, a+1))])

for i in range(1,10):
    for j in range(1, i+1):
        #print ('{}*{}={:<2}'.format(i, j, i*j), end=' ')
        print("%d*%d=%d" % (i, j, i*j))
    print "\n"
"""
print ''.join(["%s×%s=%s%s" % (a, b, a * b, ['\t','\n'][a == b]) for a in range(1, 10) for b in range(1, a+1)])

print [1, 3][1==2], [1, 3][2==2]
##1 3


