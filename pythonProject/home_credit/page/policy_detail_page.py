import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from home_credit.page.base_page import BasePage
from selenium.webdriver.common.by import By

class PolicyDetailPage(BasePage):
    def click_view_coc(self):
        ele_view_coc = (By.XPATH, '//*[@class="ant-row igloo-form-card-container-group"]/div[4]/a')
        # 显示等待
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_view_coc))
        # 点击review coc
        self.find_and_click(*ele_view_coc)
        time.sleep(1)

        ele_open_new_page = (By.XPATH, '//*[@class="ant-modal-title"]/div/span')
        # 显示等待
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_open_new_page))
        self.find_and_click(*ele_open_new_page)
        time.sleep(1)

    def goto_polocy_list(self):
        ele_back = (By.XPATH, '//*[@class="igloo-typography-body1 word-wrap backText___31t64"]')
        # 显示等待
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_back))
        self.find_and_click(*ele_back)

    def check_loan_term(self):
        ele_loanterm = (By.XPATH,'//*[contains(text(), "Loan Term")]/../../span')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_loanterm))
        loanterm_item = self.find(*ele_loanterm)
        loan_term = loanterm_item.text
        return loan_term

    def check_coverage_start_date(self):
        ele_coverage_start_date= (By.XPATH,'//*[contains(text(), "Coverage Start Date")]/../../span')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_coverage_start_date))
        coverage_start_date_item = self.find(*ele_coverage_start_date)
        coverage_start_date = coverage_start_date_item.text
        return coverage_start_date

    def check_coverage_end_date(self):
        ele_coverage_end_date = (By.XPATH,'//*[contains(text(), "Coverage End Date")]/../../span')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_coverage_end_date))
        coverage_end_date_item = self.find(*ele_coverage_end_date)
        coverage_end_date = coverage_end_date_item.text
        return coverage_end_date

    def check_fullname(self):
        ele_fullname = (By.XPATH,'//*[contains(text(), "Full Name")]/../../span')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_fullname))
        fullname_item = self.find(*ele_fullname)
        full_name = fullname_item.text
        return full_name

    def check_gender(self):
        ele_gender = (By.XPATH,'//*[contains(text(), "Gender")]/../../span')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_gender))
        gender_item = self.find(*ele_gender)
        gender = gender_item.text
        return gender

    def check_birthdate(self):
        ele_birthdate = (By.XPATH,'//*[contains(text(), "Date of Birth")]/../../span')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_birthdate))
        birthdate_item = self.find(*ele_birthdate)
        birthdate = birthdate_item.text
        return birthdate

    def check_mobile_number(self):
        ele_mobile_number = (By.XPATH,'//*[contains(text(), "Mobile Number")]/../../span')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_mobile_number))
        mobile_number_item = self.find(*ele_mobile_number)
        mobile_bumber = mobile_number_item.text
        return mobile_bumber

    def check_email(self):
        ele_email= (By.XPATH,'//*[contains(text(), "Email")]/../../span')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_email))
        email_item = self.find(*ele_email)
        email = email_item.text
        return email

    def check_address(self):
        ele_address= (By.XPATH,'//*[contains(text(), "Address")]/../../span')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_address))
        address_item = self.find(*ele_address)
        address = address_item.text
        return address






