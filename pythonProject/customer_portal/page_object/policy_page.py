import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from customer_portal.page_object.base_page import BasePage
from customer_portal.page_object.claim_form_page import ClaimFormPage
from customer_portal.page_object.claim_list_page import ClaimListPage
from customer_portal.page_object.policy_detail_page import PolicyDetailPage


class PolicyPage(BasePage):
    # 获取policy status
    def get_policy_status(self,coc_no):
        ele_birth = (
        By.XPATH, '//*[contains(text(),"'+coc_no+'")]/../../../../../div[1]/div/div[3]/span/span')
        self.wait(5,ele_birth)
        policy_status_item = self.find(*ele_birth)
        policy_status = policy_status_item.get_attribute("textContent")
        return policy_status



    def view_coc_new_window(self,coc_no):
        # 点击view coverage
        ele_view_coc = (
            By.XPATH, '//*[contains(text(),"'+coc_no+'")]/../button')
        self.wait(5,ele_view_coc)
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_view_coc))
        self.find_and_click(*ele_view_coc)
        # 新窗口打开coc 文件
        ele_new_win = (By.XPATH, '//*[contains(text(),"Certificate of Coverage")]/span')
        self.wait(5,ele_new_win)
        self.find_and_click(*ele_new_win)

    def view_coverage(self,coc_no,benefit):
        ele_view_coverage = (
            By.XPATH, '//*[contains(text(),"'+coc_no+'")]/../../../div[2]/div[2]/button')
        self.wait(5,ele_view_coverage)
        self.find_and_click(*ele_view_coverage)

        ele_amount = (By.XPATH, '//*[contains(text(),"' + benefit + '")]/../span[1]/div/div/span[2]/span[1]')
        self.wait(5, ele_amount)
        amount = self.find(*ele_amount).text
        decimal = self.find(By.XPATH, '//*[contains(text(),"' + benefit + '")]/../span[1]/div/div/span[2]/span[2]').text
        currency = self.find(By.XPATH, '//*[contains(text(),"' + benefit + '")]/../span[1]/div/div/span[1]').text

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
        self.find_and_click(By.XPATH, '//*[@class="ant-btn ant-btn-default igloo-modal-footer-button igloo-button"]')
        time.sleep(2)





    def check_drop_name(self):
        ele_drop_name = (
            By.XPATH, '//*[@id="dropMenu"]/../span[2]')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_drop_name))
        drop_name_item = self.find(*ele_drop_name)
        drop_name = drop_name_item.get_attribute("textContent")
        return drop_name

    def check_drop_email(self):
        # 点击右上角下拉按钮
        ele_down = (By.XPATH, '//*[@id="dropMenu"]/../span[3]')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_down))
        self.find_and_click(*ele_down)

        ele_drop_email = (
            By.XPATH, '//*[@id="dropMenu"]/span[1]')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_drop_email))
        drop_email_item = self.find(*ele_drop_email)
        drop_email = drop_email_item.get_attribute("textContent")
        return drop_email

    def logout(self):
        # 点击右上角下拉按钮
        ele_down = (By.XPATH, '//*[@id="dropMenu"]/../span[3]')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_down))
        self.find_and_click(*ele_down)
        time.sleep(1)

        # 点击logout按钮
        ele_logout = (By.XPATH, '//*[@id="dropMenu"]/../div[1]/span[2]')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_logout))
        self.find_and_click(*ele_logout)

    def goto_claim_form(self,coc_no):
        ele_claim_form = (By.XPATH, '//*[contains(text(),"'+coc_no+'")]/../../../../../div[1]/button')
        self.wait(5, ele_claim_form)
        self.find_and_click(*ele_claim_form)

        ele_continue = (By.XPATH, '//*[contains(text(),"Continue")]')
        self.wait(5,ele_continue)
        self.find_and_click(*ele_continue)

        return ClaimFormPage(self.driver)

    def goto_death_claim_form(self,coc_no,death_type):
        # 点击claim now
        ele_claim_now = (By.XPATH, '//*[contains(text(),"'+coc_no+'")]/../../../../../div[1]/button')
        self.wait(5, ele_claim_now)
        self.find_and_click(*ele_claim_now)
        # 点击claim form
        ele_claim_form = (By.XPATH, '//*[contains(text(),"claim form")]')
        self.wait(5, ele_claim_form)
        self.find_and_click(*ele_claim_form)
        # 填写coc_no
        ele_coc_no = (By.XPATH, '//input[@class="ant-input igloo-input"]')
        self.wait(5, ele_coc_no)
        self.find_and_send(*ele_coc_no,coc_no)
        # 选择死亡类型
        self.find_and_click(By.XPATH, '//input[@value="'+death_type+'"]')
        # 点continue
        self.find_and_click(By.XPATH, '//*[contains(text(),"Continue")]/..')
        ele_alert = (By.XPATH,'//*[@role="alert"]/div/div/span')
        self.wait(10,ele_alert)
        content = self.find(*ele_alert).text
        print(f"alert=========={content}")
        return content

    def goto_claim_list(self):
        ele_claim_list = (By.XPATH, '//div[@class="igloo-pa-header-menu-btn false"]')
        self.wait(5,ele_claim_list)
        self.find_and_click(*ele_claim_list)
        return ClaimListPage(self.driver)

    def goto_policy_detail(self,coc_no):
        ele_policy_drop = (By.XPATH,'//*[contains(text(),"'+coc_no+'")]/../../../../../div[1]/div[1]/div[1]')
        self.wait(5,ele_policy_drop)
        self.find_and_click(*ele_policy_drop)
        return PolicyDetailPage(self.driver)




















