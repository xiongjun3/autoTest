from selenium.webdriver.common.by import By
from home_credit.page.base_page import BasePage


class ClaimDetailPage(BasePage):

    def approve(self,benefit):
        #点击approve
        ele_approve = (By.XPATH, '//*[@class="ant-card-extra"]/div/div[1]')
        self.wait(5,ele_approve)
        self.find_and_click(*ele_approve)
        # 输入benefit
        ele_daily_hospital_benefit = (By.ID, "daily_hospital")
        self.wait(5,ele_daily_hospital_benefit)
        self.find_and_send(*ele_daily_hospital_benefit,benefit)
        # submit提交
        self.find_and_click(By.XPATH, '//*[contains(text(),"Submit")]')
        # 检查detail的benefit
        ele_benefit = (By.XPATH, '//*[contains(text(),"Daily Hospital Income Benefit (sickness and accident):")]/span/div/div/span[2]/span[1]')
        self.wait(5,ele_benefit)
        benefit_income = int(self.find(*ele_benefit).text)
        return benefit_income

    def reject(self,comment):
        # 点击reject
        ele_reject = (By.XPATH, '//*[@class="ant-card-extra"]/div/div[2]')
        self.wait(5,ele_reject)
        self.find_and_click(*ele_reject)
        # 输入 reason
        ele_daily_hospital_benefit = (By.ID, "comment")
        self.wait(5,ele_daily_hospital_benefit)
        self.find_and_send(*ele_daily_hospital_benefit,comment)
        # submit提交
        self.find_and_click(By.XPATH, '//*[contains(text(),"Submit")]')
        # 检查detail的reason
        ele_reason = (By.XPATH, '//*[contains(text(),"History")]/../../../../../../div[2]/div/div/div[4]/span')
        self.wait(5,ele_reason)
        reason = self.find(*ele_reason).text
        return reason



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

    def check_item_value(self,role,item):
        ele_item = (By.XPATH,'//*[contains(text(),"'+role+'")]/../../../../../..//*[contains(text(),"'+item+'")]/../../span')
        self.wait(5,ele_item)
        content = self.find(*ele_item).text
        return content

    def check_upload_file(self,item):
        ele_picture = (By.XPATH,'//*[contains(text(),"'+item+'")]/../../div[2]/span')
        self.wait(5,ele_picture)
        self.find_and_click(*ele_picture)