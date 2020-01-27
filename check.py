from datetime import date, datetime


def check_date_with_today(a_date):
    today = date.today().strftime("%d-%m-%Y")
    if a_date > today:
        return True
    return False


def check_two_dates(f_date, s_date):
    if s_date > f_date:
        return True
    return False


def str_to_date(str_date):
    str_date = datetime.strptime(str_date, '%Y-%m-%d')
    str_date = str_date.strftime("%d-%m-%Y")
    return str_date


def date_to_str(d):
    return str(d.strftime("%d-%m-%Y"))


def reformat_date(d):
    d = datetime.strptime(d, '%Y-%m-%d')
    d = d.strftime("%d-%m-%Y")
    return str(d)
