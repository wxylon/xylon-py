#-*-coding:utf-8-*-
#http://hi.baidu.com/khzmylyasdhjmwr/item/f2078953e2346acbd2e10c25
#http://blog.sina.com.cn/s/blog_5e32cc130100fltb.html
#http://jyd.me/python/python-string-reverse/

str = "abcdef"
print str, "反转：", str[::-1]

print str, "反转：", reduce(lambda x,y:y+x, str)

a=list(str)
a.reverse()
print str, "反转：", "".join(a)
