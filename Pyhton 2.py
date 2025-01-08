import datetime
import calendar
def get_weekday(day,month,year):
    week_days = ['Понедельник', 'Вторник', 'Среда','Четверг','Пятница','Суббота', 'Воскресенье']
    return week_days[calendar.weekday(year, month, day)]

def is_leap_year(year):
   return calendar.isleap(year)

def calculate_age(year):
   current_year = datetime.datetime.now().year
   return current_year - year

day = int(input('Введите день рождения:'))
month = int(input('Введите месяц рождения:'))
year = int(input('Введите год рождения:'))

print('День недели вашего рождения:', get_weekday(day, month, year))
print('Год вашего рождения был високосный:', is_leap_year(year))
print('Вам сейчас', calculate_age(year), 'лет')

print('*' * len(str(day)), '*' * len(str(month)), '*' * len(str(year)), sep=' ')
