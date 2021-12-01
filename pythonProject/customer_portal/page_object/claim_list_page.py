import time
from selenium.webdriver.common.by import By
from customer_portal.page_object.base_page import BasePage
from customer_portal.page_object.claim_form_page import ClaimFormPage


class ClaimListPage(BasePage):
    def goto_claim_form(self):
        ele_claim = (By.XPATH, '//button[@class="ant-btn ant-btn-primary igloo-pa-card-page-head-btn"]')
        self.wait(5,ele_claim)
        self.find_and_click(*ele_claim)

        return ClaimFormPage(self.driver)

    def cancel_claim(self,claim_id):
        ele_claim_processing_claim_list = (By.XPATH,'//*[contains(text(),"CLAIM PROCESSING")]/../../../td[2]')
        self.wait(5,ele_claim_processing_claim_list)
        li = self.find_list(*ele_claim_processing_claim_list)
        length = len(li)
        claim_processing_claim_list = []
        for i in range(length):
            claim_id = li[i].text
            claim_processing_claim_list.append(claim_id)

        ele_cancel = (By.XPATH, '//td[contains(text(),"'+claim_processing_claim_list[0]+'")]/../td[6]/div')
        self.wait(5,ele_cancel)
        self.find_and_click(*ele_cancel)
        #
        ele_cancel_confirm = (By.XPATH,'//div[@class="ant-modal-footer"]/button[1]')
        self.wait(5,ele_cancel_confirm)
        self.find_and_click(*ele_cancel_confirm)


