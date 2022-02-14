from apis.get_token import TestGetToken
import random

from utils.file_tools import FileTool


class AdminApi(TestGetToken):
    def __init__(self):
        # 调用文件的读取方法获取yaml数据
        yaml_data = FileTool.read_yaml("secrets")
        # 从yaml数据中读取需要的username和password
        email = yaml_data.get("email")
        password = yaml_data.get("password")
        # print(f"email={email},password={password}")
        self.admin_token = self.test_get_token(email,password)

    # client api
    def add_company(self,data):
        url = "https://api.qa.iglooinsure.com/v1/uic-eb/admin/company_add"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("POST", url, tool="requests",json=data, headers=headers)
        return r

    def contact_info(self,data):
        url = "https://api.qa.iglooinsure.com/v1/uic-eb/admin/contact_info"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("PUT", url, tool="requests", json=data,headers=headers)
        return r

    def company_list(self,data):
        url = "https://api.qa.iglooinsure.com/v1/uic-eb/admin/companies"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("GET", url, tool="requests", params=data, headers=headers)
        return r

    def company_detail(self,company_id):
        url = f"https://api.qa.iglooinsure.com/v1/uic-eb/admin/companies/{company_id}"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("GET", url, tool="requests",headers=headers)
        return r

    def member_list(self,data):
        url = "https://api.qa.iglooinsure.com/v1/uic-eb/admin/members"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("GET", url, tool="requests", params=data, headers=headers)
        return r

    def invalid_list(self,data):
        url = "https://api.qa.iglooinsure.com/v1/uic-eb/admin/invalid_list"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("GET", url, tool="requests", params=data, headers=headers)
        return r

    def invalid_change(self,data):
        url = "https://api.qa.iglooinsure.com/v1/uic-eb/admin/invalid_change"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("POST", url, tool="requests",json=data,headers=headers)
        return r

    # policy api
    def policy_list(self,data):
        url = "https://api.qa.iglooinsure.com/v1/uic-eb/admin/policies"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("GET", url, tool="requests",params=data,headers=headers)
        return r

    def policy_detail(self,policy_id):
        url = f"https://api.qa.iglooinsure.com/v1/uic-eb/admin/policies/{policy_id}"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("GET", url, tool="requests",headers=headers)
        return r

    def policy_refund(self,policy_id,data):
        url = f"https://api.qa.iglooinsure.com/v1/uic-eb/admin/policies/{policy_id}/refund"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("POST", url, tool="requests",json=data, headers=headers)
        return r

    # claim api
    def claim_list(self,data):
        url = "https://api.qa.iglooinsure.com/v1/uic-eb/admin/claims"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("GET", url, tool="requests", params=data, headers=headers)
        return r

    def claim_detail(self,claim_id):
        url = f"https://api.qa.iglooinsure.com/v1/uic-eb/admin/claims/{claim_id}"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("GET", url, tool="requests", headers=headers)
        return r

    def claim_approve(self,claim_id,data):
        url = f"https://api.qa.iglooinsure.com/v1/uic-eb/admin/claims/{claim_id}/approve"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("POST", url, tool="requests",json=data, headers=headers)
        return r

    def claim_fail(self,claim_id,data):
        url = f"https://api.qa.iglooinsure.com/v1/uic-eb/admin/claims/{claim_id}/disapprove"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("POST", url, tool="requests",json=data, headers=headers)
        return r

    def claim_pass(self,claim_id):
        url = f"https://api.qa.iglooinsure.com/v1/uic-eb/admin/claims/{claim_id}/confirm"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("POST", url, tool="requests", headers=headers)
        return r

    def claim_pend(self,claim_id,data):
        url = f"https://api.qa.iglooinsure.com/v1/uic-eb/admin/claims/{claim_id}/pend"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("POST", url, tool="requests",json=data, headers=headers)
        return r

    def claim_reject(self,claim_id,data):
        url = f"https://api.qa.iglooinsure.com/v1/uic-eb/admin/claims/{claim_id}/reject"
        headers = {"X-Axinan-Authorization": self.admin_token}
        r = self.send("POST", url, tool="requests",json=data, headers=headers)
        return r










