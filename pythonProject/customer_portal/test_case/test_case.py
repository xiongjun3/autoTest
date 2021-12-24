import allure
from customer_portal.page_object.policy_page import PolicyPage


@allure.feature("customer policy页面功能")
class TestPolicy:

    @allure.story("检查protected policy status：PROTECTED")
    def test_policy_detail_policystatus_protected(self):
        self.coc_no = "HCACOC65586238"
        self.policy_status = "PROTECTED"

        main = PolicyPage()
        policy_status = main.get_policy_status(self.coc_no)
        assert policy_status == self.policy_status

    @allure.story("检查protected policy status：POLICY EXPIRED")
    def test_policy_detail_policystatus_protected(self):
        self.coc_no = "MICIHCA67497916"
        self.policy_status = "POLICY EXPIRED"

        main = PolicyPage()
        policy_status = main.get_policy_status(self.coc_no)
        assert policy_status == self.policy_status



    @allure.story("查看coc文件")
    def test_view_coc_new_window(self):
        self.coc_no = "MICIHCA67497916"

        main = PolicyPage()
        main.view_coc_new_window(self.coc_no)

    @allure.story("查看coverage:Daily Hospital Income Benefit")
    def test_view_coverage(self):
        self.coc_no = "MICIHCA67497916"
        self.benefit = "Daily Hospital Income Benefit (sickness and accident)"
        self.content = "PHP1,000.00 per day (max of 15 days)"

        main = PolicyPage()
        content = main.view_coverage(self.coc_no,self.benefit)
        assert content == self.content

    @allure.story("查看coverage:Accidental Burial Benefit")
    def test_view_coverage(self):
        self.coc_no = "MICIHCA67497916"
        self.benefit = "Accidental Burial Benefit"
        self.content = "PHP10,000.00"

        main = PolicyPage()
        content = main.view_coverage(self.coc_no, self.benefit)
        assert content == self.content

    @allure.story("查看coverage:Emergency Room Assistance (sickness and accident)")
    def test_view_coverage(self):
        self.coc_no = "MICIHCA67497916"
        self.benefit = "Emergency Room Assistance (sickness and accident)"
        self.content = "PHP10,000.00(one time use)"

        main = PolicyPage()
        content = main.view_coverage(self.coc_no, self.benefit)
        assert content == self.content

    @allure.story("查看coverage:Burial Cash Assistance due to Natural sickness")
    def test_view_coverage(self):
        self.coc_no = "MICIHCA67497916"
        self.benefit = "Burial Cash Assistance due to Natural sickness"
        self.content = "PHP10,000.00"

        main = PolicyPage()
        content = main.view_coverage(self.coc_no, self.benefit)
        assert content == self.content





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



    @allure.story("go to death claim form")
    def test_cannot_goto_death_claim_form(self):
        # 这个policy已经申请过death claim了
        self.coc_no = "HCACOC65586238"
        self.death_type = "Accident"
        self.content = "Claims may no longer be submitted for this policy"

        main = PolicyPage()
        content = main.goto_death_claim_form(self.coc_no,self.death_type)
        assert content == self.content

    @allure.story("退出登陆")
    def test_policy_detail(self):
        main = PolicyPage()
        main.logout()

