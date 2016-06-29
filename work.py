# -*- coding: utf-8 -*-

import requests

url="http://op-lf.reidx.com/zhanbao/INSERT_MONITOR/do.php?action=login"
headers_base = {"Host":" op-lf.reidx.com","User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv\":\"49.0) Gecko/20100101 Firefox/49.0","Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language":" zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3","Accept-Encoding":" gzip, deflate","Cookie":" PHPSESSID=mc93er8cqq7j6mne77rd06s992","Connection":" keep-alive","Upgrade-Insecure-Requests":" 1"}


data={"password":"root","username":"亢旭东"}

r=requests.post(url,data=data,headers=headers_base)
print r.text

durr="http://op-lf.reidx.com/zhanbao/INSERT_MONITOR/do.php?action=add_dailyTask"
workdata={"details":"","endtime":"","plandur":"2","proline":"海量","remark":"","starttime":"","state":"进行中","taskitem":"知识整理","taskname":"测试","tasktype":"客户运营","todaydur":"2","worksource":""}
work=requests.post(durr,data=workdata,headers=headers_base)