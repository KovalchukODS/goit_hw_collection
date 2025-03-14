import datetime as dt
from datetime import datetime as dtdt, timedelta as td

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def get_upcoming_birthdays(users):
    current_day = dtdt.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = dtdt.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=current_day.year)
        
        if birthday_this_year < current_day:
            birthday_this_year = birthday_this_year.replace(year=current_day.year + 1)
        
        days_until_birthday = (birthday_this_year - current_day).days
        
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() in [5, 6]:
                congratulation_date += td(days=(7 - congratulation_date.weekday()))
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)