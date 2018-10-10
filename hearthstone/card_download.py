#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import re
import os
heros = ['druid', 'hunter', 'mage', 'paladin', 'priest', 'rogue', 'shaman', 'warlock', 'warrior','neutral']
for hero in heros:
	hero_file = os.getcwd() + "\\" + hero
	print(hero_file)
	if not os.path.exists(hero_file):
		os.mkdir(hero_file)
	for page in range(1,21):
		url = 'http://hs.blizzard.cn/action/cards/query?cardClass=' + hero +'&' +'p=' + str(page)
		print(url)
		opener = urllib.request.build_opener()
		headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
		opener.addheaders = [headers]
		urllib.request.install_opener(opener)
		response = opener.open(url).read().decode('utf-8')
		card_name = '"name":"(.+?)"'
		card_url =  '"imageUrl":"(.+?)"'
		card_Name = re.compile(card_name).findall(response)
		card_Url = re.compile(card_url).findall(response)
		card_info = zip(card_Name, card_Url)
		for name, url in card_info:
			print(name, url)
			urllib.request.urlretrieve(url, filename=hero_file + "\\" + name + '.png')
