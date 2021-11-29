import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from customer_portal.page_object.base_page import BasePage


class ClaimFormPage(BasePage):
    def submit_claim_form(self):
        # 展开id_type下拉列表
        ele_id_type_drop = (By.XPATH, '//input[@id="insured_identificationType"]/../../..')
        self.wait(5,ele_id_type_drop)
        self.find_and_click(*ele_id_type_drop)
        #选择id_type
        ele_id_type = (By.CSS_SELECTOR, "[label='National ID']")
        self.wait(5, ele_id_type)
        self.find_and_click(*ele_id_type)
        # 输入id_no
        self.find_and_send(By.XPATH, '//*[@id="insured_identificationNumber"]', "123456")
        # 点击continue
        self.find_and_click(By.XPATH, '//button[@class="ant-btn ant-btn-primary igloo-step-button igloo-button"]')
        # 展开关系下拉列表
        self.find_and_click(By.XPATH, '//input[@id="claimant_relationshipType"]/../../..')
        #选择关系类型
        ele_id_type = (By.CSS_SELECTOR, "[label='Self']")
        self.wait(5, ele_id_type)
        self.find_and_click(*ele_id_type)
        # 点击continue
        self.find_and_click(By.XPATH, '//button[@class="ant-btn ant-btn-primary igloo-step-button igloo-button"]')
        # 选择benefit
        self.find_and_click(By.XPATH, '//*[@value="daily_hospital"]')
        # 上传文件Hospital Certificate
        self.find_and_send(By.XPATH, '//input[@id="benefit_hospitalCertificate"]',"/Users/xiongjun/Pictures/123.jpg")
        # 上传文件SOA from the Hospital
        self.find_and_send(By.XPATH, '//input[@id="benefit_hospitalSoa"]',"/Users/xiongjun/Pictures/123.jpg")
        time.sleep(5)
        # 点击continue
        self.find_and_click(By.XPATH, '//button[@class="ant-btn ant-btn-primary igloo-step-button igloo-button"]')
        # 输入account name
        self.find_and_send(By.XPATH,'//input[@id="reimbursement_accountName"]',"xiongjun")
        # 输入account no
        self.find_and_send(By.XPATH,'//input[@type="tel"]',"123456789")
        # 输入bank name
        self.find_and_send(By.XPATH,'//input[@id="reimbursement_bankName"]',"china bank")
        # 点击continue
        self.find_and_click(By.XPATH, '//button[@class="ant-btn ant-btn-primary igloo-step-button igloo-button"]')
        # 勾选协议
        self.find_and_click(By.XPATH, '//input[@type="checkbox"]')
        # 点击submit
        self.find_and_click(By.XPATH, '//button[@type="submit"]')

        #提交成功页面，claim id
        ele_claim_id=(By.XPATH, '//*[contains(text(),"Claim ID:")]')
        self.wait(5,ele_claim_id)
        claim_id_string = self.find(*ele_claim_id).text
        print(claim_id_string)
        claim_id=claim_id_string[10:]
        print(claim_id)


        # 点击进入claim list页面
        self.find_and_click(By.XPATH, '//*[contains(text(),"Go to Claim Overview")]')

        # 检查claim列表页第一行是刚刚创建的claim
        time.sleep(2)
        # ele_claim_id_first = (By.XPATH, '//*[contains(text(),"'+claim_id+'")]')
        # self.wait(5,ele_claim_id_first)
        self.find(By.XPATH, '//*[contains(text(),"'+claim_id+'")]')

        return claim_id













        time.sleep(5)







        time.sleep(5)






