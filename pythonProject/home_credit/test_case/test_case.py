import os

import pytest

from home_credit.page.admin_panel_page import AdminPanelPage
import allure

@allure.feature("policy页面功能")
class TestPolicy:

    @allure.story("搜索功能")
    def test_search(self):
        self.displayid = "MICIHCA67497916"
        main = AdminPanelPage()
        searchresult = main.goto_homecredit().search(self.displayid)
        print(searchresult)
        assert searchresult == self.displayid

    @allure.story("按protected状态过滤")
    def test_filter_protected(self):
        # 查找元素用的前端标签的text
        self.policy_status = "PolicyProtected"
        #期望的policy list中的policy status
        policy_status = "PROTECTED"

        main = AdminPanelPage()
        policy_status_list = main.goto_homecredit().filter_policy_status(self.policy_status)
        lenth=len(policy_status_list)
        for i in range(lenth):
            assert policy_status_list[i] == policy_status

    @allure.story("按start_date过滤")
    def test_filter_startdate(self):
        # 搜索时输入的start date
        self.start_date = "11 / 01 / 2021"
        # 搜索时输入的end date
        self.end_date = "11 / 01 / 2021"
        # 在start date 和end date一样的情况下，搜索结果start_date_list中的日期
        start_date = "11 / 01 / 2021"

        main = AdminPanelPage()
        start_date_list = main.goto_homecredit().filter_start_date(self.start_date,self.end_date)
        lenth = len(start_date_list)
        for i in range(lenth):
            assert start_date_list[i] == start_date

    @allure.story("上传csv文件")
    def test_import_enrollment(self):
        # csvpath的路径
        self.path = '/Users/xiongjun/Documents/test_files'
        self.csvpath = os.path.join(self.path,'tmpl_wrong_format_birth.csv')

        main = AdminPanelPage()
        main.goto_homecredit().import_enrollment(self.csvpath)

    @allure.story("logout")
    def test_logout(self):
        main = AdminPanelPage()
        main.goto_homecredit().logout()


@allure.feature("policy_detial页面功能")
class TestPolicyDtail:
    @allure.story("点击policy_detail页的coc文件")
    def test_view_coc(self):
        self.policy_id="HCACOC50882728"

        main = AdminPanelPage()
        main.goto_homecredit().goto_policy_detail(self.policy_id).click_view_coc()

    @allure.story("policy detail页面点击返回按钮回到policy list页面")
    def test_gobackto_policy_list(self):
        self.policy_id="HCACOC50882728"

        main = AdminPanelPage()
        main.goto_homecredit().goto_policy_detail(self.policy_id).goto_polocy_list()

    @allure.story("policy detail页面检查loan term")
    def test_check_loanterm(self):
        # 查找元素用的前端标签的text
        self.policy_id="HCACOC50882728"
        # 期望的loan term
        self.loan_term = "6 months"

        main = AdminPanelPage()
        loan_term = main.goto_homecredit().goto_policy_detail(self.policy_id).check_loan_term()
        assert self.loan_term == loan_term

    @allure.story("policy detail页面检查coverage start date")
    def test_check_coveragestartdate(self):
        # 查找元素用的前端标签的text
        self.policy_id = "HCACOC50882728"
        # 期望的coverage start date
        self.coverage_start_date = "11 / 10 / 2021"

        main = AdminPanelPage()
        coverage_start_date = main.goto_homecredit().goto_policy_detail(self.policy_id).check_coverage_start_date()
        assert self.coverage_start_date == coverage_start_date

    @allure.story("policy detail页面检查coverage end date")
    def test_check_coverageenddate(self):
        # 查找元素用的前端标签的text
        self.policy_id = "HCACOC50882728"
        # 期望的coverage end date
        self.coverage_end_date = "11 / 11 / 2022"

        main = AdminPanelPage()
        coverage_end_date = main.goto_homecredit().goto_policy_detail(self.policy_id).check_coverage_end_date()
        assert self.coverage_end_date == coverage_end_date

    @allure.story("policy detail页面检查full name")
    def test_check_fullname(self):
        # 查找元素用的前端标签的text
        self.policy_id = "HCACOC50882728"
        # 期望的full name
        self.fullname = "yue test liang"

        main = AdminPanelPage()
        fullname = main.goto_homecredit().goto_policy_detail(self.policy_id).check_fullname()
        assert self.fullname == fullname

    @allure.story("policy detail页面检查gender")
    def test_check_gender(self):
        # 查找元素用的前端标签的text
        self.policy_id = "HCACOC50882728"
        # 期望的gender
        self.gender = "Male"

        main = AdminPanelPage()
        gender = main.goto_homecredit().goto_policy_detail(self.policy_id).check_gender()
        assert self.gender == gender

    @allure.story("policy detail页面检查date of birth")
    def test_check_birthdate(self):
        # 查找元素用的前端标签的text
        self.policy_id = "HCACOC50882728"
        # 期望的gender
        self.birthdate = "02 / 29 / 1960"

        main = AdminPanelPage()
        birthdate = main.goto_homecredit().goto_policy_detail(self.policy_id).check_birthdate()
        assert self.birthdate == birthdate

    @allure.story("policy detail页面检查mobile number")
    def test_check_birthdate(self):
        # 查找元素用的前端标签的text
        self.policy_id = "HCACOC50882728"
        # 期望的gender
        self.mobile_number = "177101445487978"

        main = AdminPanelPage()
        mobile_number = main.goto_homecredit().goto_policy_detail(self.policy_id).check_mobile_number()
        assert self.mobile_number == mobile_number

    @allure.story("policy detail页面检查email")
    def test_check_email(self):
        # 查找元素用的前端标签的text
        self.policy_id = "HCACOC50882728"
        # 期望的gender
        self.email = "liang.yue@iglooinsure.com"

        main = AdminPanelPage()
        email = main.goto_homecredit().goto_policy_detail(self.policy_id).check_email()
        assert self.email == email

    @allure.story("policy detail页面检查address")
    def test_check_address(self):
        # 查找元素用的前端标签的text
        self.policy_id = "HCACOC50882728"
        # 期望的gender
        self.address = "chain sichuan chengdu 1-101 t！@#¥%……&*（）——+中国四川成都1-101"

        main = AdminPanelPage()
        address = main.goto_homecredit().goto_policy_detail(self.policy_id).check_address()
        assert self.address == address

















