def func_period(pay_period):
    billing_period = ""
    if pay_period == "1":
        billing_period = "Monthly"
    elif pay_period == "2":
        billing_period = "HalfYearly"
    elif pay_period == "3":
        billing_period = "Yearly"
    return billing_period

def func_relationship(r):
    relationship = ""
    if r == "1":
        relationship = "self"
    elif r == "2":
        relationship = "spouse"
    elif r == "3":
        relationship = "father"
    elif r == "4":
        relationship = "mother"
    elif r == "5":
        relationship = "child"
    elif r == "6":
        relationship = "sister"
    elif r == "7":
        relationship = "brother"
    elif r == "8":
        relationship = "aunt"
    elif r == "9":
        relationship = "uncle"
    elif r == "10":
        relationship = "paternal_grandfather"
    elif r == "11":
        relationship = "paternal_grandmother"
    elif r == "12":
        relationship = "maternal_grandfather"
    elif r == "13":
        relationship = "maternal_grandmother"

    return relationship

def func_renew(re):
    has_renewed = False
    if re == "false":
        has_renewed = False
    elif re == "true":
        has_renewed = True
    return has_renewed

def func_maternity(ma):
    has_maternity = False
    if ma == "false":
        has_maternity = False
    elif ma == "true":
        has_maternity = True
    return has_maternity

def func_sales_channel(ch):
    sales_channel = ""
    if ch == 1:
        sales_channel = "broker"
    elif ch == 2:
        sales_channel = "agent"
    elif ch == 3:
        sales_channel = "direct_business"
    return sales_channel