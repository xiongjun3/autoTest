import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from home_credit.page.base_page import BasePage
from selenium.webdriver.common.by import By

class PolicyDetailPage(BasePage):
    def click_view_coc(self):
        ele_view_coc = (By.XPATH, '//*[@class="ant-row igloo-form-card-container-group"]/div[4]/a')
        # 显示等待
        self.wait(5,ele_view_coc)
        # 点击review coc
        self.find_and_click(*ele_view_coc)
        time.sleep(1)

        ele_open_new_page = (By.XPATH, '//*[@class="ant-modal-title"]/div/span')
        # 显示等待
        self.wait(5,ele_open_new_page)
        self.find_and_click(*ele_open_new_page)
        time.sleep(1)

    def goto_polocy_list(self):
        ele_back = (By.XPATH, '//*[@class="igloo-typography-body1 word-wrap backText___31t64"]')
        # 显示等待
        self.wait(5,ele_back)
        self.find_and_click(*ele_back)

    def check_loan_term(self):
        ele_loanterm = (By.XPATH,'//*[contains(text(), "Loan Term")]/../../span')
        self.wait(5,ele_loanterm)
        loan_term = self.find(*ele_loanterm).text
        return loan_term

    def check_coverage_start_date(self):
        ele_coverage_start_date= (By.XPATH,'//*[contains(text(), "Coverage Start Date")]/../../span')
        self.wait(5,ele_coverage_start_date)
        coverage_start_date = self.find(*ele_coverage_start_date).text
        return coverage_start_date

    def check_coverage_end_date(self):
        ele_coverage_end_date = (By.XPATH,'//*[contains(text(), "Coverage End Date")]/../../span')
        self.wait(5,ele_coverage_end_date)
        coverage_end_date = self.find(*ele_coverage_end_date).text
        return coverage_end_date

    def check_fullname(self):
        ele_fullname = (By.XPATH,'//*[contains(text(), "Full Name")]/../../span')
        self.wait(5,ele_fullname)
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_fullname))
        full_name = self.find(*ele_fullname).text
        return full_name

    def check_gender(self):
        ele_gender = (By.XPATH,'//*[contains(text(), "Gender")]/../../span')
        self.wait(5,ele_gender)
        gender = self.find(*ele_gender).text
        return gender

    def check_birthdate(self):
        ele_birthdate = (By.XPATH,'//*[contains(text(), "Date of Birth")]/../../span')
        self.wait(5,ele_birthdate)
        birthdate = self.find(*ele_birthdate).text
        return birthdate

    def check_mobile_number(self):
        ele_mobile_number = (By.XPATH,'//*[contains(text(), "Mobile Number")]/../../span')
        self.wait(5,ele_mobile_number)
        mobile_bumber = self.find(*ele_mobile_number).text
        return mobile_bumber

    def check_email(self):
        ele_email= (By.XPATH,'//*[contains(text(), "Email")]/../../span')
        self.wait(5,ele_email)
        email = self.find(*ele_email).text
        return email

    def check_address(self):
        ele_address= (By.XPATH,'//*[contains(text(), "Address")]/../../span')
        self.wait(5,ele_address)
        address = self.find(*ele_address).text
        return address






