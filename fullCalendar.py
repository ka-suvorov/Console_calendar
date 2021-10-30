#!/usr/bin/python
# -*- coding: utf-8 -*-


#Import standart modules

import datetime
import calendar
import sys
import os
from time import sleep

#prepare to work with the colors of unix console
import colorama
from colorama import Fore, Back, Style
colorama.init()

# main program
now = datetime.datetime.now()
c = calendar.TextCalendar(calendar.MONDAY) #Set first day as Mond
n = ''
switch = True

# Функция выхода программы	
def exit():
	sleep(2)
	print(Fore.RED + 'До свидания!')
	loadShutdownAnimation()

# Функция анимации загрузки
def loadStartAnimation():
	print(Fore.MAGENTA + 'Загружаем Календарь... \n')
	sleep(0.1)
	start = ['З','а','г','р','у','ж','а', 'е ','м ','с','я']
	succsess = '\n Календарь успешно загружен!'
		
	for i in range(0, len(start)):
		sleep(0.2)
		print(Fore.GREEN, Style.BRIGHT + " ", start[i], end="")
	print(succsess)
	
# функция анимации завершения
def loadShutdownAnimation():
	global switch
	print(Fore.RED + 'Выгружаем календарь из памяти... \n')
	sleep(0.1)
	start = ['В','ы','г','р','у','ж','а', 'е ','м ','с','я']
	succsess = '\n ...Календарь завершил работу успешно!'
		
	for i in range(0, len(start)):
		sleep(0.2)
		print(Fore.RED + " ", start[i], end="")
	print(succsess)
	sleep(1)
	switch = False
	
# функция очистки дисплея с автоопределением системы и вызова игрового меню
def clearScreen():
	if (os.name == 'nt'):
		sleep(2)
		os.system('cls')
	elif (os.name == 'posix'):
		time.sleep(2)
		os.system('clear')
	else:
		print(Fore.YELLOW, Back.RED + 'Другие операционные системы не поддерживаются!')
		exit()	

#Fantion of starting Program
def run():
	clearScreen()
	startCalendar()

#Fantion of starting Calendar
def startCalendar():
	loadStartAnimation()
	start = int(input(Fore.CYAN + 'Выбери \n \"1\" для работы с календарем.\n \"2\" - для выхода из календаря: '))
	if (start < 1 or start > 2):
		run()
	elif (start == 2):
		print(Fore.RED + 'Досвидания!')
		loadShutdownAnimation()	
		
#Main cycle of Calendar					
def calendarick():
	h = int(input('Введите год: '))
	n = int(input('Введите номер месяца: '))
	if (n < 0 or n > 12):
		print(Fore.RED + 'В году 12 месяцев!')
		run()
	else:	
		month = c.formatmonth(h, n)
		print(Fore.MAGENTA + 'Текущее время: \n')
		print()
		print(now.strftime(Fore.GREEN + "%d-%m-%Y"))
		print()
		print(Fore.YELLOW + month)
		print(Fore.CYAN + 'Хотите посмотреть другую дату?')
		startCalendar()

#Initialize program	
run()	
