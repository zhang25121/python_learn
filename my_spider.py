#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import re
import os


headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
for u in range(1, 215):
	url = 'http://www.tupianzj.com/meinv/xinggan/list_176_' + str(u) + '.html'
	data = opener.open(url).read().decode('gbk')
	# 第一层先大致找出每个图片集的封面链接和标题
	pat1 = '</em></span> </li><li> <a href="(.+?).html" title="(.+?)"><img src="'
	result = re.compile(pat1).findall(data)
	result = tuple(result)
	print(result[0])

	for sub_url, title in result:
		# 创建以封面标题命名的文件夹
		filename = os.getcwd() + "\\" + title
		# 如果不存在则创建
		if not os.path.exists(filename):
			os.mkdir(filename)
		# 将爬下来的/meinv/20190712/189834.html格式链接，拼上域名作为访问相册集的入口url
		sub_Url = 'http://www.tupianzj.com' + sub_url + '.html'
		print(sub_Url)
		# 打开第一个图片集的入口
		sub_data = opener.open(sub_Url).read().decode('gbk')
		# 将打开的大图页面 正则匹配出大图url,并将图片url保存在文件夹中
		bigpic_pat = '<img src="(.+?)" id="bigpicimg"'
		bigpic = re.compile(bigpic_pat).findall(sub_data)
		bigpic = tuple(bigpic)
		urllib.request.urlretrieve(bigpic[0], filename=filename + "\\" + '1.png')
		# 获取相册集页数
		pages_pat = '共(.+?)页'
		pages = re.compile(pages_pat).findall(sub_data)
		pages = tuple(pages)
		pages = int(pages[0])
		print(pages)
		for i in range(2, pages):
			subs_url = 'http://www.tupianzj.com' + sub_url + '_' + str(i) +'.html'
			print(subs_url)
			subs_data = opener.open(subs_url).read().decode('gbk')
			# 将打开的大图页面 正则匹配出大图url,并将图片url保存在文件夹中
			bigpic_sub_pat = '<img src="(.+?)" id="bigpicimg"'
			bigpic_sub = re.compile(bigpic_pat).findall(subs_data)
			bigpic_sub = tuple(bigpic_sub)
			urllib.request.urlretrieve(bigpic_sub[0], filename=filename + "\\" + str(i) + '.png')
