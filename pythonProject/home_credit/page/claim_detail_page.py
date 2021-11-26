from selenium.webdriver.common.by import By
from home_credit.page.base_page import BasePage


class ClaimDetailPage(BasePage):

    def check_coc_no(self):
        ele_coc_no = (By.XPATH,'//*[contains(text(), "COC No.")]/../../span')
        self.wait(5,ele_coc_no)
        coc_no = self.find(*ele_coc_no).text
        return coc_no

    def check_claim_date(self):
        ele_coc_no = (By.XPATH,'//*[contains(text(), "Claim Date")]/../../span')
        self.wait(5,ele_coc_no)
        claim_date = self.find(*ele_coc_no).text
        return claim_date

    def check_full_name(self):
        ele_full_name = (By.XPATH,'//*[contains(text(), "Full Name")]/../../span')
        self.wait(5,ele_full_name)
        full_name = self.find(*ele_full_name).text
        return full_name