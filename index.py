
#-*- coding:utf-8 -*-


import os
from appium import webdriver
import time
import unittest
import json
import https
from login import LoginTests

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

		LoginTests.test_login_with_psw()
		

		
		#修改密码
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/avatar").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/rl_set_password").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/et_pwd").send_keys("qwerty")
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/action_open_regist").click()

		#用新密码登陆
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/logout").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/avatar").click()
		self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'输入手机号')]").send_keys('17710144548')	
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/et_login_certificate").send_keys('qwerty')

		self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'登录')]").click()
		#断言
		nickname = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/nickname").text
		self.assertNotEqual(nickname,"未登陆",msg="modify password fail!")

		#还原密码
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/avatar").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/rl_set_password").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/et_pwd").send_keys("123456")
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/action_open_regist").click()

		#添加地址
		address_count_before = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/address_count").text
		address_brfoer = int(address_count_before)

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
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/action_back").click()

		address_count_after = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/address_count").text
		address_after = int(address_count_after)
		self.assertNotEqual(address_after,address_brfoer,msg="creat new address fail!")



		#删掉地址
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/rl_address").click()		
		self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'收货人：auto_name1')]").click()
		self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'删除')]").click()
		time.sleep(1)
		self.driver.find_element_by_id("android:id/button1").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/action_back").click()

		address_count_after_delete = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/address_count").text
		aderr_after_delete = int(address_count_after_delete)
		self.assertNotEqual(aderr_after_delete,address_after,msg="delete new address fail!")
		self.assertEqual(aderr_after_delete,address_brfoer,msg="delete new address fail!")

		#修改昵称
		nickname_before = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/nickname").text		
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/rl_nickname").click()	
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/nickname").clear()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/nickname").send_keys("test_name")
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/action_save").click()	
		#断言
		nickname_after = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/nickname").text
		self.assertNotEqual(nickname_after,nickname_before,msg="modify nickname fail!")
		#还原昵称
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/nickname").clear()		
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/nickname").send_keys(nickname_before)
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/action_save").click()	
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/action_back").click()

		#签到
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/tab_widget_internal_icon").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/action_open_check_in").click()
		score = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/credit").text
		score = int(score)
		score +=2
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/sign_in").click()
		time.sleep(1)
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/iv_btn_close").click()
		score_after = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/credit").text
		score_after = int(score_after)
		self.assertEqual(score,score_after,msg="sign in fail!")
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/action_back").click()

		

		#收藏攻略
		self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'分类')]").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/category_article_see_more").click()
		self.driver.find_element_by_xpath("//android.widget.ImageView[contains(@index,0)]").click()
		count_before = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/fav_count").text
		count_before = int(count_before)
		count_before += 1 

		context_artcle = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/post_title").text

		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/fav_heart").click()
		count_after = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/fav_count").text
		count_after = int(count_after)
		self.assertNotEqual(count_before,count_after,msg = "favor success!")

		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/action_back").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/action_back").click()
		self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'我的')]").click()
		self.driver.find_element_by_id("com.liwushuo.gifttalk:id/article_tab").click()
		context_artcle_favor = self.driver.find_element_by_id("com.liwushuo.gifttalk:id/post_title").text
		self.assertIsNot(context_artcle,context_artcle_favor,msg = "favor list is ok!")






										

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(DpAppTests)
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite) #执行测试用例

