import os
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from home_credit.page.base_page import BasePage
from selenium.webdriver.common.by import By
from home_credit.page.policy_detail_page import PolicyDetailPage
from selenium.webdriver.common.keys import Keys


class PolicyPage(BasePage):
    def goto_policy_detail(self,policy_id):
        time.sleep(3)
        ele_policy_detial = (By.XPATH, '//*[contains(text(),"'+policy_id+'")]')
        # 显示等待
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_policy_detial))
        self.find_and_click(*ele_policy_detial)
        return PolicyDetailPage(self.driver)

    def search(self,displayid):
        locator = (By.XPATH,'//*[@class="ant-input-affix-wrapper igloo-form-filter-default-input"]/input')
        #显示等待
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(locator))
        input = self.driver.find_element(By.XPATH,'//*[@class="ant-input-affix-wrapper igloo-form-filter-default-input"]/input')
        # 向搜索框输入传入的displayid
        input.send_keys(displayid)
        # 回车
        input.send_keys(Keys.ENTER)
        time.sleep(5)
        # 找到搜索后的第一列的policyid
        element = self.driver.find_element(By.XPATH,'//*[@class="ant-table-tbody"]/tr[1]/td[1]')
        text = element.text
        return text
        time.sleep(1)

    def filter_policy_status(self,policy_status):
        locator = (By.XPATH, '//*[@class="ant-btn igloo-form-filter-filter-button"]')
        # 显示等待
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(locator))
        filter = self.driver.find_element(By.XPATH,'//*[@class="ant-btn igloo-form-filter-filter-button"]')
        # 点击filter按钮
        filter.click()
        time.sleep(1)
        # 点击protected状态
        ele_policy_status = (By.XPATH, '//*[@value="'+policy_status+'"]')
        self.find_and_click(*ele_policy_status)
        # self.driver.find_element(By.XPATH,'//*[@class="ant-row"]/div[1]/label/span[1]').click()
        time.sleep(1)
        # 点击apply按钮
        self.driver.find_element(By.XPATH,'//*[@class="igloo-form-filter-drop-down-footer"]/div/div[2]').click()
        time.sleep(2)
        # 获取policy状态列表
        ele_list = self.driver.find_elements(By.XPATH,'//*[@class="igloo-typography-status word-wrap"]')
        len(ele_list)
        lenth = len(ele_list)
        policy_status_list = []
        for i in range(lenth):
            policy_status = ele_list[i].text
            policy_status_list.append(policy_status)
        return policy_status_list

    def filter_start_date(self,start_date,end_date):
        locator = (By.XPATH, '//*[@class="ant-btn igloo-form-filter-filter-button"]')
        # 显示等待
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(locator))
        filter = self.driver.find_element(By.XPATH, '//*[@class="ant-btn igloo-form-filter-filter-button"]')
        # 点击filter按钮
        filter.click()
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
        time.sleep(2)
        # 获取start date 列表
        ele_startdate = (By.XPATH, '//*[@class="ant-table-tbody"]/tr//td[5]')
        WebDriverWait(self.driver, 30, 0.5).until(expected_conditions.element_to_be_clickable(ele_startdate))
        start_list = self.find_list(*ele_startdate)
        lenth = len(start_list)
        start_date_list = []
        for i in range(lenth):
            # 循环获取列表的text属性，并拼成一个新的数组
            ele=start_list[i].text
            start_date_list.append(ele)
        return start_date_list

    def import_enrollment(self,csvpath):
        ele_import = (By.XPATH, '//*[@class="igloo-typography-h4 word-wrap"]')
        # 显示等待
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_import))
        self.find_and_click(*ele_import)
        time.sleep(1)

        # 上传文件
        ele_brower = (By.XPATH, '//*[@class="ant-upload ant-upload-btn"]/input')
        upload = self.find(*ele_brower)

        upload.send_keys(csvpath)
        time.sleep(2)
        # 查找上传的文件名称
        ele_file_name = (By.XPATH, '//*[@title="tmpl_wrong_format_birth.csv"]')
        WebDriverWait(self.driver, 30, 0.5).until(expected_conditions.element_to_be_clickable(ele_file_name))
        self.find(*ele_file_name).get_attribute('text')

        # 查找error report元素
        ele_error_report = (By.XPATH, '//*[@class="ant-btn ant-btn-link  igloo-button"]')
        self.find(*ele_error_report)

        # 关闭弹框
        ele_close_button = (By.XPATH, '//*[@class="ant-modal-close-x"]')
        self.find_and_click(*ele_close_button)
        time.sleep(1)

        #关闭上传队列
        ele_importing_quene = (By.XPATH, '//*[@class="igloo-admin-upload-float-header-close igloo-icon"]')
        self.find_and_click(*ele_importing_quene)
        time.sleep(1)
        ele_close = (By.XPATH, '//*[@class="ant-btn ant-btn-primary"]')
        self.find_and_click(*ele_close)

    def logout(self):
        time.sleep(5)
        ele_email = (By.XPATH, '//*[@class="ant-dropdown-trigger dropdown___19oDc"]/span[3]')
        # 显示等待
        WebDriverWait(self.driver, 10, 0.5).until(expected_conditions.element_to_be_clickable(ele_email))
        self.find_and_click(*ele_email)

        ele_logout = (By.XPATH, '//*[@class="ant-dropdown ant-dropdown-placement-bottomLeft "]/div/div[3]')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_logout))

        self.find_and_click(*ele_logout)







































