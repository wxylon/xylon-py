class MyException(ZeroDivisionError):
    pass


try:
   # print 1/0
    raise
except (MyException, TypeError):
    print "MyException encoutered"
