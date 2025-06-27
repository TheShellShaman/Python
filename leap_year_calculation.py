#is year leap year?
def is_year_leap(year):
        if year % 4 != 0 :
            return False
        elif year % 100 != 0 :
            return True
        elif year % 400 != 0 :
            return False
        else:
             return True

#how many days in a month
def days_in_month(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

#day of the year
def day_of_year(year,month,day):
    if year < 1582 or month < 1 or month >12 or day < 1 or day > 31:
        return None
    
    max_day = days_in_month(year, month)
    if day < 1 or day > max_day :
        return None


    days = 0
    for m in range(1, month):
        days += days_in_month(year, m)
        if days == None:
            return None
    days += day
    return days

print(day_of_year(2000,12,31))
