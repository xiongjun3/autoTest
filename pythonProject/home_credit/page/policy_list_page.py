import time
from home_credit.page.base_page import BasePage
from selenium.webdriver.common.by import By
from home_credit.page.claim_list_page import ClaimListPage
from home_credit.page.policy_detail_page import PolicyDetailPage
from selenium.webdriver.common.keys import Keys

from home_credit.page.reimburse_list_page import ReimburseListPage


class PolicyPage(BasePage):

    def goto_policy_detail(self,policy_id):
        # 将policyid传进xpath里
        ele_policy_detial = (By.XPATH, '//*[contains(text(),"'+policy_id+'")]')
        # 显示等待
        self.wait(5,ele_policy_detial)
        self.find_and_click(*ele_policy_detial)
        return PolicyDetailPage(self.driver)

    def goto_claim_list(self):
        # cliam tab的xpath定位
        ele_claim_list = (By.XPATH, '//*[contains(text(),"Claim")]')
        # 显示等待
        self.wait(5,ele_claim_list)
        self.find_and_click(*ele_claim_list)
        return ClaimListPage(self.driver)

    def goto_reimbuser_list(self):
        ele_reimburse_list = (By.XPATH, '//*[@title="Reimburse"]/span')
        # 显示等待
        self.wait(5,ele_reimburse_list)
        self.find_and_click(*ele_reimburse_list)
        return ReimburseListPage(self.driver)



    def search(self,coc_no):
        locator = (By.XPATH,'//*[@class="ant-input-affix-wrapper igloo-form-filter-default-input"]/input')
        #显示等待
        self.wait(5,locator)
        input = self.driver.find_element(By.XPATH,'//*[@class="ant-input-affix-wrapper igloo-form-filter-default-input"]/input')
        # 向搜索框输入传入的displayid
        input.send_keys(coc_no)
        # 回车
        input.send_keys(Keys.ENTER)
        time.sleep(5)
        # 找到搜索后的第一行的policyid
        element_coc_no = (By.XPATH,'//*[@class="ant-table-tbody"]/tr[1]/td[1]')
        self.wait(5,element_coc_no)
        text = self.find(*element_coc_no).text
        return text

    def filter_policy_status(self,policy_status):
        locator = (By.XPATH, '//*[@class="ant-btn igloo-form-filter-filter-button"]')
        # 显示等待
        self.wait(5,locator)
        self.find_and_click(*locator)
        time.sleep(1)
        # 点击protected状态
        ele_policy_status = (By.XPATH, '//*[@value="'+policy_status+'"]')
        self.find_and_click(*ele_policy_status)
        time.sleep(1)
        # 点击apply按钮
        self.driver.find_element(By.XPATH,'//*[@class="igloo-form-filter-drop-down-footer"]/div/div[2]').click()
        time.sleep(2)
        # 获取policy状态列表
        ele_list = self.driver.find_elements(By.XPATH,'//*[@class="igloo-typography-status word-wrap"]')
        length = len(ele_list)
        policy_status_list = []
        for i in range(length):
            policy_status = ele_list[i].text
            policy_status_list.append(policy_status)
        return policy_status_list

    def filter_start_date(self,start_date,end_date):
        locator = (By.XPATH, '//*[@class="ant-btn igloo-form-filter-filter-button"]')
        # 显示等待
        self.wait(5,locator)
        self.find_and_click(*locator)
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
        self.wait(5,ele_startdate)
        start_list = self.find_list(*ele_startdate)
        length = len(start_list)
        start_date_list = []
        for i in range(length):
            # 循环获取列表的text属性，并拼成一个新的数组
            ele=start_list[i].text
            start_date_list.append(ele)
        return start_date_list

    def import_enrollment(self,csvpath):
        ele_import = (By.XPATH, '//*[@class="igloo-typography-h4 word-wrap"]')
        # 显示等待
        self.wait(5,ele_import)
        self.find_and_click(*ele_import)
        time.sleep(1)
        # 上传文件
        ele_brower = (By.XPATH, '//*[@class="ant-upload ant-upload-btn"]/input')
        upload = self.find(*ele_brower)
        upload.send_keys(csvpath)
        time.sleep(2)
        # 查找上传的文件名称
        ele_file_name = (By.XPATH, '//*[@title="tmpl_wrong_format_birth.csv"]')
        self.wait(5,ele_file_name)
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
        self.wait(5,ele_email)
        self.find_and_click(*ele_email)
        ele_logout = (By.XPATH, '//*[@class="ant-dropdown ant-dropdown-placement-bottomLeft "]/div/div[3]')
        self.wait(5,ele_logout)
        self.find_and_click(*ele_logout)







































