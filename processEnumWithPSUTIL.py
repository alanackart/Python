# -*- coding: utf8 -*-
import psutil

print u"进程ID：    模块名："
ACCESS_DENIED=''
for pid in sorted(psutil.get_pid_list()):
    try:
        p = psutil.Process(pid)
        pinfo = p.as_dict(ad_value=ACCESS_DENIED)
    print u"%05x      %s"%(pid,pinfo['name']
    except psutil.NoSuchProcess: pass
  
raw_input()  #Press any key to end 
