import requests

class TestToken:
    def test_get_token(self):
        url1="https://api.qa.iglooinsure.com/v1/admin_account/login/by_password"
        data={"email":"jun.xiong@iglooinsure.com","password":"123456"}
        r = requests.post(url=url1,json=data)
        admin_token = r.json().get("user_token")
        return admin_token
        print(r.text)
        print(r.json().get("user_token"))

