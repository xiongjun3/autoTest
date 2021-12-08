#  -*-  coding: utf-8  -*-
import configparser
import os
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def get_config(self):
        # python3里面自带configparser模块来读取ini文件
        # 读取iselenium中的Chrome driver的路径，不然执行的时候会报错
        config = configparser.ConfigParser()
        # 用户的主目录
        homepath = os.environ['HOME']
        # os.path.join用来拼接，最终是iselenium.ini文件的路径
        configpath = os.path.join(homepath,'iselenium.ini')
        config.read(configpath)
        # config.read(os.path.join(os.environ['HOME'],'iselenium.ini'))
        return config

    # 防止重复初始化webdriver，需要一个构造函数，如果形参base_driver==none,就初始化一个，如果已经有driver了，就把driver赋值给base_driver
    # 则需要PageObject返回处也加一个driver参数
    _base_url = "https://dashboard.qa.axinan.com/platform/policy"
    def __init__(self, base_driver: WebDriver=None):
        config = self.get_config()

        try:
            using_headless = os.environ["using_headless"]
        except KeyError:
            using_headless = None
            print('没有配置环境变量 using_headless,按照有界面方式运行自动化测试')

        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print("使用无界面方式运行")
            # add_argument 添加启动参数
            chrome_options.add_argument("--headless")

        # driver前加self，让其变成一个实例变量，如是只是一个变量是传不到子类中去的

        if base_driver == None:
            # 传入两个参数，第一个参数是driver的路径，
            self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'),
                                           options=chrome_options)
            # self.driver = webdriver.Chrome()
            self.driver.get(self._base_url)
            self.driver.maximize_window()


            time.sleep(2)
            self.driver.find_element(By.ID, "email").send_keys("jun.xiong@iglooinsure.com")
            locator = (By.ID, "password")
            WebDriverWait(self.driver, 10, 0.5).until(expected_conditions.element_to_be_clickable(locator))
            self.driver.find_element(By.ID, "password").send_keys("123456")
            self.driver.find_element(By.CLASS_NAME, "igloo-login-button").click()
            time.sleep(2)
        else:
            self.driver = base_driver

    # 封装查找元素的方法
    def find(self, by, value):
        return self.driver.find_element(by, value)

    # 封装查找点击的方法
    def find_and_click(self, by, value):
        return self.driver.find_element(by, value).click()

    # 封装查找发送内容的方法
    def find_and_send(self, by, value, text):
        return self.driver.find_element(by, value).send_keys(text)

    # 封装查找列表的方法
    def find_list(self, by, value):
        return self.driver.find_elements(by, value)

    # 封装显示等待
    def wait(self,second,element):
        WebDriverWait(self.driver, second, 0.5).until(expected_conditions.element_to_be_clickable(element))

    # 封装move readonly
    def move_readonly(self,n):
        self.driver.execute_script("document.getElementsByTagName('input')["+n+"].removeAttribute('readonly')")

    def search(self, text):
        # text可以是claim id也可以是coc no
        ele_search = (By.XPATH, '//*[@class="igloo-form-filter"]/span/input')
        self.wait(5, ele_search)
        search_input = self.find(*ele_search)
        search_input.send_keys(text)
        search_input.send_keys(Keys.ENTER)
        time.sleep(2)
        # check 搜索结果
        content1 = self.find(By.XPATH, '//*[@class="ant-table-tbody"]/tr[1]/td[1]').text
        content2 = self.find(By.XPATH, '//*[@class="ant-table-tbody"]/tr[1]/td[2]').text
        content3 = self.find(By.XPATH, '//*[@class="ant-table-tbody"]/tr[1]/td[3]').text
        content4 = self.find(By.XPATH, '//*[@class="ant-table-tbody"]/tr[1]/td[4]').text
        content5 = self.find(By.XPATH, '//*[@class="ant-table-tbody"]/tr[1]/td[5]').text

        return content1,content2,content3,content4,content5

    def filter_date(self,start_date,end_date):
        ele_filter = (By.XPATH, '//*[@class="ant-btn igloo-form-filter-filter-button"]')
        self.wait(5,ele_filter)
        self.find_and_click(*ele_filter)

        time.sleep(1)
        #找到start_date,的输入框,去掉只读属性
        js = "document.getElementsByTagName('input')[4].removeAttribute('readonly')"
        # 执行js代码
        self.driver.execute_script(js)
        # 向时间控件start date 输入时间
        self.driver.find_element(By.XPATH, '//*[@placeholder="Start date"]').send_keys(start_date)
        # 找到end_date的输入框，去掉只读属性
        js = "document.getElementsByTagName('input')[5].removeAttribute('readonly')"
        self.driver.execute_script(js)
        self.driver.find_element(By.XPATH,'//*[@placeholder="End date"]').send_keys(end_date)
        #点击apply按钮
        self.driver.find_element(By.XPATH, '//*[@class="igloo-form-filter-drop-down-footer"]/div/div[2]').click()
        time.sleep(8)
        # 获取claim date 列表
        ele_claim_date = (By.XPATH, '//*[@class="ant-table-tbody"]/tr//td[5]')
        self.wait(5,ele_claim_date)
        date_ele_list = self.find_list(*ele_claim_date)
        length = len(date_ele_list)
        date_list = []
        for i in range(length):
            # 循环获取列表的text属性，并拼成一个新的数组
            ele = date_ele_list[i].text
            date_list.append(ele)
        return date_list

    def filter_status(self,status):
        ele_filter = (By.XPATH, '//*[@class="ant-btn igloo-form-filter-filter-button"]')
        # 显示等待
        self.wait(5,ele_filter)
        self.find_and_click(*ele_filter)
        time.sleep(1)
        # 选择状态
        ele_policy_status = (By.XPATH, '//*[@value="'+status+'"]')
        self.find_and_click(*ele_policy_status)
        time.sleep(1)
        # 点击apply按钮
        self.driver.find_element(By.XPATH,'//*[@class="igloo-form-filter-drop-down-footer"]/div/div[2]').click()
        time.sleep(3)
        # 获取状态列表
        ele_list = self.driver.find_elements(By.XPATH,'//*[@class="igloo-typography-status word-wrap"]')
        length = len(ele_list)
        status_list = []
        for i in range(length):
            policy_status = ele_list[i].text
            status_list.append(policy_status)
        return status_list



