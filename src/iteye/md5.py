#-*-coding:utf-8-*- 

#import md5
import hashlib

str = "this is a test"
#m1 = md5.new()
#m1.update(str)

#dest1 = m1.hexdigest()

m2 = hashlib.md5()
m2.update(str)

dest2 = m2.hexdigest()

print 'source string: ', str   
#print 'destination string1: ', dest1   
print 'destination string2: ', dest2   