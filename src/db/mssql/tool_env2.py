# -*- coding: utf8 -*-
from tool_py import py_dictionary
import datetime
import os
import re
import time


signs = [">=","<=",">","<","="]

def convert_utf8(file_name):
    fp = open(file_name,"a+")
    con = fp.read()
    con = force_unicode(con).encode("utf8")
    fp.seek(0)
    fp.truncate()
    fp.write(con)
    fp.close()

def force_unicode(txt):
    try:
        return txt.decode('utf8')
    except:
        pass
    try:
        return txt.decode('cp936')
    except:
        pass
    try:
        return unicode(txt)
    except:
        pass
    return txt

def force_cp936(txt):
    try:
        return txt.encode('cp936',"ignore")
    except:
        pass
    return txt

def force_utf8(txt):
    try:
        return txt.encode('utf8','ignore')
    except:
        pass
    return txt

def is_number(txt):
    try:
        txt = float(txt)
        return True
    except:
        return False

 

def valid_value_test(txt): # 筛选空值, none, null等无效数据
    invalid_value = ["", "none", "null"]
    if txt is not None:
        try:
            txt = txt.strip().lower()
            if txt in invalid_value:
                return False
            else:
                return True
        except:
            return True
    else:
        return False

def force_to_float(txt):
    try:
        txt = float(txt)
    except:
#        print u"不能转换为浮点数字"
        txt = None
    return txt


def time_switch(time_string):
#    format = None
#    time = None
    
    time_format = [
                   [re.compile("(\d+-){2}\d+\s+(\d+:){2}\d+\.\d+"), "%Y-%m-%d %H:%M:%S.%f"],
                   [re.compile("(\d+-){2}\d+\s+(\d+:){2}\d+"), "%Y-%m-%d %H:%M:%S"],
                   [re.compile("(\d+-){2}\d+"), "%Y-%m-%d"],
                   [re.compile("(\d+/){2}\d+\s+(\d+:){2}\d+\.\d+"), "%Y/%m/%d %H:%M:%S.%f"],
                   [re.compile("(\d+/){2}\d+\s+(\d+:){2}\d+"), "%Y/%m/%d %H:%M:%S"],
                   [re.compile("(\d+/){2}\d+"), "%Y/%m/%d"], 
                   ]
    for fmt in time_format:

        format = fmt[0].match(time_string)
        if format:
            try:
                time = datetime.datetime.strptime(time_string, fmt[1])
                return time
            except:
                pass

def to_timestamp(time_string):
    time_format = [
                   [re.compile("(\d+-){2}\d+\s+(\d+:){2}\d+\.\d+"), "%Y-%m-%d %H:%M:%S.%f"],
                   [re.compile("(\d+-){2}\d+\s+(\d+:){2}\d+"), "%Y-%m-%d %H:%M:%S"],
                   [re.compile("(\d+-){2}\d+"), "%Y-%m-%d"],
                   [re.compile("(\d+/){2}\d+\s+(\d+:){2}\d+\.\d+"), "%Y/%m/%d %H:%M:%S.%f"],
                   [re.compile("(\d+/){2}\d+\s+(\d+:){2}\d+"), "%Y/%m/%d %H:%M:%S"],
                   [re.compile("(\d+/){2}\d+"), "%Y/%m/%d"], 
                   ]
    for fmt in time_format:

        format = fmt[0].match(time_string)
        if format:
            try:
                t = time.strptime(time_string,fmt[1])
                t2 = datetime.datetime.strptime(time_string, fmt[1])
#                print t2.max
                timestamp = time.mktime(t2.timetuple())
                return timestamp
            except:
                pass
            
def get_strptime(time_str, format):
    time_str = time_str.strip()
    format = format.strip().replace("\n", "")
    
    try:
        time = datetime.datetime.strptime(time_str, format)
        return time
    except:
        pass
            
