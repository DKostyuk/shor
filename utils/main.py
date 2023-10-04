import datetime
import calendar
from django.contrib import auth


def datetime_string(what):
    now = datetime.datetime.now()
    file_date_now = now.strftime("%d-%m-%Y_%H-%M-%S")
    date_now = now.strftime("%Y-%m-%d")
    month_now = now.strftime("%Y-%m")
    month_now_s = datetime.datetime.strptime(month_now + '-01', '%Y-%m-%d')
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    month_prev = datetime.date(current_year, current_month - 1, 1)
    month_now_e_day = calendar.monthrange(current_year, current_month)[1]
    month_now_e = datetime.date(current_year, current_month, month_now_e_day)
    print('month_prev   ', month_prev)
    # print(month_now)
    # print(file_date_now)
    # print(type(file_date_now))
    if what == 'm_s':
        return month_now_s
    elif what == 'd':
        return date_now
    elif what == 'now':
        return now
    elif what == 'm_p':
        return month_prev
    elif what == 'm_e':
        return month_now_e


def only_dkostiuk(request):
    if auth.get_user(request).is_staff and auth.get_user(request).username == 'dkostyuk@ukr.net':
        return True
    else:
        return False
