from up.pymysql_study.test_pymysql import query_db


def query_conpany_detail(company_id):
    sql = f"select company_id,company_name,channel_detail,sales_channel,promotion_link,contact_info->>'$.name'," \
          f"contact_info->>'$.email',contact_info->>'$.mobile',contact_info->>'$.position' from company where company_id='{company_id}'"
    dat = query_db(sql)
    return dat

def query_company_head_account(company_id):
    sql2 = f"select sum(a) from (" \
           f"select count(1) as a from member where company_id='{company_id}' union all " \
           f"select count(1) as a from sub_member where main_customer_id in (select customer_id from member where company_id='{company_id}')" \
           f")c"
    dat2 = query_db(sql2)
    return dat2

def query_claim_detail(claim_id):
    sql = f"SELECT display_id,state,claim_type,UNIX_TIMESTAMP(created_at)*1000," \
           f"JSON_UNQUOTE(JSON_EXTRACT(claim_form->>'$.insured','$.full_name'))," \
           f"JSON_EXTRACT(claim_form->>'$.insured','$.birth'),JSON_UNQUOTE(JSON_EXTRACT(claim_form->>'$.insured','$.gender'))," \
           f"JSON_UNQUOTE(JSON_EXTRACT(claim_form->>'$.insured','$.id_type')),JSON_UNQUOTE(JSON_EXTRACT(claim_form->>'$.insured','$.id_no'))," \
           f"JSON_UNQUOTE(JSON_EXTRACT(claim_form->>'$.insured','$.mobile')),JSON_UNQUOTE(JSON_EXTRACT(claim_form->>'$.insured','$.email'))," \
           f"JSON_UNQUOTE(JSON_EXTRACT(claim_form->>'$.insured','$.residential_address')),claim_payment->>'$.account_name'," \
           f"claim_payment->>'$.bank_name',claim_payment->>'$.account_number',claim_payment->>'$.bank_address'," \
           f"claim_form->>'$.hospital_start',claim_form->>'$.hospital_end',claim_form->>'$.surgery_date',claim_form->>'$.death_date'," \
           f"claim_form->>'$.maternity_date' from claim where display_id='{claim_id}'"
    dat2 = query_db(sql)
    return dat2
