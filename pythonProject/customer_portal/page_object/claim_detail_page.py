from selenium.webdriver.common.by import By
from customer_portal.page_object.base_page import BasePage


class ClaimDetailPage(BasePage):
    def check_insured_detail(self , type, item):
        ele_item = (By.XPATH,'//*[contains(text(),"'+type+'")]/../..//*[contains(text(),"'+item+'")]/../../div[2]/span')
        self.wait(5,ele_item)
        content = self.find(*ele_item).text
        return content