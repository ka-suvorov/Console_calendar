# -*- coding: utf-8 -*-

# Импорт библиотек
import datetime
import calendar

# Инициализация переменых
now = datetime.datetime.now()
c = calendar.TextCalendar(calendar.MONDAY)
n = ''
switch = True

# Функция запуска программы
def run():
	startCalendar()

# Функция меню
def startCalendar():
	start = int(input('Наберите \"1\" Чтобы использовать Календарь.\n \"2\" - для выхода из программы: '))
	if (start == 1):
		run()
	elif (start == 2):
		switch = False
		quit()

# Функция вывода календаря на определенный месяц и год	
def calendarick():
		
	h = int(input('Введите год, начиная с нулевого Н.Э.: '))
	n = int(input('Введите номер месяца: '))

	month = c.formatmonth(h, n)
	print ('Текущее время: ' , end="")
	print(now.strftime("%d-%m-%Y"))
	print()
	print(month)
	
	print('Желаете посмотреть другой год и месяц?')
	
	startCalendar()

# Запуск программы
run()	