@allure.feature("claim form页面功能")
class TestClaimForm:
    @allure.story("relationship:Spouse,提交claim form并在claim list页面检查该claim已存在")
    def test_submit_claim_form(self):
        """
        insured_id_type \ claimant_id_type:
        TIN \ Passport \ UMID \ SSS \ Driver's License \ 
        National ID \ PSA Birth Certificate \ Voter's ID \ Senior Citizen Card \ PRC ID
        relationship : Self \ Spouse \ Parent \ Child \ Others
        """

        self.coc_no = "HCACOC65586238"
        self.insured_id_no = "0000011111"
        self.insured_id_type = "National ID"
        self.relationship = "Spouse"
        self.claimant_first_name = "li"
        self.claimant_middle_name = "test"
        self.claimant_last_name = "ming"
        self.claimant_mobile_no = "17710144558"
        self.claimant_email = "412882383@qqtest.com"
        self.claimant_address = "test address"
        self.claimant_id_type = "Senior Citizen Card"
        self.claimant_id_no = "9999988888"

        main = PolicyPage()
        main.goto_claim_form(self.coc_no).submit_claim_form(self.insured_id_type, self.insured_id_no, self.relationship,
                                                            self.claimant_first_name, self.claimant_middle_name,
                                                            self.claimant_last_name, self.claimant_mobile_no,
                                                            self.claimant_email, self.claimant_address,
                                                            self.claimant_id_type, self.claimant_id_no)

    @allure.story("relationship:self,提交claim form并在claim list页面检查该claim已存在")
    def test_submit_claim_form_self(self):
        """
        insured_id_type \ claimant_id_type:
        TIN \ Passport \ UMID \ SSS \ Driver's License \
        National ID \ PSA Birth Certificate \ Voter's ID \ Senior Citizen Card \ PRC ID
        relationship : Self \ Spouse \ Parent \ Child \ Others
        """

        self.coc_no = "HCACOC65586238"
        self.insured_id_type = "PRC ID"
        self.insured_id_no = "0000011111"
        self.relationship = "Self"
        self.claimant_first_name = "li"
        self.claimant_middle_name = "test"
        self.claimant_last_name = "ming"
        self.claimant_mobile_no = "17710144558"
        self.claimant_email = "412882383@qqtest.com"
        self.claimant_address = "test address"
        self.claimant_id_type = "Senior Citizen Card"
        self.claimant_id_no = "9999988888"

        main = PolicyPage()
        main.goto_claim_form(self.coc_no).submit_claim_form(self.insured_id_type, self.insured_id_no, self.relationship,
                                                            self.claimant_first_name, self.claimant_middle_name,
                                                            self.claimant_last_name, self.claimant_mobile_no,
                                                            self.claimant_email, self.claimant_address,
                                                            self.claimant_id_type, self.claimant_id_no)
    @allure.story("点击view coc")
    def test_view_coc(self):
        self.coc_no = "HCACOC65586238"

        main = PolicyPage()
        main.goto_claim_form(self.coc_no).view_coc(self.coc_no)

    @allure.story("检查coverage的Daily Hospital Income Benefit")
    def test_view_coverage_check_daily_hospital_benefit(self):
        self.coc_no = "HCACOC65586238"
        self.benefit = "Daily Hospital Income Benefit"
        self.content = "PHP1,000.00 per day (max of 15 days)"

        main = PolicyPage()
        content = main.goto_claim_form(self.coc_no).view_coverage_check_benefit(self.benefit)
        assert content == self.content

    @allure.story("检查coverage的Accidental Burial Benefit")
    def test_view_coverage_check_accidental_burial_benefit(self):
        self.coc_no = "HCACOC65586238"
        self.benefit = "Accidental Burial Benefit"
        self.content = "PHP10,000.00"

        main = PolicyPage()
        content = main.goto_claim_form(self.coc_no).view_coverage_check_benefit(self.benefit)
        assert content == self.content

    @allure.story("检查coverage的Emergency Room Assistance")
    def test_view_coverage_check_em_benefit(self):
        self.coc_no = "HCACOC65586238"
        self.benefit = "Emergency Room Assistance (sickness and accident)"
        self.content = "PHP10,000.00(one time use)"

        main = PolicyPage()
        content = main.goto_claim_form(self.coc_no).view_coverage_check_benefit(self.benefit)
        assert content == self.content

    @allure.story("检查coverage的Burial Cash Assistance due to Natural sickness")
    def test_view_coverage_check_natural_death_benefit(self):
        self.coc_no = "HCACOC65586238"
        self.benefit = "Burial Cash Assistance due to Natural sickness"
        self.content = "PHP10,000.00"

        main = PolicyPage()
        content = main.goto_claim_form(self.coc_no).view_coverage_check_benefit(self.benefit)
        assert content == self.content

    @allure.story("检查category")
    def test_check_category(self):
        self.coc_no = "HCACOC65586238"
        self.category = "Health and Personal Accident"

        main = PolicyPage()
        category = main.goto_claim_form(self.coc_no).check_category()
        assert category == self.category

    @allure.story("检查loan_term")
    def test_check_coverage_start_date(self):
        self.coc_no = "HCACOC65586238"
        self.item = "Loan Term"
        self.content = "6 months"

        main = PolicyPage()
        content = main.goto_claim_form(self.coc_no).check_item(self.item)
        assert content == self.content

    @allure.story("检查Coverage Start Date")
    def test_check_loan_term(self):
        self.coc_no = "HCACOC65586238"
        self.item = "Coverage Start Date"
        self.content = "11 / 10 / 2021"

        main = PolicyPage()
        content = main.goto_claim_form(self.coc_no).check_item(self.item)
        assert content == self.content

    @allure.story("检查Coverage Start Date")
    def test_check_loan_term(self):
        self.coc_no = "HCACOC65586238"
        self.item = "Coverage End Date"
        self.content = "11 / 11 / 2022"

        main = PolicyPage()
        content = main.goto_claim_form(self.coc_no).check_item(self.item)
        assert content == self.content


