# _*_ coding:utf8 _*_

from threading import Thread
import time

## http://www.oschina.net/code/snippet_868600_20537
def run(n):
    for tc in range(1, 5):
        print str(n) + '的' + str(tc) + '线程一直在执行的时间:' + str(time.time()) + '\n'
        time.sleep(1)
    pass

def startThread():
    t1 = Thread(target=run, args=(1,))
    t2 = Thread(target=run, args=(2,))
    t3 = Thread(target=run, args=(3,))
    t4 = Thread(target=run, args=(4,))
    t5 = Thread(target=run, args=(5,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    pass

if __name__ == '__main__':
    startThread()
    pass
