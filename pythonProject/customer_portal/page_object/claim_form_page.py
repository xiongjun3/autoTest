import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from customer_portal.page_object.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class ClaimFormPage(BasePage):
    def submit_claim_form(self,insured_id_type,insured_id_no,relationship,claimant_first_name,claimant_middle_name,claimant_last_name,claimant_mobile_no,claimant_email,claimant_address,claimant_id_type,claimant_id_no):
        # 展开id_type下拉列表
        ele_id_type_drop = (By.XPATH, '//input[@id="insured_identificationType"]/../../..')
        self.wait(5,ele_id_type_drop)
        self.find_and_click(*ele_id_type_drop)
        #选择id_type

        #鼠标移动到下拉框隐藏的选项
        ActionChains(self.driver).move_to_element(self.find(By.CSS_SELECTOR, '[label="'+insured_id_type+'"]')).send_keys(Keys.UP).perform()
        self.find_and_click(By.CSS_SELECTOR, "[label='"+insured_id_type+"']")
        # 输入id_no
        self.find_and_send(By.XPATH, '//*[@id="insured_identificationNumber"]', insured_id_no)
        # 点击continue
        self.find_and_click(By.XPATH, '//button[@class="ant-btn ant-btn-primary igloo-step-button igloo-button"]')
        # 展开关系下拉列表
        self.find_and_click(By.XPATH, '//input[@id="claimant_relationshipType"]/../../..')
        #选择关系类型
        if relationship == "Self":
            self.find_and_click(By.CSS_SELECTOR, "[label='"+relationship+"']")
        else:
            self.find_and_click(By.CSS_SELECTOR, "[label='"+relationship+"']")
            self.find_and_send(By.ID,"claimant_firstName",claimant_first_name)
            self.find_and_send(By.ID,"claimant_middleName",claimant_middle_name)
            self.find_and_send(By.ID,"claimant_lastName",claimant_last_name)
            self.find_and_send(By.XPATH,'//input[@type="tel"]',claimant_mobile_no)
            self.find_and_send(By.ID,"claimant_email",claimant_email)
            self.find_and_send(By.ID,"claimant_address",claimant_address)
            # 点开claim_id_type
            self.find_and_click(By.ID, "claimant_identificationType")
            ActionChains(self.driver).move_to_element(self.find(By.CSS_SELECTOR, '[label="' + claimant_id_type + '"]')).send_keys(Keys.UP).perform()
            self.find_and_click(By.CSS_SELECTOR, "[label='" + claimant_id_type + "']")
            self.find_and_send(By.ID,"claimant_identificationNumber",claimant_id_no)

        #点击continue
        self.find_and_click(By.XPATH, '//button[@class="ant-btn ant-btn-primary igloo-step-button igloo-button"]')
        # 选择benefit
        self.find_and_click(By.XPATH, '//*[@value="daily_hospital"]')
        # 上传文件Hospital Certificate
        self.find_and_send(By.XPATH, '//input[@id="benefit_hospitalCertificate"]',"/Users/xiongjun/Pictures/123.jpg")
        # 上传文件SOA from the Hospital
        self.find_and_send(By.XPATH, '//input[@id="benefit_hospitalSoa"]',"/Users/xiongjun/Pictures/123.jpg")
        time.sleep(2)
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

        #提交成功页面，获取页面上的claim id
        ele_claim_id=(By.XPATH, '//*[contains(text(),"Claim ID:")]')
        self.wait(5,ele_claim_id)
        claim_id_string = self.find(*ele_claim_id).text
        print(claim_id_string)
        claim_id=claim_id_string[10:]
        print(claim_id)
        # 点击进入claim list页面
        self.find_and_click(By.XPATH, '//*[contains(text(),"Go to Claim Overview")]')

        # 检查claim列表页第一行是刚刚创建的claim，列表的claim_id和成功页面的claim_id一样
        time.sleep(1)
        self.find(By.XPATH, '//*[contains(text(),"'+claim_id+'")]')
        return claim_id

    def view_coc(self,coc_no):
        ele_view_coc = (By.XPATH, '//*[contains(text(),"'+coc_no+'")]/../div/span')
        self.wait(5,ele_view_coc)
        self.find_and_click(*ele_view_coc)
        # 关闭coc文件
        ele_close = (By.XPATH, '//button[@class="ant-modal-close"]')
        self.wait(5,ele_close)
        self.find_and_click(*ele_close)

    def view_coverage_check_benefit(self,benefit):
        ele_view_coverage = (By.XPATH, '//*[contains(text(),"View Coverage")]')
        self.wait(5, ele_view_coverage)
        self.find_and_click(*ele_view_coverage)
        # 检查Accidental Burial Benefit
        ele_amount = (By.XPATH,'//*[contains(text(),"'+benefit+'")]/../span[1]/div/div/span[2]/span[1]')
        self.wait(5,ele_amount)
        amount = self.find(*ele_amount).text
        decimal = self.find(By.XPATH,'//*[contains(text(),"'+benefit+'")]/../span[1]/div/div/span[2]/span[2]').text
        currency = self.find(By.XPATH,'//*[contains(text(),"'+benefit+'")]/../span[1]/div/div/span[1]').text

        if benefit == "Accidental Burial Benefit":
            content = currency + amount + decimal
        if benefit == "Burial Cash Assistance due to Natural sickness":
            content = currency + amount + decimal
        if benefit == "Daily Hospital Income Benefit (sickness and accident)":
            unit = self.find(By.XPATH, '//*[contains(text(),"' + benefit + '")]/../span[2]').text
            note = self.find(By.XPATH, '//*[contains(text(),"' + benefit + '")]/../span[3]').text
            content = currency + amount + decimal + " " + unit + " " + note
        if benefit == "Emergency Room Assistance (sickness and accident)":
            note = self.find(By.XPATH, '//*[contains(text(),"' + benefit + '")]/../span[2]').text
            content = currency + amount + decimal + note
        return content
        # 关闭coverage文件
        self.find_and_click(By.XPATH, '//*[@class="igloo-modal-footer-btns"]')

    def check_category(self):
        ele_category = (By.XPATH,'//*[contains(text(),"Category")]/../../div[2]/span/div/span')
        self.wait(5,ele_category)
        category = self.find(*ele_category).text
        return category

    def check_item(self,item):
        ele_item = (By.XPATH,'//*[contains(text(),"'+item+'")]/../../div[2]/span')
        self.wait(5,ele_item)
        content = self.find(*ele_item).text
        return content















        time.sleep(5)







        time.sleep(5)






