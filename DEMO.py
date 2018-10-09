#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import re
import os
url = 'http://www.tupianzj.com/meinv/xiezhen/list_179_1.html'
headers = (
	# 'Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	# 'Accept-Encoding', 'gzip, deflate',
	# 'Connection', 'keep-alive',
	# 'Referer', 'http://www.tupianzj.com/meinv/xiezhen/list_179_3.html',
	'User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
)

opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
data = opener.open(url).read().decode('gbk')
# print(data)

#排除其他图干扰
pat1 = '<LI>(.+?)</LI>'
result = re.compile(pat1).findall(data)
result = str(result)
# 封面png图片匹配下载
# 封面图片地址 封面标题
pat2 = '<img src="http://(.+?)" alt="(.+?)" border="0"'
result1 = re.compile(pat2).findall(result)
result1 = result1[:]

pat3 = '<a href="(.+?)" target="_blank">'
result2 = re.compile(pat3).findall(result)  #第一页封面的链接

# # result2得到每个封面的链接
for i in result2:
	if result2.count(i) != 1:
		result2.remove(i)
print(type(result1))

print("/************************************************************************************************/")
print("/************************************************************************************************/")


# 将result1和result2合并为result3,方便后续遍历

# 按封面来依次创建文件夹
c = zip(result1,result2)

for i,j in c:
	print(i[0],i[1],j)


print("/************************************************************************************************/")
print("/************************************************************************************************/")