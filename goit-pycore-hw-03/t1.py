import datetime as dt
from datetime import datetime as dtdt

def get_days_from_today(date: str) -> int:
    try:
        current_date = dtdt.today().date()
        date_from_arg = dtdt.strptime(date, "%Y-%m-%d").date()
        days_giff = (current_date - date_from_arg).days
        print(f'The difference between dates {date} and {current_date} is {days_giff}')
        return days_giff
    except Exception:
        print('Type date in \'yyyy-mm-dd\' format ')

get_days_from_today("2027-10-09")
get_days_from_today(21)