#  -*-  coding: utf-8  -*-
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import yaml


class TestLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def test_get_admin_token(self):
        self.driver.get("https://dashboard.qa.axinan.com/platform/policy")
        time.sleep(2)
        self.driver.find_element(By.ID, "email").send_keys("jun.xiong@iglooinsure.com")
        locator = (By.ID, "password")
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.CLASS_NAME, "igloo-login-button").click()
        time.sleep(2)
        self.driver.get("https://dashboard.qa.axinan.com/platform/policy")
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="HomeCredit"]/div/div/div[2]/div[3]/div/div/img').click()


        #获取cookie
        cookie = self.driver.get_cookies()
        print(f"================cookie: {cookie}")
        with open("./cookie.yaml","w") as f:
            yaml.safe_dump(cookie, f)

    def test_add_cookie(self):
        self.driver.get("https://dashboard.qa.axinan.com/platform/policy")
        # 从cookie文件中获取cookie
        cookie = yaml.safe_load(open("cookie.yaml"))
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(3)
        self.driver.get("https://dashboard.qa.axinan.com/platform/policy")







