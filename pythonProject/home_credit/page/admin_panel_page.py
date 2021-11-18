from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from home_credit.page.base_page import BasePage
from selenium.webdriver.common.by import By
from home_credit.page.policy_list_page import PolicyPage


class AdminPanelPage(BasePage):
    def goto_homecredit(self):
        locator = (By.XPATH,'//*[@class="ant-space ant-space-horizontal ant-space-align-center platforms___27-_C"]/div[3]/div/div')
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(By.XPATH,'//*[@class="ant-space ant-space-horizontal ant-space-align-center platforms___27-_C"]/div[3]/div/div').click()
        return PolicyPage(self.driver)

