import time
from home_credit.page.base_page import BasePage
from selenium.webdriver.common.by import By
from home_credit.page.claim_list_page import ClaimListPage
from home_credit.page.policy_detail_page import PolicyDetailPage
from selenium.webdriver.common.keys import Keys

from home_credit.page.reimburse_list_page import ReimburseListPage


class PolicyPage(BasePage):

    def goto_policy_detail(self,policy_id):
        # 先搜索出来再进入详情页，不然如果再第二页就会报错
        ele_search = (By.XPATH, '//*[@class="igloo-form-filter"]/span/input')
        self.wait(5, ele_search)
        search_input = self.find(*ele_search)
        search_input.send_keys(policy_id)
        search_input.send_keys(Keys.ENTER)

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

    def goto_reimburse_list(self):
        ele_reimburse_list = (By.XPATH, '//*[@title="Reimburse"]/span')
        # 显示等待
        self.wait(5,ele_reimburse_list)
        self.find_and_click(*ele_reimburse_list)
        return ReimburseListPage(self.driver)

    def search_by_coc_no(self,coc_no):
        content1,content2,content3,content4,content5 = self.search(coc_no)
        return content1,content2,content3,content4,content5


    def filter_policy_status(self,policy_status):
        date_list = self.filter_status(policy_status)
        return date_list

    def filter_start_date(self,start_date,end_date):
        start_date_list = self.filter_date(start_date,end_date)
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
        # 关闭上传队列
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







































