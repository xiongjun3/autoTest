import configparser
import os
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver



class TestLogin:
    def get_config(self):
        # python3里面自带configparser模块来读取ini文件
        # 读取iselenium中的Chrome driver的路径，不然执行的时候会报错
        config = configparser.ConfigParser()
        # 用户的主目录
        homepath = os.environ['HOME']
        # os.path.join用来拼接，最终是iselenium.ini文件的路径
        configpath = os.path.join(homepath, 'iselenium.ini')
        config.read(configpath)
        # config.read(os.path.join(os.environ['HOME'],'iselenium.ini'))
        return config

    def set_config(self):
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

        self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'),
                                       options=chrome_options)

    def test_login(self):
        url1 = "https://homecredit.qa.axinan.com/pc/login?id=bb806618-e0b2-4f1e-bb8c-24d208ce5aae"
        self.driver.get(url1)
        time.sleep(2)
        locator = (By.XPATH, '//*[@class="ant-btn ant-btn-link igloo-otp-extra igloo-button"]')
        WebDriverWait(self.driver, 10, 0.5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(By.XPATH, '//*[@class="ant-btn ant-btn-link igloo-otp-extra igloo-button"]').click()
        windows_handles = self.driver.window_handles
        print(f"---------------windows_handles:{windows_handles}")

        time.sleep(2)

        #打开邮箱获取验证码
        url2 = "https://mail.google.com/mail/u/0/#inbox"
        self.driver.get(url2)
        ele_email = (By.ID, "identifierId")
        WebDriverWait(self.driver, 10, 0.5).until(expected_conditions.element_to_be_clickable(ele_email))
        # 输入邮箱
        self.driver.find_element(By.ID, "identifierId").send_keys("jun.xiong@iglooinsure.com")
        # 点击下一步
        self.driver.find_element(By.XPATH,
                            '//*[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b"]').click()
        time.sleep(2)
        # 输入密码
        self.driver.find_element(By.NAME, "password").send_keys("xj425123")
        # 点击下一步登陆
        self.driver.find_element(By.ID, "passwordNext").click()

        time.sleep(5)
        ele_email_1 = (By.XPATH, '//*[@id=":1k"]/tbody/tr[1]')
        WebDriverWait(self.driver, 10, 0.5).until(expected_conditions.element_to_be_clickable(ele_email_1))
        # 进入收件箱，点击进入第一封邮件详情
        self.driver.find_element(By.XPATH, '//*[@id=":1k"]/tbody/tr[1]').click()
        time.sleep(3)

        OTP_item = self.driver.find_element(By.XPATH,
                                       '//*[@style="font-weight:700;font-size:32px;line-height:37.5px;margin-bottom:16px"]')

        OPT = OTP_item.get_attribute("textContent")
        OPT_code = OPT.strip()
        print(f"---------------OPT:{OPT_code}")

        # 获取到验证码后，登陆
        self.driver.get(url1)
        ele_opt = (By.ID, "otp")
        WebDriverWait(self.driver, 20, 0.5).until(expected_conditions.element_to_be_clickable(ele_opt))

        self.driver.find_element(By.ID, "otp").send_keys(OPT_code)
        self.driver.find_element(By.XPATH, '//*[@class="ant-btn ant-btn-primary igloo-login-button"]').click()
        time.sleep(2)

        # 获取local_storage
        HomeCredit_qa_jwt = self.driver.execute_script('return window.localStorage.getItem("HomeCredit_qa_jwt");', "HomeCredit_qa_jwt")
        HomeCredit_qa_customerName = self.driver.execute_script('return window.localStorage.getItem("HomeCredit_qa_customerName");', "HomeCredit_qa_customerName")
        HomeCredit_qa_customerEmail = self.driver.execute_script('return window.localStorage.getItem("HomeCredit_qa_customerEmail");', "HomeCredit_qa_customerEmail")
        local_storage = {"HomeCredit_qa_jwt":HomeCredit_qa_jwt, "HomeCredit_qa_customerName":HomeCredit_qa_customerName, "HomeCredit_qa_customerEmail":HomeCredit_qa_customerEmail}

        with open("local_storage.yaml", "w") as f:
            # 第一个参数是要写入的数据
            yaml.safe_dump(local_storage, f)

    def teardown_class(self):
        self.driver.quit()









