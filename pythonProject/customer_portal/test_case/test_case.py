import allure
from customer_portal.page_object.policy_page import PolicyPage


@allure.feature("customer policy页面功能")
class TestPolicy:
    @allure.story("检查full name")
    def test_policy_detail_fullname(self):
        main = PolicyPage()
        full_name = main.get_fullname()
        assert full_name == "xiong test jun"

    @allure.story("检查gender")
    def test_policy_detail_gender(self):
        main = PolicyPage()
        gender = main.get_gender()
        assert gender == "Male"

    @allure.story("检查date of birth")
    def test_policy_detail_birth(self):
        main = PolicyPage()
        birth = main.get_birth()
        assert birth == "02 / 29 / 1960"

    @allure.story("检查protected policy status")
    def test_policy_detail_policystatus_protected(self):
        main = PolicyPage()
        policy_status = main.get_policy_status_protected()
        assert policy_status == "PROTECTED"

    @allure.story("检查expired policy status")
    def test_policy_detail_policystatus_expired(self):
        main = PolicyPage()
        policy_status = main.get_policy_status_expired()
        assert policy_status == "POLICY EXPIRED"

    @allure.story("查看coc文件")
    def test_policy_detail(self):
        main = PolicyPage()
        main.view_coc()

    @allure.story("查看coverage")
    def test_policy_detail(self):
        main = PolicyPage()
        main.view_coverage()

    @allure.story("检查loan term")
    def test_policy_detail_birth(self):
        main = PolicyPage()
        loan_term = main.get_loan_term()
        assert loan_term == "6 months"

    @allure.story("检查coverage start date")
    def test_policy_detail_birth(self):
        main = PolicyPage()
        coverage_start_date = main.get_coverage_start_date()
        assert coverage_start_date == "11 / 10 / 2021"

    @allure.story("检查drop name")
    def test_drop_name(self):
        main = PolicyPage()
        drop_name = main.check_drop_name()
        assert drop_name == "jun xiong"

    @allure.story("检查drop email")
    def test_drop_email(self):
        main = PolicyPage()
        drop_email = main.check_drop_email()
        assert drop_email == "Email: jun.xiong@iglooinsure.com"


    @allure.story("退出登陆")
    def test_policy_detail(self):
        main = PolicyPage()
        main.logout()

@allure.feature("claim form页面功能")
class TestClaimForm:
    @allure.story("提交claim form并在claim list页面检查该claim已存在")
    def test_submit_claim_form(self):
        self.coc_no = "HCACOC65586238"
        main = PolicyPage()
        main.goto_claim_form(self.coc_no).submit_claim_form()

@allure.feature("claim list页面功能")
class TestClaimList:
    @allure.story("cancel pilicy")
    def test_cancel_policy(self):
        self.claim_no = "HC-MICI-20338279"
        main = PolicyPage()
        main.goto_claim_list().cancel_claim(self.claim_no)










