#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
class Register(object):

	def __init__(self):
		self.username = None
		self.password = None
		self.sure_password = None
		self.register_info = None

	def r_username(self):
		# 1. 提示用户输入用户名
		print("用户名由6-16位的字母数字下划线组成")
		existed = False
		if existed == False:
			while existed == False:
				global username
				username = input("请输入你要注册的用户名：")
				if len(username) == 0:
					print("用户名不能为空，请重新输入!")
					continue
				if len(username) < 6:
					print("用户名太短了")
					continue
				if len(username) > 16:
					print("用户名太长了")
					continue
				if len(username) >= 6 and len(username) <= 16:
					with open('user_info.txt') as user_info:
						while True:
							info = user_info.readline().split(" ")
							if info[0] == '':
								print("用户名可用")
								existed = True
								break
							else:
								info = info[0]
								if info == username:
									print("用户名已存在")
									break
								else:
									continue
						continue

		pat_username = '[^a-zA-Z10-9_]'
		name_result = re.compile(pat_username).findall(username)
		if not name_result:
			self.username = username
		else:
			print("注册用户名不合法，请重新输入!")
			Register.r_username(self)

	def r_password(self):
		# 2. 提示用户输入密码
		while True:
			print("密码由6-16位的字母数字下划线组成")
			password = input("请输入你要注册的密码：")
			if len(password) == 0:
				print("密码不能为空，请重新输入!")
				continue
			if len(password) < 6:
				print("密码太短了")
				continue
			if len(password) > 16:
				print("密码太长了")
				continue
			if len(password) >= 6 and len(password) <= 16:
				pass
			pat_password = '[^a-zA-Z10-9_]'
			psd_result = re.compile(pat_password).findall(password)
			if not psd_result:
				self.password = password
				break
			else:
				print("密码不合法，请重新输入!")
				continue

	def r_sure_password(self):
		# 2. 提示用户输入密码
		while True:
			print("密码由6-16位的字母数字下划线组成")
			sure_password = input("请再次输入你要注册的密码：")
			if len(sure_password) == 0:
				print("密码不能为空，请重新输入!")
				continue
			if len(sure_password) < 6:
				print("密码太短了")
				continue
			if len(sure_password) > 16:
				print("密码太长了")
				continue
			if len(sure_password) >= 6 and len(sure_password) <= 16:
				pass
			pat_sure_password = '[^a-zA-Z10-9_]'
			sure_psd_result = re.compile(pat_sure_password).findall(sure_password)
			if not sure_psd_result:
				self.sure_password = sure_password
				break
			else:
				print("密码不合法，请重新输入!")
				continue

	def r_confirm_password(self):
		if self.password == self.sure_password:
			self.register_info = self.username + " " + self.password
		else:
			print("两次密码不一致，请重新输入")
			Register.r_password(self)
			Register.r_sure_password(self)

	def write_uesr_info(self):
		try:
			with open('user_info.txt', 'a+') as user_info:
				print("恭喜！账号注册成功！")
				user_info.write(self.register_info)
				user_info.write('\n')
		except Exception as e:
			print("%s" % e)


if __name__ == "__main__":
	a = Register()
	a.r_username()
	a.r_password()
	a.r_sure_password()
	a.r_confirm_password()
	a.write_uesr_info()