import os
import time
from home_credit.page.admin_panel_page import AdminPanelPage
import allure

@allure.feature("policy页面功能")
class TestPolicy:

    @allure.story("搜索功能")
    def test_search(self):
        self.coc_no = "MICIHCA67497916"
        self.insured_name = "xiong test jun"
        self.email = "jun.xiong@iglooinsure.com"
        self.loan_term = "6 months"
        self.coverage_start_date = "11 / 10 / 2021"

        main = AdminPanelPage()
        coc_no,insured_name,email,loan_term,coverage_start_date= main.goto_homecredit().search_by_coc_no(self.coc_no)
        assert coc_no == self.coc_no and insured_name == self.insured_name and email == self.email and loan_term == self.loan_term and coverage_start_date == self.coverage_start_date

    @allure.story("按protected状态过滤")
    def test_filter_protected(self):
        # 查找元素用的前端标签的text
        self.policy_status = "PolicyProtected"
        # 期望的policy list中的policy status
        policy_status = "PROTECTED"

        main = AdminPanelPage()
        policy_status_list = main.goto_homecredit().filter_policy_status(self.policy_status)
        length = len(policy_status_list)
        for i in range(length):
            assert policy_status_list[i] == policy_status

    @allure.story("按start_date过滤")
    def test_filter_coverage_star_tdate(self):
        # 搜索时输入的start date
        self.start_date = "11 / 01 / 2021"
        # 搜索时输入的end date
        self.end_date = "11 / 01 / 2021"
        # 在start date 和end date一样的情况下，搜索结果start_date_list中的日期
        start_date = "11 / 01 / 2021"

        main = AdminPanelPage()
        start_date_list = main.goto_homecredit().filter_start_date(self.start_date,self.end_date)
        length = len(start_date_list)
        for i in range(length):
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
        self.policy_id="HCACOC39282770"

        main = AdminPanelPage()
        main.goto_homecredit().goto_policy_detail(self.policy_id).click_view_coc()

    @allure.story("policy detail页面点击返回按钮回到policy list页面")
    def test_gobackto_policy_list(self):
        self.policy_id="HCACOC50882728"

        main = AdminPanelPage()
        main.goto_homecredit().goto_policy_detail(self.policy_id).goto_polocy_list()

    @allure.story("policy detail页面检查loan term")
    def test_check_loan_term(self):
        self.policy_id="MICIHCA67826395"
        self.item = "Loan Term"
        self.content = "6 months"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_policy_detail(self.policy_id).check_item_value(self.item)
        assert content == self.content

    @allure.story("policy detail页面检查Coverage Start Date")
    def test_check_coverage_start_date(self):
        self.policy_id = "MICIHCA67826395"
        self.item = "Coverage Start Date"
        self.content = "11 / 01 / 2021"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_policy_detail(self.policy_id).check_item_value(self.item)
        assert content == self.content

    @allure.story("policy detail页面检查Coverage End Date")
    def test_check_coverage_end_date(self):
        self.policy_id = "MICIHCA67826395"
        self.item = "Coverage End Date"
        self.content = "05 / 01 / 2022"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_policy_detail(self.policy_id).check_item_value(self.item)
        assert content == self.content

    @allure.story("policy detail页面检查full name")
    def test_check_full_name(self):
        self.policy_id = "MICIHCA67826395"
        self.item = "Full Name"
        self.content = "xiong ten jun"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_policy_detail(self.policy_id).check_item_value(self.item)
        assert content == self.content

    @allure.story("policy detail页面检查gender")
    def test_check_gender(self):
        self.policy_id = "MICIHCA67826395"
        self.item = "Gender"
        self.content = "Female"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_policy_detail(self.policy_id).check_item_value(self.item)
        assert content == self.content

    @allure.story("policy detail页面检查date of birth")
    def test_check_birth_date(self):
        self.policy_id = "MICIHCA67826395"
        self.item = "Date of Birth"
        self.content = "12 / 29 / 1994"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_policy_detail(self.policy_id).check_item_value(self.item)
        assert content == self.content

    @allure.story("policy detail页面检查mobile number")
    def test_check_mobile_no(self):
        self.policy_id = "MICIHCA67826395"
        self.item = "Mobile Number"
        self.content = "177101445487978"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_policy_detail(self.policy_id).check_item_value(self.item)
        assert content == self.content

    @allure.story("policy detail页面检查email")
    def test_check_email(self):
        self.policy_id = "MICIHCA67826395"
        self.item = "Email"
        self.content = "ten.xiong@iglooinsure.com"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_policy_detail(self.policy_id).check_item_value(self.item)
        assert content == self.content

    @allure.story("policy detail页面检查address")
    def test_check_address(self):
        self.policy_id = "MICIHCA67826395"
        self.item = "Address"
        self.content = "china sichuan chengdu 1-101"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_policy_detail(self.policy_id).check_item_value(self.item)
        assert content == self.content


