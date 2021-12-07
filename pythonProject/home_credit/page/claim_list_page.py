import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from home_credit.page.base_page import BasePage
from home_credit.page.claim_detail_page import ClaimDetailPage


class ClaimListPage(BasePage):
    def goto_claim_detail_by_claimid(self,claim_id):
        # 先搜索出来再进入详情页，不然如果再第二页就会报错
        ele_search = (By.XPATH, '//*[@class="igloo-form-filter"]/span/input')
        self.wait(5,ele_search)
        search_input = self.find(*ele_search)
        search_input.send_keys(claim_id)
        search_input.send_keys(Keys.ENTER)

        ele_claim_detail = (By.XPATH, '//*[contains(text(),"' + claim_id + '")]')
        self.wait(5,ele_claim_detail)
        self.find_and_click(*ele_claim_detail)
        return ClaimDetailPage(self.driver)

    def goto_claim_detail_by_status(self,claim_status):
        ele_claim_detail = (By.XPATH,'//*[contains(text(),"'+claim_status+'")]')
        self.wait(5,ele_claim_detail)
        cliam_list = self.find_list(*ele_claim_detail)
        cliam_list[0].click()
        return ClaimDetailPage(self.driver)

    def search_by_claim_id(self,claim_id):
        # 搜索结果claim_id的定位
        content1,content2,content3,content4,content5 = self.search(claim_id)
        return content1, content2, content3, content4, content5


    def search_by_coc_no(self,coc_no):
        ele_input = (By.XPATH, '//*[@placeholder="Search by claim ID, COC No."]')
        self.wait(5,ele_input)
        input = self.find(*ele_input)
        input.send_keys(coc_no)
        time.sleep(1)
        # 回车
        input.send_keys(Keys.ENTER)
        time.sleep(3)
        # 找到搜索后的那一列的coc_no
        ele_coc_no = (By.XPATH, '//*[@class="ant-table-tbody"]//td[2]')
        self.wait(5,ele_coc_no)
        ele_list = self.find_list(*ele_coc_no)
        length = len(ele_list)
        coc_no_list = []
        for i in range(length):
            coc_no = ele_list[i].text
            coc_no_list.append(coc_no)
        return coc_no_list

    def filter_claim_date(self,start_date,end_date):
        claim_date_list = self.filter_date(start_date,end_date)
        return claim_date_list

    def filter_policy_status(self,claim_status):
        date_list = self.filter_status(claim_status)
        return date_list