@allure.feature("claim list页面功能")
class TestClaimList:
    @allure.story("cancel pilicy：先找到可以cancel的列表，然后cancel第一个")
    def test_cancel_policy(self):
        main = PolicyPage()
        main.goto_claim_list().cancel_claim()

    @allure.story("check insured full name")
    def test_check_insured_full_name(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Insured’s Details"
        self.item = "Full Name"
        self.content = "xiong jun"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type,self.item)
        assert content == self.content

    @allure.story("check insured gender")
    def test_check_insured_gender(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Insured’s Details"
        self.item = "Gender"
        self.content = "Male"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type,self.item)
        assert content == self.content

    @allure.story("check insured Date of Birth")
    def test_check_insured_date_of_birth(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Insured’s Details"
        self.item = "Date of Birth"
        self.content = "02 / 29 / 1960"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type,self.item)
        assert content == self.content

    @allure.story("check insured Mobile Number")
    def test_check_insured_mobile_no(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Insured’s Details"
        self.item = "Mobile Number"
        self.content = "177101445487978"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type,self.item)
        assert content == self.content

    @allure.story("check insured email")
    def test_check_insured_email(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Insured’s Details"
        self.item = "Email"
        self.content = "jun.xiong@iglooinsure.com"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type,self.item)
        assert content == self.content

    @allure.story("check insured address")
    def test_check_insured_address(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Insured’s Details"
        self.item = "Address"
        self.content = "chain sichuan chengdu 1-101 t！@#¥%……&*（）——+中国四川成都1-101"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type, self.item)
        assert content == self.content

    @allure.story("check insured Identification Type")
    def test_check_insured_address(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Insured’s Details"
        self.item = "Identification Type"
        self.content = "Senior Citizen Card"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type, self.item)
        assert content == self.content

    @allure.story("check insured Identification Number")
    def test_check_insured_address(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Insured’s Details"
        self.item = "Identification Number"
        self.content = "0000011111"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type, self.item)
        assert content == self.content

    @allure.story("check Claimant’s Relationship to the Insured")
    def test_check_claimant_relationship(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Claimant’s Details"
        self.item = "Relationship to the Insured"
        self.content = "Spouse"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type, self.item)
        assert content == self.content

    @allure.story("check Claimant’s Full Name")
    def test_check_claimant_full_name(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Claimant’s Details"
        self.item = "Full Name"
        self.content = "li test ming"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type, self.item)
        assert content == self.content

    @allure.story("check Claimant’s Mobile Number")
    def test_check_claimant_mobile_no(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Claimant’s Details"
        self.item = "Mobile Number"
        self.content = "17710144558"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type, self.item)
        assert content == self.content

    @allure.story("check Claimant’s Mobile Number")
    def test_check_claimant_mobile_no(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Claimant’s Details"
        self.item = "Mobile Number"
        self.content = "17710144558"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type, self.item)
        assert content == self.content

    @allure.story("check Claimant’s Email")
    def test_check_claimant_email(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Claimant’s Details"
        self.item = "Email"
        self.content = "412882383@qqtest.com"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type, self.item)
        assert content == self.content

    @allure.story("check Claimant’s Address")
    def test_check_claimant_address(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Claimant’s Details"
        self.item = "Address"
        self.content = "test address"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type, self.item)
        assert content == self.content

    @allure.story("check Claimant’s Identification Type")
    def test_check_claimant_id_type(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Claimant’s Details"
        self.item = "Identification Type"
        self.content = "Senior Citizen Card"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type, self.item)
        assert content == self.content

    @allure.story("check Claimant’s Identification Number")
    def test_check_claimant_id_no(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Claimant’s Details"
        self.item = "Identification Number"
        self.content = "9999988888"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type, self.item)
        assert content == self.content

    @allure.story("check Reimbursement Account Name")
    def test_check_claimant_account_name(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Reimbursement Details"
        self.item = "Account Name"
        self.content = "xiongjun"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type, self.item)
        assert content == self.content

    @allure.story("check Reimbursement Account Number")
    def test_check_claimant_account_no(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Reimbursement Details"
        self.item = "Account Number"
        self.content = "123456789"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type, self.item)
        assert content == self.content

    @allure.story("check Reimbursement Bank Name")
    def test_check_claimant_account_no(self):
        self.claim_id = "HC-MICI-48440846"
        self.type = "Reimbursement Details"
        self.item = "Bank Name"
        self.content = "china bank"

        main = PolicyPage()
        content = main.goto_claim_list().goto_claim_detail(self.claim_id).check_insured_detail(self.type, self.item)
        assert content == self.content

