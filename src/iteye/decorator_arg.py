#-*-coding:utf-8-*- 

# decorator_arg.py   
  
# 修饰函数       
def decorator(fun):       
    def ifun(*args, **kwargs):       
        args = (i+1 for i in args)       
        return fun(*args, **kwargs)       
    return ifun       
  
def decorator1(arg):   
    def _decorator1(fun):   
        def ifun(*args, **kwargs):   
            args = (i+arg for i in args)   
            return fun(*args, **kwargs)   
        return ifun   
    return _decorator1   
  
# 被修饰函数1   
@decorator   
def fun1(x,y,z):       
    return x+y+z       
  
arg = 2   
# 被修饰函数2   
@decorator1(arg)   
def fun2(x,y,z):   
    return x+y+z   
      
# 测试代码       
a = 3       
b = 4       
c = 5   
  
print fun1(a,b,c)   
print fun2(a,b,c)   