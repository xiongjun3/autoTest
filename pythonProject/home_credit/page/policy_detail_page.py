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






