from datetime import date, datetime


def check_date_with_today(a_date):
    a_date = datetime.strptime(a_date, "%d-%m-%Y")
    today = datetime.today()
    if a_date > today:
        return True
    return False


def check_two_dates(f_date, s_date):
    f_date = datetime.strptime(f_date, "%d-%m-%Y")
    s_date = datetime.strptime(s_date, "%d-%m-%Y")
    if s_date > f_date:
        return True
    return False


def str_to_date(str_date):
    str_date = datetime.strptime(str_date, '%Y-%m-%d')
    str_date = str_date.strftime("%d-%m-%Y")
    return str_date


def convert_date_for_event(str_date):
    str_date = datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
    str_date = str_date.isoformat()
    return str(str_date)


def change_date_format(str_date):
    str_date = datetime.strptime(str_date, "%d-%m-%Y  %H:%M:%S")
    str_date = str_date.strftime("%Y-%m-%d  %H:%M:%S")
    return str(str_date)


def date_to_str(d):
    return str(d.strftime("%d-%m-%Y"))


def reformat_date(d):
    d = datetime.strptime(d, '%Y-%m-%d')
    d = d.strftime("%d-%m-%Y")
    return str(d)


def get_today_date():
    today = date.today().strftime("%Y-%m-%d")
    return today
