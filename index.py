
#coding=utf-8

import os
#from selenium import webdriver
from appium import webdriver
import time
import unittest
import json

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

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

	def tearDown(self):
		self.driver.quit() #case执行完退出

	def test_dpApp(self):  #需要执行的case

		time.sleep(2)
		self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'我的')]").click()

		self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'未登录')]/preceding-sibling::*[1]").click()
		

		#self.login_with_uname()
		#self.login_with_code()
		self.login_with_QQ()

		time.sleep(5)

	def login_with_uname(self):

		self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'输入手机号')]").send_keys('17710144548')	
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/et_login_certificate").send_keys('123456')

		self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'登录')]").click()
	

	def login_with_code(self):

		self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'输入手机号')]").send_keys('17710144548')	
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/tv_login_type_switch").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/tv_auth_code_btn").click()
		time.sleep(5)
		self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'登录')]").click()


	def login_with_QQ():
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/signin_qq").click()
		


		
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(DpAppTests)
	unittest.TextTestRunner(verbosity=2).run(suite) #执行测试用例

