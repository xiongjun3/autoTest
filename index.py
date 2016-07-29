
#-*- coding:utf-8 -*-


import os
#from selenium import webdriver
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

	def test_dpApp(self):  #需要执行的case

		#登陆
		time.sleep(10)
		self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'我的')]").click()
		self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'未登录')]/preceding-sibling::*[1]").click()

		self.login_with_psw()
		#self.login_with_code()
		#self.login_with_QQ()
		#self.login_with_wechat()
		#self.login_with_weibo()

		time.sleep(5)

		#修改密码
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/avatar").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/rl_set_password").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/et_pwd").send_keys("qwerty")
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/action_open_regist").click()

		#断言
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/logout").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/avatar").click()
		self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'输入手机号')]").send_keys('17710144548')	
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/et_login_certificate").send_keys('qwerty')

		self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'登录')]").click()		
		try:
			user_name = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/nickname").text
			assert (user_name == "17710144548"),"login fail"
		except AssertionError,msg:
			print msg

		#还原密码
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/avatar").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/rl_set_password").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/et_pwd").send_keys("123456")
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/action_open_regist").click()

		#添加地址
		address_count_before = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/address_count").text

		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/rl_address").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/build_new_address").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/et_receiving_name").send_keys("auto_name1")
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/et_receiving_phone").send_keys("13511111111")
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/tx_pcd").click()
		time.sleep(2)

		#滑动选省市区
		#province = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/province")


		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/done").click()

		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/et_road").set_text("中文地址")
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/right_text").click()
		address_count_after = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/address_count").text
		self.assertEqual(address_count_before,address_count_after,msg="creat new address fail!")



		#删掉地址
		self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'收货人：auto_name1')]").click()
		self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'删除')]").click()
		time.sleep(1)
		self.driver.find_element_by_id("android:id/button1").click()
		address_count_after_delete ＝ self.driver.find_element_by_id("com.liwushuo.gifttalk:id/address_count").text
		self.assertEqual(address_count_after_delete,address_count_after,msg="delete new address fail!")
		self.assertNotEqual(address_count_after_delete,address_count_before,msg="delete new address fail!")



	def login_with_psw(self):

		self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'输入手机号')]").send_keys('17710144548')	
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/et_login_certificate").send_keys('123456')

		self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'登录')]").click()

		try:
			user_name = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/nickname").text
			assert (user_name == "17710144548"),"login fail"
		except AssertionError, msg:
			print msg
		

	def login_with_code(self):

		self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'输入手机号')]").send_keys('17710144548')	
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/tv_login_type_switch").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/tv_auth_code_btn").click()
		time.sleep(5)
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/et_login_certificate").send_keys(getSmsCode("17710144548"))
		self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'登录')]").click()
		
		user_name = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/nickname").text
		self.assertNotEqual(user_name,"17710144548",msg="login fail")

		'''
		try:
			user_name = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/nickname").text
			assert (user_name == "17710144548"),"login fail"
		except AssertionError as msg:
			print msg
		'''



	def login_with_QQ(self):
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/signin_qq").click()
		time.sleep(5)
		self.driver.find_element_by_class_name("android.widget.Button").click()

		#绑定手机号
		time.sleep(5)
		self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'手机号')]").send_keys('17710144548')
		self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'获取验证码')]").click()
		time.sleep(5)
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/et_sms_auth_code").send_keys(https.getSmsCode("17710144548"))
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/tv_next_btn").click()
		

		#修改绑定的手机号




	def login_with_wechat(self):
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/signin_wechat").click()
		


	def login_with_weibo(self):
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/signin_weibo").click()
		time.sleep(5)



										

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(DpAppTests)
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite) #执行测试用例

