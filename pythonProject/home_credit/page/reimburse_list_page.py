
from selenium.webdriver.common.by import By
from home_credit.page.base_page import BasePage
from home_credit.page.reimburse_detail_page import ReimburseDetailPage


class ReimburseListPage(BasePage):
    def goto_reimburse_detail_by_claimid(self,claim_id):
        ele_reimburse_detial = (By.XPATH, '//*[contains(text(),"'+claim_id+'")]')
        self.wait(5,ele_reimburse_detial)
        self.find_and_click(*ele_reimburse_detial)
        return ReimburseDetailPage(self.driver)

    def goto_reimburse_detail_by_status(self,status):
        ele_reimburse_detail = (By.XPATH, '//*[contains(text(),"'+status+'")]')
        self.wait(5, ele_reimburse_detail)
        reimburse_list = self.find_list(*ele_reimburse_detail)
        reimburse_list[0].click()
        return ReimburseDetailPage(self.driver)




