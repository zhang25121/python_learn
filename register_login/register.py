#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
# 1. 提示用户输入用户名
print("用户名由6-16位的字母数字下划线组成")
while True:
	username = input("请输入你要注册的用户名：")
	if len(username) == 0:
		print("用户名不能为空，请重新输入!")
		continue
	if len(username) < 6 :
		print("用户名太短了")
		continue
	if len(username) > 16 :
		print("用户名太长了")
		continue
	if len(username) >= 6 and len(username) <=16:
		pass
	pat_username = '[^a-zA-Z10-9_]'
	name_result = re.compile(pat_username).findall(username)
	if not name_result:
		break
	else:
		print("注册用户名不合法，请重新输入!")
		continue
# 2. 提示用户输入密码
while True:
	print("密码由6-16位的字母数字下划线组成")
	password = input("请输入你要注册的密码：")
	if len(password) == 0:
		print("密码不能为空，请重新输入!")
		continue
	if len(password) < 6 :
		print("密码太短了")
		continue
	if len(password) > 16 :
		print("密码太长了")
		continue
	if len(password) >= 6 and len(password) <=16:
		pass
	pat_password = '[^a-zA-Z10-9_]'
	psd_result = re.compile(pat_password).findall(password)
	if not psd_result:
		break
	else:
		print("密码不合法，请重新输入!")
		continue
# 3. 提示用户确认输入密码，如果确认密码和密码一致，则密码输入成功.
while True:
	sure_password = input("请再次输入你要注册的密码：")
	# 判断两次密码是否一致,一致则注册成功，给用户提示,“恭喜您，账号注册成功!”
	if password == sure_password:
		print("恭喜您，账号注册成功!")
		with open('user_info.txt', 'a+') as user_info:
			user_info.write(username+" "+password)
			user_info.write('\n')
			break
	else:
		continue