@allure.feature("policy detail页面功能")
class TestPolicyDetail:
    @allure.story("check full name")
    def test_check_full_name(self):
        self.coc_no = "HCACOC65586238"
        self.item = "Full Name"
        self.content = "xiong jun"

        main = PolicyPage()
        content = main.goto_policy_detail(self.coc_no).check_policy_detail(self.item)
        assert content == self.content

    @allure.story("check gender")
    def test_check_full_name(self):
        self.coc_no = "HCACOC65586238"
        self.item = "Gender"
        self.content = "Male"

        main = PolicyPage()
        content = main.goto_policy_detail(self.coc_no).check_policy_detail(self.item)
        assert content == self.content

    @allure.story("check date of birth")
    def test_check_full_name(self):
        self.coc_no = "HCACOC65586238"
        self.item = "Date of Birth"
        self.content = "02 / 29 / 1960"

        main = PolicyPage()
        content = main.goto_policy_detail(self.coc_no).check_policy_detail(self.item)
        assert content == self.content

    @allure.story("check Mobile Number")
    def test_check_full_name(self):
        self.coc_no = "HCACOC65586238"
        self.item = "Mobile Number"
        self.content = "177101445487978"

        main = PolicyPage()
        content = main.goto_policy_detail(self.coc_no).check_policy_detail(self.item)
        assert content == self.content

    @allure.story("check Email")
    def test_check_full_name(self):
        self.coc_no = "HCACOC65586238"
        self.item = "Email"
        self.content = "jun.xiong@iglooinsure.com"

        main = PolicyPage()
        content = main.goto_policy_detail(self.coc_no).check_policy_detail(self.item)
        assert content == self.content

    @allure.story("check Address")
    def test_check_full_name(self):
        self.coc_no = "HCACOC65586238"
        self.item = "Address"
        self.content = "chain sichuan chengdu 1-101 t！@#¥%……&*（）——+中国四川成都1-101"

        main = PolicyPage()
        content = main.goto_policy_detail(self.coc_no).check_policy_detail(self.item)
        assert content == self.content


    @allure.story("check Loan Term")
    def test_check_full_name(self):
        self.coc_no = "HCACOC65586238"
        self.item = "Loan Term"
        self.content = "6 months"

        main = PolicyPage()
        content = main.goto_policy_detail(self.coc_no).check_policy_detail(self.item)
        assert content == self.content

    @allure.story("check Coverage Start Date")
    def test_check_full_name(self):
        self.coc_no = "HCACOC65586238"
        self.item = "Coverage Start Date"
        self.content = "11 / 10 / 2021"

        main = PolicyPage()
        content = main.goto_policy_detail(self.coc_no).check_policy_detail(self.item)
        assert content == self.content

    @allure.story("check Coverage End Date")
    def test_check_full_name(self):
        self.coc_no = "HCACOC65586238"
        self.item = "Coverage End Date"
        self.content = "11 / 11 / 2022"

        main = PolicyPage()
        content = main.goto_policy_detail(self.coc_no).check_policy_detail(self.item)
        assert content == self.content












