#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import re
import os
for i in range(1,127):
	url = 'http://www.tupianzj.com/meinv/xiezhen/list_179_' + str(i) + '.html'
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
	for i in result1:
		print('result1 = ' + str(i) )
	print("/************************************************************************************************/")
	print("/************************************************************************************************/")
	for i in result2:
		print('result2 = ' + i)

	# 将result1和result2合并为result3,方便后续遍历
	result3 = zip(result1,result2)
	# 按封面来依次创建文件夹

	# 循环下载第一页的内容
	for i,j in result3:
		current_path = os.getcwd()
		#创建文文件夹
		creat_file = os.path.join(current_path, i[1])
		if not os.path.exists(creat_file):
			os.mkdir(creat_file)
		# 依次打开封面的链接进行图片下载
		current_url = 'http://www.tupianzj.com' + j
	#################################################################################
		for q in range(0,40):
			try:
				subfile = opener.open(current_url).read().decode('gbk') #子页面内容
				if subfile:
					#pat4 = '<div id=\'bigpic\'> <a href=\'javascript:dPlayNext();\'><a href=\'(.+?)\'><img src="(.+?)" id="bigpicimg"'
					pat4 = '<img src="(.+?)" id="bigpicimg"'
					pat5 = "><a href='(.+?)'><img"
					save_data = re.compile(pat4).findall(subfile)
					if save_data:
						save_data = save_data[0]
					else:
						continue
					q += 1
					name = creat_file + '\\' + str(q)+ '.jpg'

					urllib.request.urlretrieve(save_data,filename=name)

					next_url = re.compile(pat5).findall(subfile)
					if next_url:
						current_url = current_url[:39] + str(next_url[0])
				else:
					continue
			except:
				break
#################################################################################
