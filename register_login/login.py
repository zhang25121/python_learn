#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1. 提示用户输入用户名
while True:
	username = input("请输入你的用户名：")
	if len(username) == 0:
		print("用户名不能为空")
	else:
		break
	# 2. 提示用户输入密码
while True:
	password = input("请输入你的密码：")
	if len(password) == 0:
		print("密码不能为空")
	else:
		break

sure_login_info = username + " " + password + "\n"
# 以只读文件打开user_info，检查用户输入的用户名和密码是否在用户信息内
with open('user_info.txt','r') as user_info:
	while True:
		info = user_info.readline()
		if not info:
			# 如果用户名和密码不匹配则提示用户"用户名或密码错误"
			print("用户名或密码错误")
			break
		# 如果用户名和密码匹配则提示用户登录成功
		if sure_login_info == info:
			print("登录成功")
			break
		else:
			continue

