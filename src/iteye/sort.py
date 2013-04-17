#-*-coding:utf-8-*- 
# sort.py

def splitStr():
    print "######################################"

# 演示对字符串列表进行排序
simpleList = ["3.world", "2.hello", "1.python"]
print simpleList

simpleList.sort()
print simpleList

splitStr()

# 演示对整型数进行排序
simpleList = [3, 2, 9]
simpleList.sort()
print simpleList

splitStr()

simpleDic = {"t1":"测试2", "t2":"测试1"}
print simpleDic
print sorted(simpleDic.items(), key = lambda x: x[0])
print sorted(simpleDic.items(), key = lambda x: x[1])

splitStr()

# 这个类用来演示如何对自定义对象进行排序  
class Sortobj:
    a = 0
    b = ""
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def printab(self):
        print ("a = %s, b = %s" %(self.a, self.b))


simpleObj = [Sortobj(1, "c"), Sortobj(5, "a"), Sortobj(4, "n"), Sortobj(2, "h"), Sortobj(3, "i")]
print simpleObj;
for obj in simpleObj:
    obj.printab()
    
splitStr()
simpleObj.sort(lambda x,y: cmp(x.a, y.a))
for obj in simpleObj:
    obj.printab()
    
splitStr()
simpleObj.sort(lambda x,y: cmp(x.b, y.b))  
for obj in simpleObj:  
    obj.printab()  


