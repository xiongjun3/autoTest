import requests

from apis.base_api import BaseApi


class TestGetToken(BaseApi):
    def test_get_token(self,email,password):
        # email = "jun.xiong@iglooinsure.com"
        # password = "123456"
        url = "https://api.qa.iglooinsure.com/v1/admin_account/login/by_password"
        params = {"email": email, "password": password}
        r = self.send("POST",url,tool="requests",json=params)
        # r = requests.post(url=url1,json=data)
        admin_token = r.json().get("user_token")
        return admin_token


