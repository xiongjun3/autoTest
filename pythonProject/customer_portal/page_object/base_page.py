import time
import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver



class BasePage:
    # 防止重复初始化webdriver，需要一个构造函数，如果形参base_driver==none,就初始化一个，如果已经有driver了，就把driver赋值给base_driver
    # 则需要PageObject返回处也加一个driver参数
    _base_url = "https://homecredit.qa.axinan.com/pc/policy"
    def __init__(self, base_driver: WebDriver=None):
        if base_driver == None:
            # driver前加self，让其变成一个实例变量，如是只是一个变量是传不到子类中去的
            self.driver = webdriver.Chrome()
            self.driver.get(self._base_url)

            # 写local storage
            # 从local_storage文件中获取HomeCredit_qa_jwt
            local_storage = yaml.safe_load(open("../config/local_storage.yaml"))
            HomeCredit_qa_jwt = local_storage["HomeCredit_qa_jwt"]
            HomeCredit_qa_customerName = local_storage["HomeCredit_qa_customerName"]
            HomeCredit_qa_customerEmail = local_storage["HomeCredit_qa_customerEmail"]

            self.driver.execute_script("localStorage.setItem(arguments[0],arguments[1]);", 'HomeCredit_qa_jwt',HomeCredit_qa_jwt)
            self.driver.execute_script("localStorage.setItem(arguments[0],arguments[1]);", 'HomeCredit_qa_customerName',HomeCredit_qa_customerName)
            self.driver.execute_script("localStorage.setItem(arguments[0],arguments[1]);", 'HomeCredit_qa_customerEmail',HomeCredit_qa_customerEmail)

            time.sleep(1)
            self.driver.get(self._base_url)

            time.sleep(1)
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
