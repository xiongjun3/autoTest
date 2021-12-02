import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from customer_portal.page_object.base_page import BasePage
from customer_portal.page_object.claim_form_page import ClaimFormPage
from customer_portal.page_object.claim_list_page import ClaimListPage
from customer_portal.page_object.policy_detail_page import PolicyDetailPage


class PolicyPage(BasePage):

    def get_fullname(self):
        # policyid=MICIHCA75454055的元素的查看详情按钮
        ele_policydetail = (By.XPATH, '//*[contains(text(),"MICIHCA75454055")]/../../../../../div[1]/div/div[1]')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_policydetail))
        self.find_and_click(*ele_policydetail)

        # 查找policyid=MICIHCA75454055的full_name
        ele_fullname = (By.XPATH, '//*[contains(text(),"MICIHCA75454055")]/../../../../../div[3]/div[2]/div[2]/div/div/div[1]/div[2]')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_fullname))
        full_name_item = self.find(*ele_fullname)
        full_name = full_name_item.get_attribute("textContent")
        return full_name

        #收起详情按钮
        ele_policydetail = (By.XPATH, '//*[contains(text(),"MICIHCA75454055")]/../../../../../div[1]/div/div[1]')
        self.find_and_click(*ele_policydetail)

    def get_gender(self):
        # policyid=MICIHCA75454055的元素的查看详情按钮
        ele_policydetail = (By.XPATH, '//*[contains(text(),"MICIHCA75454055")]/../../../../../div[1]/div/div[1]')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_policydetail))
        self.find_and_click(*ele_policydetail)

        # 查找policyid=MICIHCA75454055的date of birth
        ele_gender = (
            By.XPATH,
            '//*[contains(text(),"MICIHCA75454055")]/../../../../../div[3]/div[2]/div[2]/div/div/div[2]/div[2]')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_gender))
        gender_item = self.find(*ele_gender)
        gender = gender_item.get_attribute("textContent")
        return gender

        # 收起详情按钮
        ele_policydetail = (By.XPATH, '//*[contains(text(),"MICIHCA75454055")]/../../../../../div[1]/div/div[1]')
        self.find_and_click(*ele_policydetail)

    # 获取policy
    def get_birth(self):
        # policyid=MICIHCA75454055的元素的查看详情按钮
        ele_policydetail = (By.XPATH, '//*[contains(text(),"MICIHCA75454055")]/../../../../../div[1]/div/div[1]')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_policydetail))
        self.find_and_click(*ele_policydetail)

        # 查找policyid=MICIHCA75454055的date of birth
        ele_birth = (
        By.XPATH, '//*[contains(text(),"MICIHCA75454055")]/../../../../../div[3]/div[2]/div[2]/div/div/div[3]/div[2]')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_birth))
        birth_item = self.find(*ele_birth)
        birth = birth_item.get_attribute("textContent")
        return birth

        # 收起详情按钮
        ele_policydetail = (By.XPATH, '//*[contains(text(),"MICIHCA75454055")]/../../../../../div[1]/div/div[1]')
        self.find_and_click(*ele_policydetail)

    # 获取policy status
    def get_policy_status(self):
        # 查找policyid=MICIHCA75454055的status
        ele_birth = (
        By.XPATH, '//*[contains(text(),"MICIHCA75454055")]/../../../../../div[1]/div/div[3]/span/span')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_birth))
        policy_status_item = self.find(*ele_birth)
        policy_status = policy_status_item.get_attribute("textContent")
        return policy_status

    # policy_status = PROTECTED
    def get_policy_status_protected(self):
        # 查找policyid=MICIHCA75454055的status
        ele_birth = (
        By.XPATH, '//*[contains(text(),"MICIHCA75454055")]/../../../../../div[1]/div/div[3]/span/span')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_birth))
        policy_status_item = self.find(*ele_birth)
        policy_status = policy_status_item.get_attribute("textContent")
        return policy_status

    # policy_status = POLICY EXPIRED
    def get_policy_status_expired(self):
        # 查找policyid=MICIHCA75454055的status
        ele_birth = (
        By.XPATH, '//*[contains(text(),"MICIHCA67497916")]/../../../../../div[1]/div/div[3]/span/span')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_birth))
        policy_status_item = self.find(*ele_birth)
        policy_status = policy_status_item.get_attribute("textContent")
        return policy_status

    def view_coc(self):
        ele_view_coc = (
            By.XPATH, '//*[contains(text(),"MICIHCA75454055")]/../button')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_view_coc))
        self.find_and_click(*ele_view_coc)
        time.sleep(2)

    def view_coverage(self):
        ele_view_coverage = (
            By.XPATH, '//*[contains(text(),"MICIHCA75454055")]/../../../div[2]/div[2]/button')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_view_coverage))
        self.find_and_click(*ele_view_coverage)
        time.sleep(2)

    def get_loan_term(self):
        ele_loan_term = (
            By.XPATH, '//*[contains(text(),"MICIHCA75454055")]/../../../div[3]/div[2]/span')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_loan_term))
        loan_term_item = self.find(*ele_loan_term)
        loan_tern = loan_term_item.get_attribute("textContent")
        return loan_tern

    def get_coverage_start_date(self):
        ele_coverage_start_date = (
            By.XPATH, '//*[contains(text(),"MICIHCA75454055")]/../../../div[4]/div[2]/span')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(ele_coverage_start_date))
        coverage_start_date_item = self.find(*ele_coverage_start_date)
        coverage_start_date = coverage_start_date_item.get_attribute("textContent")
        return coverage_start_date

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




