@allure.feature("claim_list页面功能")
class TestClaimList:
    @allure.story("search by claim id")
    def test_search_by_cliam_id(self):
        self.claim_id = "D-HC-MICI-76181916"
        self.coc_no = "MICIHCA75454055"
        self.insured_name = "xiong test jun"
        self.claimant_email = "412882383@qq.com"
        self.claim_date = "11 / 19 / 2021"

        main = AdminPanelPage()
        claim_id,coc_no,insured_name,claimant_email,claim_date = main.goto_homecredit().goto_claim_list().search_by_claim_id(self.claim_id)
        assert claim_id == self.claim_id and coc_no == self.coc_no and insured_name == self.insured_name and claimant_email == self.claimant_email and claim_date==self.claim_date

    @allure.story("search by coc no")
    def test_search_by_coc_no(self):
        self.coc_no = "MICIHCA75454055"

        main = AdminPanelPage()
        coc_no_list = main.goto_homecredit().goto_claim_list().search_by_coc_no(self.coc_no)
        length = len(coc_no_list)
        for i in range(length):
            assert coc_no_list[i] == self.coc_no

    @allure.story("按claim_date过滤")
    def test_filter_claim_date(self):
        # 搜索时输入的start date
        self.start_date = "11 / 19 / 2021"
        # 搜索时输入的end date
        self.end_date = "11 / 19 / 2021"
        # 在start date 和end date一样的情况下，搜索结果claim_date_list中的日期
        self.claim_date = "11 / 19 / 2021"

        main = AdminPanelPage()
        claim_date_list = main.goto_homecredit().goto_claim_list().filter_claim_date(self.start_date,self.end_date)
        length = len(claim_date_list)
        for i in range(length):
            assert claim_date_list[i] == self.claim_date

    @allure.story("按protected:ClaimProcessing状态过滤")
    def test_filter_claim_processing(self):
        # 查找元素用的前端标签的text
        self.policy_status = "ClaimProcessing"
        # 期望的policy list中的policy status
        claim_status = "CLAIM PROCESSING"

        main = AdminPanelPage()
        self.policy_status_list = main.goto_homecredit().goto_claim_list().filter_policy_status(self.policy_status)
        length = len(self.policy_status_list)
        for i in range(length):
            assert self.policy_status_list[i] == claim_status

    @allure.story("按protected:ClaimApproved状态过滤")
    def test_filter_ClaimApproved(self):
        # 查找元素用的前端标签的text
        self.policy_status = "ClaimApproved"
        # 期望的policy list中的policy status
        policy_status = "CLAIM APPROVED"

        main = AdminPanelPage()
        policy_status_list = main.goto_homecredit().goto_claim_list().filter_policy_status(self.policy_status)
        length = len(policy_status_list)
        for i in range(length):
            assert policy_status_list[i] == policy_status

