import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from home_credit.page.base_page import BasePage
from home_credit.page.claim_detail_page import ClaimDetailPage


class ClaimListPage(BasePage):
    def goto_claim_detail_by_claimid(self,claim_id):
        ele_claim_detial = (By.XPATH, '//*[contains(text(),"' + claim_id + '")]')
        self.wait(5,ele_claim_detial)
        self.find_and_click(*ele_claim_detial)
        return ClaimDetailPage(self.driver)

    def goto_claim_detail_by_status(self,claim_status):
        ele_claim_detail = (By.XPATH,'//*[contains(text(),"'+claim_status+'")]')
        self.wait(5,ele_claim_detail)
        cliam_list = self.find_list(*ele_claim_detail)
        cliam_list[0].click()
        return ClaimDetailPage(self.driver)


    def search_by_claimid(self,claimid):
        ele_input = (By.XPATH, '//*[@placeholder="Search by claim ID, COC No."]')
        # 显示等待
        self.wait(5,ele_input)
        input = self.find(*ele_input)
        # 向搜索框输入传入的claimid
        input.send_keys(claimid)
        # 回车
        input.send_keys(Keys.ENTER)
        time.sleep(5)
        # 找到搜索后的第一行的claimid
        ele_claimid = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[1]/td[1]')
        self.wait(5,ele_claimid)
        text = self.find(*ele_claimid).text
        return text

    def search_by_coc_no(self,coc_no):
        ele_input = (By.XPATH, '//*[@placeholder="Search by claim ID, COC No."]')
        # 显示等待
        self.wait(5,ele_input)
        input = self.find(*ele_input)
        # 向搜索框输入传入的claimid
        input.send_keys(coc_no)
        time.sleep(1)
        # 回车
        input.send_keys(Keys.ENTER)
        time.sleep(3)
        # 找到搜索后的那一列的claimid
        ele_coc_no = (By.XPATH, '//*[@class="ant-table-tbody"]//td[2]')
        self.wait(5,ele_coc_no)
        ele_list = self.find_list(*ele_coc_no)
        print(f"ele_list========={ele_list}")
        length = len(ele_list)
        coc_no_list = []
        for i in range(length):
            coc_no = ele_list[i].text
            print(f"coc_no========={coc_no}")
            coc_no_list.append(coc_no)
        return coc_no_list

    def filter_claim_date(self,start_date,end_date):
        ele_filter = (By.XPATH, '//*[@class="ant-btn igloo-form-filter-filter-button"]')
        # 显示等待
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
        time.sleep(2)
        # 获取claim date 列表
        ele_claim_date = (By.XPATH, '//*[@class="ant-table-tbody"]/tr//td[5]')
        self.wait(5,ele_claim_date)
        list = self.find_list(*ele_claim_date)
        length = len(list)
        claim_date_list = []
        for i in range(length):
            # 循环获取列表的text属性，并拼成一个新的数组
            ele=list[i].text
            claim_date_list.append(ele)
        return claim_date_list

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



