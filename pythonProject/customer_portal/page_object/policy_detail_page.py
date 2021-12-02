from selenium.webdriver.common.by import By
from customer_portal.page_object.base_page import BasePage


class PolicyDetailPage(BasePage):
    def check_policy_detail(self, item):
        ele_item = (By.XPATH,'//*[contains(text(),"'+item+'")]/../../div[2]/span')
        self.wait(5,ele_item)
        content = self.find(*ele_item).text
        return content