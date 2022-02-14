import random

import requests


class TestCompany:
    def setup_class(self):
        url1 = "https://api.qa.iglooinsure.com/v1/admin_account/login/by_password"
        data = {"email": "jun.xiong@iglooinsure.com", "password": "123456"}
        r = requests.post(url=url1, json=data)
        self.admin_token = r.json().get("user_token")
    def test_add_company(self):
        url1 = "https://api.qa.iglooinsure.com/v1/uic-eb/admin/company_add"
        random1 = random.randint(100, 999)
        data = {"company_name":f"company auto name {random1}","sales_channel":"direct_business","contact_info":{}}

        headers = {"X-Axinan-Authorization": self.admin_token}
        r = requests.post(url=url1,json=data,headers=headers)
        assert r.json().get("ok") == "ok"
        print(r.json())

    def test_update_company(self):
        url1 = "https://api.qa.iglooinsure.com/v1/uic-eb/admin/contact_info"
        data = {"company_id":"UIC72959785","contact_info":{"name":"name 1","position":"test position","mobile":"0123456788","email":"jun.xiong@iglooinsure.com"}}
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = requests.put(url=url1,json=data,headers=headers)
        assert r.json().get("ok") == "ok"
        print(r.json())

