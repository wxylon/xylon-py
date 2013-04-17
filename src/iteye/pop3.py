#-*-coding:utf-8-*- 
# pop3.py

import poplib

emailServer = poplib.POP3("pop3.163.com")
emailServer.user("wangxiongdx")
emailServer.pass_("0110cr")
emailServer.set_debuglevel(0)

serverWelcome = emailServer.welcome
print serverWelcome

emailMsgNum, emailSize = emailServer.stat()
print 'email number is %d and size is %d'%(emailMsgNum, emailSize)  

for i in range(emailMsgNum):
    receve = emailServer.retr(i+1)
    print "len:" ,receve.__len__()
    for piece in receve[1]:
        if piece.startswith("Subject"):
            print "\t" + piece.decode('gb2312')
            break

emailServer.quit()


