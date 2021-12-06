import time
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
        self.wait(5,ele_open_new_page)
        self.find_and_click(*ele_open_new_page)
        time.sleep(1)

    def check_item_value(self,item):
        ele_item = (By.XPATH, '//*[contains(text(),"'+item+'")]/../../span')
        self.wait(5,ele_item)
        content = self.find(*ele_item).text
        return content

    def goto_polocy_list(self):
        ele_back = (By.XPATH, '//*[@class="igloo-typography-body1 word-wrap backText___31t64"]')
        # 显示等待
        self.wait(5,ele_back)
        self.find_and_click(*ele_back)





