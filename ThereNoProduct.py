import random
import datetime


def ThereNoProduct(date1: str, date2: str):

    date1 = datetime.datetime.strptime(date1, '%d-%m-%Y')
    date2 = datetime.datetime.strptime(date2, '%d-%m-%Y')

    min_date = min(date1, date2)
    max_date = max(date1, date2)

    delta = max_date - min_date
    random_days = random.randint(0, delta.days)
    random_date = min_date + datetime.timedelta(days=random_days)

    day_of_the_week = random_date.weekday()

    if day_of_the_week == 1:
        print('today is monday')

if __name__ == '__main__':
    ThereNoProduct("01-01-2020", "08-12-2000")