def get_SQL_time(con):
    
    ptn_time = [
                re.compile("""\s\(*([^\s><\=]+)\s*([><\=]+)\s*['"](\d+-\d+-\d+(?:\s*\d+\:\d+\:\d+)*)['"]\s*and([^><\=]+)([><\=]+)\s*['"](\d+-\d+-\d+(?:\s*\d+\:\d+\:\d+)*)['"]""", re.I),
                re.compile("""\s\(*([^\s><\=]+)\s*([><\=]+)\s*['"](\d+/\d+/\d+(?:\s*\d+\:\d+\:\d+)*)['"]\s*and([^><\=]+)([><\=]+)\s*['"](\d+/\d+/\d+(?:\s*\d+\:\d+\:\d+)*)['"]""", re.I),
                re.compile("""\s([^\s]+)\s*([><\=]+)\s*TO_DATE\(['"]([^'"]+)['"]\s*,\s*['"]([^'"]+)['"]\)\s*AND([^><\=]+)([><\=]+)\s*TO_DATE\(['"]([^'"]+)['"]\s*,\s*['"]([^'"]+)['"]\)""", re.I),
                re.compile("""BETWEEN\s*TO_DATE\s*\(['"]([^'"]+)['"]\s*,\s*['"]([^'"]+)['"]\)\s*AND\s*TO_DATE\s*\(['"]([^'"]+)['"]\s*,\s*['"]([^'"]+)['"]\)""", re.I),
                ]
    time_list = []
    for ptn in ptn_time:
        time_iter = ptn.finditer(con)
        while True:
            try:
                time_record = []
                iter = time_iter.next()
                con_time = iter.groups()
                print "con_time:" 
                print con_time
#                    print "---------"
                start_index = iter.span()[0]
                time_record.append(con_time)
                time_record.append(start_index)
                time_list.append(time_record)
            except:
                break
#    for time_rec in time_list:
#        con_time = time_rec[0]
#        start_index = time_rec[1]
##            line_num = self.get_line_num(whole_con, start_index)
##            print line_num
#        line_num = self.get_line_num(whole_con, start_index)
#        start_time = None
#        end_time = None
            
def sql_time_convert(format):
    sql_python = {"YYYY":"%Y", "MM":"%m", "DD":"%d", "HH24":"%H", "HH12":"%I", "MI":"%M","SS":"%S"}
    for s_p in sql_python.keys():
        format = format.replace(s_p, sql_python[s_p])
    return format
            
            
            
            
            
            
            
            
            
            
#        print time_list
def time_compare(start_time, end_time):
    try:
        delta = end_time - start_time
#        print delta
        if delta.days < 0 or  delta.seconds < 0 or delta.microseconds < 0:
            return False
#        elif delta == datetime.timedelta(0):
#            return False
        else:
#            print str(delta)
            return delta
    except:
        return False
    
def time_compare_2(time_1, time_2,sign):
#    print "mmmmmmmmmmmmmmm"
#    if sign not in signs:
#        print u"错误的符号:%s" %sign
#        return False
#    if isinstance(time_1, datetime.datetime) == False:
#        print u"错误的时间:%s" %time_1
#        return False    
#    if isinstance(time_2, datetime.datetime) == False:
#        print u"错误的时间:%s" %time_2
#        return False        

    if sign == "=":
        if time_1 == time_2:
            return True
    elif sign == ">":
        if time_1 > time_2:
            return True
    elif sign == ">=":
        if time_1 >= time_2:
            return True
    elif sign == "<":
        if time_1 < time_2:
            return True
    elif sign == "<=":
        if time_1 <= time_2:
            return True
    else:
        return False

            
#        result = eval("time_1%stime_2" % sign)
#        return result  
#    except:
#        return False

def get_file_format(path):
    if "." in path:
        path = path.split(".")
        return path[-1].lower()
    else:
        return None           
        
def get_all_path(dir,topdown=True, get_dirs=False, get_path=True, format_keep=[]):
    """
        args:
        
        format_keep - specific file format to keep; such as: 'txt'
        
        return: 
        (dir_list, path_list)
        
        dir_list - all dirs below the given dir
        
        path_list - all paths below the given dir
    """
    dir_list = []
    path_list = []
    for root, dirs, files in os.walk(dir, topdown):
        if get_path == True:
            for name in files:
                current_path = os.path.join(root,name)
                if format_keep:
                    for format in format_keep:
                        format = format.lower()
                        file_format = get_file_format(current_path)
                        if file_format.lower() == format:
#                            print current_path
                            path_list.append(current_path)
                else:
#                    print current_path
                    path_list.append(current_path)
        if get_dirs == True:                     
            for name in dirs:
                current_dir = os.path.join(root,name)
#                print current_dir
                dir_list.append(current_dir)
    return dir_list,path_list  

def repeat_list_remove(list):
    list =  sorted(set(list),key=list.index)
    return list

