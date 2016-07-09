
#coding=utf-8

import os
from selenium import webdriver
import time
import unittest

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
		desired_caps['platformVersion'] = '4.2.2' #系统版本
		desired_caps['deviceName'] = '022AQQ7N37083100'  #设备id
		desired_caps['autoLaunch'] = 'true'  #是否自动启动
		desired_caps['app'] = PATH(
			'/Users/xiongjun/python/apk/app-debug-wpvar.apk'      #安装包的路径，放在该py文件的目录下
		)
		desired_caps['appPackage'] = 'com.liwushuo.gifttalk'  #包名
		desired_caps['appActivity'] = 'com.liwushuo.gifttalk.MainActivity'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

	def tearDown(self):
		self.driver.quit() #case执行完退出

	def test_dpApp(self):  #需要执行的case
		#time.sleep(20)
		my = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'我的')]")
		my.click()
		time.sleep(3)

		print 1
		
		login = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'未登录')]/preceding-sibling::*[1]")
		login.click()
		time.sleep(3)

		print 2
	
		tel = self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'输入手机号')]")
		#for i in range(11):
			#tel.send_keys(i)
		#tel.set_value('123sdf123');
		#tel.set_text('123sdf123');

		print 3
		
		time.sleep(3)
		pass_word = self.driver.find_element_by_xpath("//android.widget.EditText[1]")
		pass_word.send_keys('wwwwww')

		print 4

		time.sleep(3)
		bun_submit = self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'登录')]")
		bun_submit.click()

		print 5


		'''
		login = self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text,'我的')]')


		us = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/other_login_wrapper")
		us.send_keys('17710144548')
		pw = self.driver.find_element_by_id('com.liwushuo.gifttalk:id/et_login_certificate')
		pw.send_keys('wwwwww')
		login = self.driver.find_element_by_id('com.liwushuo.gifttalk:id/login')
		login.click()
		'''
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(DpAppTests)
	unittest.TextTestRunner(verbosity=2).run(suite) #执行测试用例

