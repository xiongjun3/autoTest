import time
import uuid
import random

import allure
import pytest
from jsonpath import jsonpath
from apis.admin_api import AdminApi
from up.pymysql_study.sql import query_conpany_detail, query_company_head_account, query_claim_detail
from up.pymysql_study.test_pymysql import query_db
from utils.data_handle import func_period, func_relationship, func_renew, func_maternity, func_sales_channel
from utils.logger_util import logger


@allure.feature("company")
class TestCompany:
    def setup_class(self):
        self.admin = AdminApi()
        self.company_id="UIC20457185"

    def get_uid(self):
        return str(uuid.uuid1()).split("-")[0]

    @allure.feature("company")
    @allure.story("添加company")
    @pytest.mark.parametrize("company_name,sales_channel,channel_detail,name,position,mobile,email,expect",
                             [("company", "broker", "detail", "xiongjun", "chengdu", "0123451234", "e@qq.com", 200),
                              ("company", "agent", "detail", "xiongjun", "chengdu", "0123451234", "e@qq.com", 200),
                              ("company", "direct_business", "detail", "", "chengdu", "0123451234", "e@qq.com", 200),
                              ("company", "direct_business", "detail", "", "", "", "", 200),
                              ("company", "broker", "detail", "xiongjun", "chengdu", "9123451234", "e@qq.com", 400),
                              ("", "broker", "detail", "xiongjun", "chengdu", "0123451234", "e@qq.com", 400),
                              ("company", "broker", "", "xiongjun", "chengdu", "0123451234", "e@qq.com", 400)])
    def test_add_company(self, company_name, sales_channel, channel_detail, name, position, mobile, email, expect):
        uid = self.get_uid()
        data = {"company_name": f"{company_name}_{uid}" if company_name else "",
                "sales_channel": sales_channel,
                "channel_detail": channel_detail,
            "contact_info":{"name": name,
                            "position": position,
                            "mobile": mobile,
                            "email": email}}
        logger.info(data)

        r = self.admin.add_company(data)
        logger.info(r)
        assert r.status_code == expect

    @allure.feature("company")
    @allure.story("根据company name搜索company list")
    def test_search_company_by_name(self):
        dat = query_conpany_detail(self.company_id)
        sales_channel = func_sales_channel(dat[0][3])
        dat2 = query_company_head_account(self.company_id)
        data = {"search_keyword":dat[0][1]}

        r = self.admin.company_list(data)
        assert r.json().get("total") == 1
        assert r.json().get("data")[0].get("company_id") == dat[0][0]
        assert r.json().get("data")[0].get("company_name") == dat[0][1]
        assert r.json().get("data")[0].get("channel_detail") == dat[0][2]
        assert r.json().get("data")[0].get("sales_channel") == sales_channel
        assert r.json().get("data")[0].get("promotion_link") == dat[0][4]
        assert r.json().get("data")[0].get("headcount") == dat2[0][0]

    @allure.feature("company")
    @allure.story("根据company id搜索company list")
    def test_search_company_by_id(self):
        dat = query_conpany_detail(self.company_id)
        data = {"search_keyword":dat[0][0]}

        r = self.admin.company_list(data)
        assert r.json().get("total") == 1
        assert r.json().get("data")[0].get("company_id") == dat[0][0]
        assert r.json().get("data")[0].get("company_name") == dat[0][1]
        assert r.json().get("data")[0].get("channel_detail") == dat[0][2]
        assert r.json().get("data")[0].get("promotion_link") == dat[0][4]

    @allure.feature("company")
    @allure.story("company detail")
    def test_company_detail(self):
        dat = query_conpany_detail(self.company_id)
        dat2 = query_company_head_account(self.company_id)


        r = self.admin.company_detail(self.company_id)

        assert r.json().get("company_name") == dat[0][1]
        assert r.json().get("channel_detail") == dat[0][2]
        assert r.json().get("headcount") == dat2[0][0]
        assert r.json().get("promotion_link") == dat[0][4]
        assert r.json().get("contact_info").get("email") == dat[0][6]
        assert r.json().get("contact_info").get("mobile") == dat[0][7]
        assert r.json().get("contact_info").get("name") == dat[0][5]
        assert r.json().get("contact_info").get("position") == dat[0][8]

    @allure.feature("company")
    @allure.story("查询member list的总量")
    def test_member_list(self):
        sql = f"select count(1) from member where customer_id in (select member_id from company_member_ref where " \
              f"state=1 and company_id='{self.company_id}' and is_principal=1)"
        dat = query_db(sql)
        valid_member_account = dat[0][0]

        data = {"company_id":self.company_id}
        r = self.admin.member_list(data)

        assert r.json().get("total") == valid_member_account

    @allure.feature("company")
    @allure.story("根据name查询member list")
    def test_member_list_by_name(self):
        sql = f"select name,mobile from member where customer_id in (select member_id from company_member_ref where " \
              f"state=1 and company_id='{self.company_id}' and is_principal=1)"
        dat = query_db(sql)
        member_name = dat[0][0]
        member_mobile = dat[0][1]

        data = {"company_id":self.company_id,"name":member_name}
        r = self.admin.member_list(data)
        assert r.json().get("member_list")[0].get("name") == member_name
        assert r.json().get("member_list")[0].get("mobile") == member_mobile

    @allure.feature("company")
    @allure.story("将member置为invalid")
    def test_invalid_change(self):
        data = {"change_type":"mark","company_id":self.company_id,"mobile":self.member_mobile}
        r = self.admin.invalid_change(data)
        assert r.json().get("ok") == "ok"

    @allure.feature("company")
    @allure.story("invalid member list")
    def test_invalid_list(self):
        sql = f"select count(1),name,mobile from member where customer_id in (select member_id from company_member_ref where " \
              f"state=2 and company_id='{self.company_id}' and is_principal=1)"
        dat = query_db(sql)
        invalid_member_account = dat[0][0]
        member_name = dat[0][1]
        member_mobile = dat[0][2]
        data = {"company_id":self.company_id}
        r = self.admin.invalid_list(data)
        result_json = r.json()
        a = jsonpath(result_json, "$.member_list[?(@.mobile=='"+member_mobile+"')].name")
        assert a[0] == member_name
        assert result_json.get("total") == invalid_member_account

    @allure.feature("company")
    @allure.story("将invalid member revert回来")
    def test_invalid_change_by_revert(self):
        data = {"change_type":"revert","company_id":self.company_id,"mobile":self.member_mobile}
        r = self.admin.invalid_change(data)
        assert r.json().get("ok") == "ok"

    @pytest.mark.parametrize("name,position,mobile,email,expect",
                             [("", "", "", "",  200),
                              ("", "", "0234565434", "", 200),
                              ("xiongjun", "chengdu", "0342342349", "jun.xiong@iglooinsure.com", 200)])
    @allure.feature("company")
    @allure.story("修改contact info")
    def test_modify_contact_info(self,name,position,mobile,email,expect):
        data = {
    "company_id":"UIC20457185",
    "contact_info":{
        "name":name,
        "position":position,
        "mobile":mobile,
        "email":email
    }
}
        r = self.admin.contact_info(data)
        assert r.status_code == expect

    @allure.feature("policy")
    @allure.story("policy list")
    def test_policy_list_all(self):
        sql = f"select count(1) from policy"
        dat = query_db(sql)
        policy_count = dat[0][0]
        data = {"sort_type":"desc"}
        r = self.admin.policy_list(data)
        assert r.json().get("total") == policy_count

    @allure.feature("policy")
    @allure.story("根据company No.搜索policy list")
    def test_policy_list_by_company_No(self):
        sql = "select display_id from policy order by id asc limit 1"
        dat = query_db(sql)
        policy_id = dat[0][0]
        data = {"search_keyword":policy_id}
        r = self.admin.policy_list(data)
        assert r.json().get("data")[0].get("policy_id") == policy_id

    @allure.feature("policy")
    @allure.story("根据company name搜索policy list")
    def test_policy_list_by_company_name(self):
        sql = f"select company_name from company where company_id='{self.company_id}'"
        dat = query_db(sql)
        company_name = dat[0][0]
        data = {"search_keyword":company_name}
        r = self.admin.policy_list(data)
        assert r.json().get("data")[0].get("company_name") == company_name

    @allure.feature("policy")
    @allure.story("protected policy detail ")
    def test_policy_detail_protected(self):
        sql1 = "select display_id from policy where state='PolicyProtected' ORDER BY id desc limit 1"
        dat1 = query_db(sql1)
        policy_id = dat1[0][0]
        sql2 = f"select state,plan_id,meta->'$.has_maternity',meta->'$.pay_period',meta->>'$.premium'," \
               f"meta->>'$.company_name',UNIX_TIMESTAMP(created_at)*1000 as purchase_date,UNIX_TIMESTAMP(start_at)*1000 " \
               f"as start_date,UNIX_TIMESTAMP(expire_at)*1000 as end_date,json_unquote(json_extract(meta->>'$.policy_renew','$.has_renewed'))" \
               f" as has_renewed,insured_detail->>'$.relationship',insured_detail->>'$.full_name'," \
               f"insured_detail->>'$.birth',insured_detail->>'$.gender',insured_detail->>'$.id_type'," \
               f"insured_detail->>'$.id_no',insured_detail->>'$.mobile',insured_detail->>'$.email'," \
               f"insured_detail->>'$.residential_address'from policy where display_id='{policy_id}'"
        dat2 = query_db(sql2)
        sql3 = f"select name,department,employee_code,mobile,email from member where customer_id in (select main_customer_id from policy where display_id='{policy_id}')"
        dat3 = query_db(sql3)

        billing_period = func_period(dat2[0][3])
        has_renewed = func_renew(dat2[0][9])
        has_maternity = func_maternity(dat2[0][2])
        relationship = func_relationship(dat2[0][10])

        r = self.admin.policy_detail(policy_id)
        assert r.json().get("state") == dat2[0][0]
        assert r.json().get("plan_id") == dat2[0][1]
        assert r.json().get("has_maternity") == has_maternity
        assert r.json().get("billing_period") == billing_period
        assert r.json().get("premium") == dat2[0][4]
        assert r.json().get("company_name") == dat2[0][5]
        assert r.json().get("purchase_date") == dat2[0][6]
        assert r.json().get("start_at") == dat2[0][7]
        assert r.json().get("expire_at") == dat2[0][8]
        assert r.json().get("has_renewed") == has_renewed
        assert r.json().get("insured_detail").get("relationship") == relationship
        assert r.json().get("insured_detail").get("full_name") == dat2[0][11]
        assert r.json().get("insured_detail").get("birth") == int(dat2[0][12])
        assert r.json().get("insured_detail").get("gender") == dat2[0][13]
        assert r.json().get("insured_detail").get("id_type") == dat2[0][14]
        assert r.json().get("insured_detail").get("id_no") == dat2[0][15]
        assert r.json().get("insured_detail").get("mobile") == dat2[0][16]
        assert r.json().get("insured_detail").get("email") == dat2[0][17]
        assert r.json().get("insured_detail").get("residential_address") == dat2[0][18]
        assert r.json().get("employee_detail").get("full_name") == dat3[0][0]
        assert r.json().get("employee_detail").get("department") == dat3[0][1]
        assert r.json().get("employee_detail").get("employee_code") == dat3[0][2]
        assert r.json().get("employee_detail").get("mobile") == dat3[0][3]
        assert r.json().get("employee_detail").get("email") == dat3[0][4]

    @allure.feature("policy")
    @allure.story("refunded policy detail ")
    def test_policy_detail_refunded(self):
        sql1 = "select display_id,state from policy where state='PolicyRefunded' ORDER BY id desc limit 1"
        dat1 = query_db(sql1)
        policy_id = dat1[0][0]
        sql2 = f"select JSON_UNQUOTE(json_extract(meta->>'$.refund_info','$.refund_amount'))," \
               f"JSON_UNQUOTE(json_extract(meta->>'$.refund_info','$.refund_date'))," \
               f"JSON_UNQUOTE(json_extract(meta->>'$.refund_info','$.tranct_id'))," \
               f"UNIX_TIMESTAMP(cancel_at)*1000,SUBSTRING_INDEX(meta->>'$.cancel_endorsement','?',1) from policy where display_id='{policy_id}'"
        dat2 = query_db(sql2)
        sql3 = f"select JSON_UNQUOTE(json_extract(meta->>'$.history[0]','$.operation')),json_extract(meta->>'$.history[0]','$.last_updated'),JSON_UNQUOTE(json_extract(meta->>'$.history[0]','$.user_account')) from policy where display_id='{policy_id}'"
        dat3 = query_db(sql3)
        print(f"dat3[0][0]======{dat3[0][0]}")
        r = self.admin.policy_detail(policy_id)
        assert r.json().get("state") == dat1[0][1]
        assert r.json().get("refund_info").get("refund_amount") == dat2[0][0]
        assert r.json().get("refund_info").get("refund_date") == int(dat2[0][1])
        assert r.json().get("refund_info").get("tranct_id") == dat2[0][2]
        assert r.json().get("cancel_at") == dat2[0][3]
        assert dat2[0][4] in r.json().get("cancel_endorsement")
        assert r.json().get("history")[0].get("operation") == dat3[0][0]
        assert r.json().get("history")[0].get("last_updated") == int(dat3[0][1])
        assert r.json().get("history")[0].get("user_account") == dat3[0][2]

    @allure.feature("policy")
    @allure.story("refund policy")
    def test_policy_refund(self):
        sql = "select display_id,meta->>'$.refund_premium' from policy where state='PolicyCancelled' order by id desc limit 1"
        dat = query_db(sql)
        data = {"date": round(time.time()*1000), "amount": dat[0][1], "transaction_id": str(random.randint(000000000,999999999))}
        r = self.admin.policy_refund(dat[0][0],data)
        assert r.json().get("ok") == "ok"

    @allure.feature("claim")
    @allure.story("all of claim list")
    def test_claim_list_all(self):
        sql = "SELECT count(1) from claim "
        dat = query_db(sql)
        data = {"sort_by":"created_at", "sort_type":"desc"}
        r = self.admin.claim_list(data)
        assert r.json().get("total") == dat[0][0]

    @allure.feature("claim")
    @allure.story("根据claim id搜索claim list")
    def test_claim_list_by_claim_id(self):
        sql = "SELECT UNIX_TIMESTAMP(created_at)*1000,display_id,plan_id,claim_meta->>'$.has_maternity',state,UNIX_TIMESTAMP(updated_at)*1000 from claim order by id desc"
        dat = query_db(sql)
        has_maternity = func_maternity(dat[0][3])
        data = {"sort_by":"created_at", "sort_type":"desc","search_keyword":dat[0][1]}
        sql2 = f"select display_id from  policy where id in (select policy_id from claim where display_id='{dat[0][1]}')"
        dat2 = query_db(sql2)

        r = self.admin.claim_list(data)
        assert r.json().get("data")[0].get("claim_file_date") == dat[0][0]
        assert r.json().get("data")[0].get("claim_id") == dat[0][1]
        assert r.json().get("data")[0].get("insured_plan") == dat[0][2]
        assert r.json().get("data")[0].get("maternity") == has_maternity
        assert r.json().get("data")[0].get("state") == dat[0][4]
        assert r.json().get("data")[0].get("update_date") == dat[0][5]
        assert r.json().get("data")[0].get("policy_id") == dat2[0][0]
        assert r.json().get("total") == 1

    @allure.feature("claim")
    @allure.story("根据policy no搜索claim list")
    def test_claim_list_by_policy_no(self):
        sql = "select display_id from policy where id = (select policy_id from claim order by id desc limit 1)"
        dat = query_db(sql)
        data = {"sort_by":"created_at", "sort_type":"desc","search_keyword":dat[0][0]}
        r = self.admin.claim_list(data)
        assert r.json().get("total") == 1

    @allure.feature("claim")
    @allure.story("benefit为processing_daily_hospital的claim detail")
    def test_claim_detail_processing_daily_hospital(self):
        sql = "select display_id from claim where claim_type='daily_hospital' order by id desc limit 1"
        dat = query_db(sql)

        dat2 = query_claim_detail(dat[0][0])

        r = self.admin.claim_detail(dat[0][0])
        assert r.json().get("claim_id") == dat[0][0]
        assert r.json().get("state") == dat2[0][1]
        assert r.json().get("claim_details").get("claim_reasons")[0] == dat2[0][2]
        assert r.json().get("claim_file_date") == dat2[0][3]
        assert r.json().get("insured_details").get("full_name") == dat2[0][4]
        assert r.json().get("insured_details").get("birth") == int(dat2[0][5])
        assert r.json().get("insured_details").get("gender") == dat2[0][6]
        assert r.json().get("insured_details").get("id_type") == dat2[0][7]
        assert r.json().get("insured_details").get("id_no") == dat2[0][8]
        assert r.json().get("insured_details").get("mobile") == dat2[0][9]
        assert r.json().get("insured_details").get("email") == dat2[0][10]
        assert r.json().get("insured_details").get("residential_address") == dat2[0][11]
        assert r.json().get("payment_details").get("account_name") == dat2[0][12]
        assert r.json().get("payment_details").get("bank_name") == dat2[0][13]
        assert r.json().get("payment_details").get("account_number") == dat2[0][14]
        assert r.json().get("payment_details").get("bank_address") == dat2[0][15]
        assert r.json().get("claim_details").get("hospital_start") == int(dat2[0][16])
        assert r.json().get("claim_details").get("hospital_end") == int(dat2[0][17])

    @allure.feature("claim")
    @allure.story("benefit为processing_surgery的claim detail")
    def test_claim_detail_processing_surgery(self):
        sql = "select display_id from claim where  claim_type='surgery' order by id desc limit 1"
        dat = query_db(sql)

        dat2 = query_claim_detail(dat[0][0])

        r = self.admin.claim_detail(dat[0][0])
        assert r.json().get("claim_id") == dat[0][0]
        assert r.json().get("state") == dat2[0][1]
        assert r.json().get("claim_details").get("surgery_date") == int(dat2[0][18])

    @allure.feature("claim")
    @allure.story("benefit为processing_death的claim detail")
    def test_claim_detail_processing_death(self):
        sql = "select display_id from claim where claim_type='death' order by id desc limit 1"
        dat = query_db(sql)

        dat2 = query_claim_detail(dat[0][0])

        r = self.admin.claim_detail(dat[0][0])
        assert r.json().get("claim_id") == dat[0][0]
        assert r.json().get("state") == dat2[0][1]
        assert r.json().get("claim_details").get("death_date") == int(dat2[0][19])

    @allure.feature("claim")
    @allure.story("benefit为processing_death的claim detail")
    def test_claim_detail_processing_death(self):
        sql = "select display_id from claim where  claim_type='maternity' order by id desc limit 1"
        dat = query_db(sql)

        dat2 = query_claim_detail(dat[0][0])

        r = self.admin.claim_detail(dat[0][0])
        assert r.json().get("claim_id") == dat[0][0]
        assert r.json().get("state") == dat2[0][1]
        assert r.json().get("claim_details").get("maternity_date") == int(dat2[0][20])

    @allure.feature("claim")
    @allure.story("claim approved successfully")
    def test_claim_approved(self):
        sql = "select display_id from claim where state='ClaimProcessing' order by id desc limit 1"
        dat = query_db(sql)
        data = {"approved_amount":"1","comment":"test Approval Reason"}
        r = self.admin.claim_approve(dat[0][0],data)
        assert r.json().get("ok") == ""

    @allure.feature("claim")
    @allure.story("claim approved unsuccessfully with incorrect state")
    def test_claim_approved_bad_case(self):
        sql = "select display_id from claim where state != 'ClaimProcessing' order by id desc limit 1"
        dat = query_db(sql)
        data = {"approved_amount":"1","comment":"test Approval Reason"}
        r = self.admin.claim_approve(dat[0][0],data)
        assert r.json().get("message") == "claim status is not in processing"

    @allure.feature("claim")
    @allure.story("claim fail successfully ")
    def test_claim_fail(self):
        sql = "select display_id from claim where state='ClaimAuditPending' order by id desc limit 1"
        dat = query_db(sql)
        data = {"comment":"test fail reason"}
        r = self.admin.claim_fail(dat[0][0], data)
        assert r.json().get("ok") == ""

    @allure.feature("claim")
    @allure.story("claim fail unsuccessfully with incorrect state")
    def test_claim_fail_bad_case(self):
        sql = "select display_id from claim where state!='ClaimAuditPending' order by id desc limit 1"
        dat = query_db(sql)
        data = {"comment":"test fail reason"}
        r = self.admin.claim_fail(dat[0][0], data)
        assert r.json().get("message") == "claim status is not in audit pending confirmation"

    @allure.feature("claim")
    @allure.story("claim pass successfully")
    def test_claim_pass(self):
        sql = "select display_id from claim where state='ClaimAuditPending' order by id desc limit 1"
        dat = query_db(sql)
        r = self.admin.claim_pass(dat[0][0])
        assert r.json().get("ok") == ""

    @allure.feature("claim")
    @allure.story("claim pass unsuccessfully with incorrect state")
    def test_claim_pass_bad_case(self):
        sql = "select display_id from claim where state!='ClaimAuditPending' order by id desc limit 1"
        dat = query_db(sql)
        r = self.admin.claim_pass(dat[0][0])
        assert r.json().get("message") == "claim status is not in audit pending confirmation"

    @allure.feature("claim")
    @allure.story("claim pend successfully")
    def test_claim_pend(self):
        sql = "select display_id from claim where state='ClaimProcessing' order by id desc limit 1"
        dat = query_db(sql)
        data = {"comment":"test pend reason"}
        r = self.admin.claim_pend(dat[0][0],data)
        assert r.json().get("ok") == "ok"

    @allure.feature("claim")
    @allure.story("claim pend unsuccessfully with incorrect state")
    def test_claim_pend_bad_case(self):
        sql = "select display_id from claim where state!='ClaimProcessing' order by id desc limit 1"
        dat = query_db(sql)
        data = {"comment":"test pend reason"}
        r = self.admin.claim_pend(dat[0][0],data)
        assert r.json().get("message") == "claim status is not in processing"

    @allure.feature("claim")
    @allure.story("claim reject successfully")
    def test_claim_reject(self):
        sql = "select display_id from claim where state in ('ClaimProcessing','ClaimPending') order by id desc limit 1"
        dat = query_db(sql)
        data = {"comment":"test fail reason"}
        r = self.admin.claim_reject(dat[0][0],data)
        assert r.json().get("ok") == "ok"

    @allure.feature("claim")
    @allure.story("claim reject unsuccessfully with incorrect state")
    def test_claim_reject_bad_case(self):
        sql = "select display_id from claim where state not in ('ClaimProcessing','ClaimPending') order by id desc limit 1"
        dat = query_db(sql)
        data = {"comment":"test fail reason"}
        r = self.admin.claim_reject(dat[0][0],data)
        assert r.json().get("message") == "claim status is not in processing or pending"































