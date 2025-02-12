"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import os

class calc():
	def __init__(self):
		self.operation = str()
		self.number_one = float()
		self.number_two = float()

	def cls(self):
		os.system('cls' if os.name == 'nt' else 'clear')


	def input_operation(self):
		self.operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
		if (self.operation == '+') or (self.operation == '-') or (self.operation == '*') or (self.operation == '/') or (self.operation == '0'):
			if self.operation == '0':
				self.bb()
			self.calculation()
		else:
			self.cls()
			print('Вы допустили ошибку при введении операции!')
			self.input_operation()

	def input_numbers(self):
		try:
			self.number_one = float(input('Введите первое число: '))
			self.number_two = float(input('Введите второе число: '))
		except Exception as e:
			print('Допущена ошибка при вводе числа. Трай аген)')
			self.input_numbers()


	def calculation(self):
		self.input_numbers()
		if self.operation == '+':
			self.cls()
			print(f'{self.number_one} + {self.number_two} = {self.number_one + self.number_two}')
		elif self.operation == '-':
			self.cls()
			print(f'{self.number_one} - {self.number_two} = {self.number_one - self.number_two}')
		elif self.operation == '*':
			self.cls()
			print(f'{self.number_one} * {self.number_two} = {self.number_one * self.number_two}')
		elif self.operation == '/':
			self.cls()
			if self.number_two == 0:
				print('Деление на ноль!')
			else:
				print(f'{self.number_one} / {self.number_two} = {self.number_one / self.number_two}')
		self.input_operation()


	def bb(self):
		exit()


calc = calc()
calc.input_operation()