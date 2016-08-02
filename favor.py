#-*- coding:utf-8 -*-


import os
from appium import webdriver
import time
import unittest
import json
import https

config_file = file("./config.json")
config = json.load(config_file)


#appium环境配置
PATH = lambda p: os.path.abspath(
	os.path.join(os.path.dirname(__file__),p)
)

'''os.path.dirname(__file__)   获取文件所在位置的完整路径
	os.path.join(os.path.dirname(__file__),p)   将多个路径组合返回
	os.path.abspath('')  返回当前文件的绝对路径
	os.path.abspath()   返回文件的绝对路径 '''


class DpAppTests(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android' #设置平台
		desired_caps['platformVersion'] = config['platformVersion'] #系统版本
		desired_caps['deviceName'] = config['deviceName']  #设备id
		desired_caps['autoLaunch'] = True  #是否自动启动
		desired_caps['app'] = PATH(config['app'])
		desired_caps['appPackage'] = 'com.liwushuo.gifttalk'  #包名
		desired_caps['appActivity'] = 'com.liwushuo.gifttalk.MainActivity'
		desired_caps['unicodeKeyboard'] = True
		desired_caps['resetKeyboard'] = True
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

	def tearDown(self):
		self.driver.quit() #case执行完退出

	