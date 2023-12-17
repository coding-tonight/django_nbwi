# from datetime import date
import nepali_datetime

""" datetime, date , time , mouth , day according to the nepali calendar  
"""

# get today date / year , mouth , day format
def today_date():
    return nepali_datetime.date.today()

# get today date / year, mouth , day in words formats
def formated_today_date():
    return nepali_datetime.date.today().strftime('%d %B %Y')

#  get today date / year , mouth  , day in nepali words formats
def nepali_word_foramted_today_date():
    return nepali_datetime.date().today().strftime('%K-%n-%D (%k %N %G)')


# convert the eng date into nepali date 
def convert_into_date(eng_date):
    return nepali_datetime.date.from_datetime_date(eng_date)

# get first day of the mouth 
def first_day_of_the_month_year():
    """ accessing the current year and month
    """
    current_year = nepali_datetime.date.today().year
    current_month = nepali_datetime.date.today().month
    day = 1
    return nepali_datetime.date(current_year,current_month,day)