def split_sign(txt):
    result = None
    for sign in signs:
#        print sign
        if sign in txt:
#            print sign
            result = txt.split(sign)
#            result.insert(1,sign)
            result.append(sign)
            break
    return result
    
def split_punc(txt):
    txt = force_unicode(txt)
    puncs = re.compile(u"[,，]")
    txt = puncs.sub("|",txt)
    txt = txt.split("|")
    return txt

def remove_txt_garbage(txt):
    if txt[0:3] == '\xef\xbb\xbf':
        txt = txt[3:]
    return txt

def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def get_pinyins(words,keep_reg=None):
    ptn_keep = None
    if keep_reg:
        ptn_keep = re.compile(keep_reg)
    pinyins = ""
    words = force_unicode(words)
    for word in words:
        word = word.encode("utf8")
        try:
            pinyins += py_dictionary[word][0][:-1]
            
        except:
            if ptn_keep and ptn_keep.search(word):
                pinyins += word
            elif not ptn_keep:
                pinyins += word
            
    print pinyins
    return pinyins

def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    
if __name__ == "__main__":
    import unittest
    class TestCase(unittest.TestCase):
        def test_time_switch(self):    
            time_string = "2010-1-1 12:24:36.594"
            assert time_switch(time_string) == datetime.datetime(2010, 1, 1, 12, 24, 36, 594000)    
            time_string = "2010-1-1 12:24:36"
            assert time_switch(time_string) == datetime.datetime(2010, 1, 1, 12, 24, 36)
            time_string = "2010-1-1"
            assert time_switch(time_string) == datetime.datetime(2010, 1, 1, 0, 0)
            time_string = "2010/1/1 12:24:36.594"
            assert time_switch(time_string) == datetime.datetime(2010, 1, 1, 12, 24, 36, 594000)    
            time_string = "2010/1/1 12:24:36"
            assert time_switch(time_string) == datetime.datetime(2010, 1, 1, 12, 24, 36)
            time_string = "2010/1/1"
            assert time_switch(time_string) == datetime.datetime(2010, 1, 1, 0, 0)
            time_string = "2010-13-1"
            assert time_switch(time_string) == None            
            time_string = "2010/1-1"
            assert time_switch(time_string) == None
            time_string = "null"
            assert time_switch(time_string) == None
            time_string = ""
            assert time_switch(time_string) == None
            
        def test_to_timestamp(self):    
            time_string = "2010-1-1 12:24:36.590"
            assert to_timestamp(time_string) == 1262319876.0
         
            
        def test_force_to_float(self):    
            txt = "2010"
            assert force_to_float(txt) == 2010.0
            txt = 19.22
            assert force_to_float(txt) == 19.22  
            txt = "aa"
            assert force_to_float(txt) == None

        def test_valid_value_test(self):    
            txt = "2010"
            assert valid_value_test(txt) == True
            txt = "  "
            assert valid_value_test(txt) == False
            txt = "none"
            assert valid_value_test(txt) == False  
            txt = "NONE"
            assert valid_value_test(txt) == False
            txt = "null"
            assert valid_value_test(txt) == False                                   
            txt = "NULL"
            assert valid_value_test(txt) == False 
            
        def test_time_compare(self): 
            start_time = datetime.datetime(2011, 1, 1, 0, 0)
            end_time = datetime.datetime(2010, 2, 1, 0, 0)
            assert time_compare(start_time, end_time) == False
            start_time = datetime.datetime(2010, 2, 1, 0, 0)
            end_time = datetime.datetime(2010, 1, 1, 0, 0)
            assert time_compare(start_time, end_time) == False            
            start_time = datetime.datetime(2010, 1, 2, 0, 0)
            end_time = datetime.datetime(2010, 1, 1, 0, 0)
            assert time_compare(start_time, end_time) == False             
            assert time_compare(start_time, end_time) == False            
            start_time = datetime.datetime(2010, 1, 1, 2, 0)
            end_time = datetime.datetime(2010, 1, 1, 0, 0)
            assert time_compare(start_time, end_time) == False
            start_time = datetime.datetime(2010, 1, 1, 0, 2)
            end_time = datetime.datetime(2010, 1, 1, 0, 0)
            assert time_compare(start_time, end_time) == False    
            start_time = datetime.datetime(2010, 1, 1, 0, 0,20)
            end_time = datetime.datetime(2010, 1, 1, 0, 0, 10)
            assert time_compare(start_time, end_time) == False                       
            start_time = datetime.datetime(2010, 1, 1, 0, 0,0, 200000)
            end_time = datetime.datetime(2010, 1, 1, 0, 0, 0, 190000)
            assert time_compare(start_time, end_time) == False
            start_time = datetime.datetime(2010, 1, 1, 0, 0,0, 200000)
            end_time = datetime.datetime(2010, 1, 1, 0, 0, 0, 200000)
            assert time_compare(start_time, end_time) == datetime.timedelta(0)            
            start_time = datetime.datetime(2010, 1, 1, 0, 0,0, 200000)
            end_time = datetime.datetime(2011, 1, 1, 0, 0, 0, 190000)
            assert time_compare(start_time, end_time) == datetime.timedelta(364, 86399, 990000)
            
        def test_time_compare_2(self): 
            start_time = datetime.datetime(2010, 1, 1, 0, 0,0, 200000)
            end_time = datetime.datetime(2011, 1, 1, 0, 0, 0, 190000)
            sign = "<"
            assert time_compare_2(start_time, end_time,sign) == True
            start_time = datetime.datetime(2010, 1, 1, 0, 0,0, 200000)
            end_time = datetime.datetime(2011, 1, 1, 0, 0, 0, 190000)
            sign = ">="
            assert time_compare_2(start_time, end_time,sign) == False 
            start_time = datetime.datetime(2010, 1, 1, 0, 0,0, 200000)
            end_time = datetime.datetime(2010, 1, 1, 0, 0, 0, 200000)
            sign = "="
            assert time_compare_2(start_time, end_time,sign) == True
            start_time = "dd"
            end_time = datetime.datetime(2010, 1, 1, 0, 0, 0, 200000)
            sign = "="
            assert time_compare_2(start_time, end_time,sign) == False
            start_time = "bb"
            end_time = "ff"
            sign = "ss"
            assert time_compare_2(start_time, end_time,sign) == False            
            
        def test_get_file_format(self):
            path = "c:\\a.txt"
            assert get_file_format(path) == "txt"
            path = "c:\\atxt"
            assert get_file_format(path) == None
            
        def test_get_strptime(self):
            time_str = "2010-10-12 23:15:12"
            format = "%Y-%m-%d %H:%M:%S"
            assert get_strptime(time_str, format) == datetime.datetime(2010, 10, 12, 23, 15, 12)
            
            
        def test_sql_time_convert(self):
            format = 'YYYY-MM-DD HH24:MI:SS'
            assert sql_time_convert(format) == "%Y-%m-%d %H:%M:%S"
            format = 'YYYY-MM-DD HH12:MI:SS'
            assert sql_time_convert(format) == "%Y-%m-%d %I:%M:%S"
        def test_is_number(self):
            txt = "2010.12"
            assert is_number(txt) == True
            txt = "12q"
            assert is_number(txt) == False
            txt = "12.3.4"
            assert is_number(txt) == False 
            txt = "-12.3"
            assert is_number(txt) == True             
                   
        def test_repeat_list_remove(self):
            list = [3,2,3,1]
            assert repeat_list_remove(list) == [3,2,1]  
            list = ["bcd","def","abc","abc"]    
            assert repeat_list_remove(list) == ["bcd","def","abc"]
        def test_split_sign(self):
            txt = "a>b"
            assert split_sign(txt) == ["a", "b", ">"]
            txt = "a<=b"
            assert split_sign(txt) == ["a", "b", "<="]
            txt = "abc"
            assert split_sign(txt) == None          
        def test_split_punc(self):
            txt = "a,b,c"
            assert split_punc(txt) == ["a","b","c"]
            txt = u"a，b,c"
            assert split_punc(txt) == ["a","b","c"]
            txt = u"kdanhao"
            assert split_punc(txt) == ["kdanhao"]            
#        fp = open(u"data\\sql测试数据\\test4.sql")
#        con = fp.read()
#        fp.close()
#        get_SQL_time(con)
#    print split_sign("a<b")
    ptn_keep = "[_\da-zA-Z]"
    words="状态POP礼品卡金额明细by订单出库时间2012订单完成时间2012（不含退款订单）_20120507V3.0"
    get_pinyins(words,ptn_keep)
    unittest.main()
    
