#  -*-  coding: utf-8  -*-
import configparser
import os
import time

from selenium import webdriver
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
        configpath = os.path.join(homepath,'iselenium.ini'')
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

            time.sleep(2)
            self.driver.find_element(By.ID, "email").send_keys("jun.xiong@iglooinsure.com")
            locator = (By.ID, "password")
            WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(locator))
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