@allure.feature("claim_detail页面功能")
class TestClaimDetail:
    @allure.story("approve")
    def test_approve(self):
        self.claim_status = "CLAIM PROCESSING"
        self.benefit = 1

        main = AdminPanelPage()
        benefit = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_status(self.claim_status).approve(self.benefit)
        assert benefit == self.benefit

    @allure.story("reject")
    def test_reject(self):
        self.claim_status = "CLAIM PROCESSING"
        self.reason = "reason:wrong information"

        main = AdminPanelPage()
        reason = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_status(self.claim_status).reject(self.reason)
        assert reason == self.reason

    @allure.story("check coc no")
    def test_check_coc_no(self):
        self.claim_id = "D-HC-MICI-76181916"
        self.item = "COC No."
        self.coc_no = "MICIHCA75454055"

        main = AdminPanelPage()
        coc_no = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_basic_item(self.item)
        assert self.coc_no == coc_no

    @allure.story("check Claim Date")
    def test_check_claim_date(self):
        self.claim_id = "HC-MICI-64908132"
        self.item = "Claim Date"
        self.claim_date = "11 / 29 / 2021"

        main = AdminPanelPage()
        claim_date = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_basic_item(self.item)
        assert self.claim_date == claim_date

    @allure.story("check full name")
    def test_check_full_name(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Insured’s Details"
        self.item = "Full Name"
        self.content = "xiong jun"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(self.role,self.item)
        assert content == self.content

    @allure.story("check gender")
    def test_check_insured_full_name(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Insured’s Details"
        self.item = "Gender"
        self.content = "Male"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check insured Date of Birth")
    def test_check_insured_gender(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Insured’s Details"
        self.item = "Date of Birth"
        self.content = "02 / 29 / 1960"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check insured Mobile Number")
    def test_check_insured_gender(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Insured’s Details"
        self.item = "Mobile Number"
        self.content = "177101445487978"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check insured Email")
    def test_check_insured_gender(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Insured’s Details"
        self.item = "Email"
        self.content = "jun.xiong@iglooinsure.com"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check insured Address")
    def test_check_insured_gender(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Insured’s Details"
        self.item = "Address"
        self.content = "chain sichuan chengdu 1-101 t！@#¥%……&*（）——+中国四川成都1-101"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check insured Identification Type")
    def test_check_insured_gender(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Insured’s Details"
        self.item = "Identification Type"
        self.content = "Senior Citizen Card"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check insured Identification Number")
    def test_check_insured_gender(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Insured’s Details"
        self.item = "Identification Number"
        self.content = "0000011111"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check claimant full name")
    def test_check_claimant_full_name(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Claimant’s Details"
        self.item = "Relationship to the Insured"
        self.content = "Spouse"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check claimant full name")
    def test_check_claimant_full_name(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Claimant’s Details"
        self.item = "Full Name"
        self.content = "li test ming"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check claimant mobile number")
    def test_check_claimant_mobile_no(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Claimant’s Details"
        self.item = "Mobile Number"
        self.content = "17710144558"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check claimant email")
    def test_check_claimant_mobile_no(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Claimant’s Details"
        self.item = "Email"
        self.content = "412882383@qqtest.com"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check claimant email")
    def test_check_claimant_mobile_no(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Claimant’s Details"
        self.item = "Address"
        self.content = "test address"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check claimant Identification Type")
    def test_check_claimant_mobile_no(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Claimant’s Details"
        self.item = "Identification Type"
        self.content = "Senior Citizen Card"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check claimant Identification Number")
    def test_check_claimant_mobile_no(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Claimant’s Details"
        self.item = "Identification Number"
        self.content = "9999988888"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check reimbursment :Account Name")
    def test_check_reimbursment_account(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Reimbursement Details"
        self.item = "Account Name"
        self.content = "xiongjun"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check reimbursment :Account Number")
    def test_check_reimbursment_account(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Reimbursement Details"
        self.item = "Account Number"
        self.content = "123456789"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check reimbursment :Bank Name")
    def test_check_reimbursment_account(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "Reimbursement Details"
        self.item = "Bank Name"
        self.content = "china bank"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check history :Claim Status")
    def test_check_claim_status(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "History"
        self.item = "Claim Status"
        self.content = "CLAIM APPROVED"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check history :Last Updated")
    def test_check_claim_status(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "History"
        self.item = "Last Updated"
        self.content = "12 / 06 / 2021"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("check history :Updated by")
    def test_check_claim_status(self):
        self.claim_id = "HC-MICI-61505107"
        self.role = "History"
        self.item = "Updated by"
        self.content = "jun.xiong@iglooinsure.com"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_item_value(
            self.role, self.item)
        assert content == self.content

    @allure.story("click soa picture")
    def test_check_SOA_file(self):
        self.claim_id = "HC-MICI-61505107"
        self.item = "SOA from the Hospital"

        main = AdminPanelPage()
        main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_upload_file(self.item)

    @allure.story("click Hospital Certificate Bearing picture")
    def test_check_HCB_file(self):
        self.claim_id = "HC-MICI-61505107"
        self.item = "Hospital Certificate Bearing the Number of Days Confined at the Hospital"

        main = AdminPanelPage()
        main.goto_homecredit().goto_claim_list().goto_claim_detail_by_claimid(self.claim_id).check_upload_file(
            self.item)

@allure.feature("reimburse_list页面功能")
class TestReimburseList:

    @allure.story("search by claim id")
    def test_search_by_claim_id(self):
        self.claim_id = "HC-MICI-43673798"
        self.coc_no = "HCACOC65586238"
        self.insure_name = "xiong jun"
        self.claimant_email = "jun.xiong@iglooinsure.com"
        self.approved_date = "11 / 22 / 2021"

        main = AdminPanelPage()
        claim_id,coc_no,insure_name,claimant_email,approved_date = main.goto_homecredit().goto_reimburse_list().search_by_claim_id(self.claim_id)
        assert claim_id == self.claim_id and coc_no == self.coc_no and insure_name == self.insure_name and claimant_email == self.claimant_email and approved_date == self.approved_date

    @allure.story("按approved_date过滤")
    def test_filter_approved_date(self):
        # 搜索时输入的start date
        self.start_date = "12 / 06 / 2021"
        # 搜索时输入的end date
        self.end_date = "12 / 06 / 2021"
        # 在start date 和end date一样的情况下，搜索结果start_date_list中的日期
        self.approved_date = "12 / 06 / 2021"

        main = AdminPanelPage()
        approved_date_list = main.goto_homecredit().goto_reimburse_list().filter_approved_date(self.start_date,self.end_date)
        length = len(approved_date_list)
        for i in range(length):
            assert approved_date_list[i] == self.approved_date

    @allure.story("按status:ReimbursementProcessing状态过滤")
    def test_filter_reimbursement_status_processing(self):
        # 查找元素用的前端标签的text
        self.status = "ReimbursementProcessing"
        # 期望的policy list中的policy status
        status = "REIMBURSEMENT PROCESSING"

        main = AdminPanelPage()
        self.status_list = main.goto_homecredit().goto_reimburse_list().filter_status(self.status)
        length = len(self.status_list)
        for i in range(length):
            assert self.status_list[i] == status

    @allure.story("按status:Reimbursed状态过滤")
    def test_filter_reimbursement_status_Reimbursed(self):
        # 查找元素用的前端标签的text
        self.status = "Reimbursed"
        # 期望的policy list中的policy status
        status = "REIMBURSED"

        main = AdminPanelPage()
        self.status_list = main.goto_homecredit().goto_reimburse_list().filter_status(self.status)
        length = len(self.status_list)
        for i in range(length):
            assert self.status_list[i] == status



@allure.feature("reimburse_detail页面功能")
class TestReimburseDetail:
    @allure.story("complete")
    def test_complete(self):
        self.reimburse_status = "REIMBURSEMENT PROCESSING"
        self.date = time.strftime("%m / %d / %Y", time.localtime())
        self.payment_id = "123456"
        self.reimbursement_status_result = "REIMBURSED"

        main = AdminPanelPage()
        reimbursement_status_result = main.goto_homecredit().goto_reimburse_list().goto_reimburse_detail_by_status(self.reimburse_status).complete(self.date,self.payment_id)
        assert reimbursement_status_result == self.reimbursement_status_result

    @allure.story("check COC No.")
    def test_check_coc_no(self):
        self.claim_id="HC-MICI-49926208"
        self.item = "COC No."
        self.content = "MICIHCA67497916"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_reimburse_list().goto_reimburse_detail_by_claimid(self.claim_id).check_item_value(self.item)
        assert content == self.content

    @allure.story("check Status Updated Date")
    def test_check_status_update_date(self):
        self.claim_id = "HC-MICI-48440846"
        self.item = "Status Updated Date"
        self.content = "12 / 06 / 2021"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_reimburse_list().goto_reimburse_detail_by_claimid(
            self.claim_id).check_item_value(self.item)
        assert content == self.content

    @allure.story("check Reimbursement Account Name")
    def test_check_account_name(self):
        self.claim_id = "HC-MICI-48440846"
        self.item = "Account Name"
        self.content = "xiongjun"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_reimburse_list().goto_reimburse_detail_by_claimid(
            self.claim_id).check_item_value(self.item)
        assert content == self.content

    @allure.story("check Reimbursement Account Number")
    def test_check_account_no(self):
        self.claim_id = "HC-MICI-48440846"
        self.item = "Account Number"
        self.content = "123456789"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_reimburse_list().goto_reimburse_detail_by_claimid(
            self.claim_id).check_item_value(self.item)
        assert content == self.content

    @allure.story("check Reimbursement Bank Name")
    def test_check_bank_name(self):
        self.claim_id = "HC-MICI-48440846"
        self.item = "Bank Name"
        self.content = "china bank"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_reimburse_list().goto_reimburse_detail_by_claimid(
            self.claim_id).check_item_value(self.item)
        assert content == self.content

    # history,REIMBURSEMENT PROCESSING状态的有三个模块，REIMBURSED状态的有6个模块
    @allure.story("check History reimbursed Reimbursement Status")
    def test_check_reimbursed_reimbursement_status(self):
        self.claim_id = "HC-MICI-48440846"
        self.n = "1"
        self.content = "REIMBURSED"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_reimburse_list().goto_reimburse_detail_by_claimid(
            self.claim_id).check_history_item(self.n)
        assert content == self.content

    @allure.story("check History reimbursed Last Updated")
    def test_check_reimbursed_last_update(self):
        self.claim_id = "HC-MICI-48440846"
        self.n = "2"
        self.content = "12 / 06 / 2021"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_reimburse_list().goto_reimburse_detail_by_claimid(
            self.claim_id).check_history_item(self.n)
        assert content == self.content

    @allure.story("check History reimbursed Updated by")
    def test_check_reimbursed_update_by(self):
        self.claim_id = "HC-MICI-48440846"
        self.n = "3"
        self.content = "jun.xiong@iglooinsure.com"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_reimburse_list().goto_reimburse_detail_by_claimid(
            self.claim_id).check_history_item(self.n)
        assert content == self.content

    @allure.story("check History reimbursement processing Reimbursement Status")
    def test_check_reimbursement_processing_reimbursement_status(self):
        self.claim_id = "HC-MICI-48440846"
        self.n = "4"
        self.content = "REIMBURSEMENT PROCESSING"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_reimburse_list().goto_reimburse_detail_by_claimid(
            self.claim_id).check_history_item(self.n)
        assert content == self.content

    @allure.story("check History reimbursement processing Last Updated")
    def test_check_reimbursement_processing_last_update(self):
        self.claim_id = "HC-MICI-48440846"
        self.n = "5"
        self.content = "12 / 06 / 2021"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_reimburse_list().goto_reimburse_detail_by_claimid(
            self.claim_id).check_history_item(self.n)
        assert content == self.content

    @allure.story("check History reimbursement processing Updated by")
    def test_check_reimbursement_processing_update_by(self):
        self.claim_id = "HC-MICI-48440846"
        self.n = "6"
        self.content = "jun.xiong@iglooinsure.com"

        main = AdminPanelPage()
        content = main.goto_homecredit().goto_reimburse_list().goto_reimburse_detail_by_claimid(
            self.claim_id).check_history_item(self.n)
        assert content == self.content






























