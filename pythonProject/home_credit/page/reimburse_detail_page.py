import time

from selenium.webdriver.common.by import By
from home_credit.page.base_page import BasePage


class ReimburseDetailPage(BasePage):
    def check_item_value(self,item):
        ele_item = (By.XPATH,'//*[contains(text(),"'+item+'")]/../../span')
        self.wait(5,ele_item)
        content = self.find(*ele_item).text
        return content

    def complete(self,date,payment_id):
        ele_complete = (By.XPATH, '//*[contains(text(),"Complete")]/..')
        self.wait(5,ele_complete)
        self.find_and_click(*ele_complete)
        # 点击日历弹框
        ele_date = (By.XPATH,'//*[@id="reimbursement_date"]/../..')
        self.wait(5,ele_date)
        self.find_and_click(*ele_date)
        time.sleep(1)
        # 移除input日历输入框的只读属性并输入日期
        self.move_readonly("2")
        self.find_and_send(By.ID,"reimbursement_date",date)
        self.find_and_send(By.ID,"transaction_id",payment_id)
        self.find_and_click(By.XPATH,'//*[contains(text(),"Submit")]/..')
        # check complete后的状态是REIMBURSED
        ele_reimbursement_status = (By.XPATH, '//*[contains(text(),"Reimbursement Status")]/../../../div[1]/div/span')
        self.wait(5,ele_reimbursement_status)
        reimbursement_status_result = self.find(*ele_reimbursement_status).text
        return reimbursement_status_result

    def check_history_item(self,n):
        ele_item = (By.XPATH, '//*[contains(text(),"History")]/../../../../../../div[2]/div/div/div['+n+']/div/span/../../span')
        self.wait(5,ele_item)
        content = self.find(*ele_item).text
        return content

