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
        main = AdminPanelPage()
        policy_status_list = main.goto_homecredit().filter_policy_status()
        lenth=len(policy_status_list)
        for i in range(lenth):
            assert policy_status_list[i] == "PROTECTED"

    @allure.story("按start_date过滤")
    def test_filter_startdate(self):
        main = AdminPanelPage()
        start_date_list = main.goto_homecredit().filter_start_date()
        lenth = len(start_date_list)
        for i in range(lenth):
            assert start_date_list[i] == "11 / 01 / 2021"

    @allure.story("上传csv文件")
    def test_import_enrollment(self):
        main = AdminPanelPage()
        main.goto_homecredit().import_enrollment()

    @allure.story("logout")
    def test_logout(self):
        main = AdminPanelPage()
        main.goto_homecredit().logout()


@allure.feature("policy_detial页面功能")
class TestPolicyDtail:
    @allure.story("点击policy_detail页的coc文件")
    def test_view_coc(self):
        main = AdminPanelPage()
        main.goto_homecredit().goto_policy_detail().click_view_coc()

    @allure.story("policy detail页面点击返回按钮回到policy list页面")
    def test_gobackto_policy_list(self):
        main = AdminPanelPage()
        main.goto_homecredit().goto_policy_detail().goto_polocy_list()













