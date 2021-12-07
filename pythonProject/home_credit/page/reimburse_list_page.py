from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from home_credit.page.base_page import BasePage
from home_credit.page.reimburse_detail_page import ReimburseDetailPage


class ReimburseListPage(BasePage):
    def goto_reimburse_detail_by_claimid(self,claim_id):
        # 先搜索出来再进入详情页，不然如果再第二页就会报错
        ele_search = (By.XPATH, '//*[@class="igloo-form-filter"]/span/input')
        self.wait(5, ele_search)
        search_input = self.find(*ele_search)
        search_input.send_keys(claim_id)
        search_input.send_keys(Keys.ENTER)

        ele_reimburse_detail = (By.XPATH, '//*[contains(text(),"'+claim_id+'")]')
        self.wait(5,ele_reimburse_detail)
        self.find_and_click(*ele_reimburse_detail)
        return ReimburseDetailPage(self.driver)

    def goto_reimburse_detail_by_status(self,status):
        ele_reimburse_detail = (By.XPATH, '//*[contains(text(),"'+status+'")]')
        self.wait(5, ele_reimburse_detail)
        reimburse_list = self.find_list(*ele_reimburse_detail)
        reimburse_list[0].click()
        return ReimburseDetailPage(self.driver)


    def search_by_claim_id(self,claim_id):
        content1,content2,content3,content4,content5 = self.search(claim_id)
        return content1, content2, content3, content4, content5

    def filter_approved_date(self,start_date,end_date):
        approved_date_list = self.filter_date(start_date,end_date)
        return approved_date_list

    def filter_reimbursement_status(self,status):
        reimbursement_status_list = self.filter_status(status)
        return reimbursement_status_list






