"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def rec(number,kk,kk2):
	k=kk
	k2=kk2
	num = int()
	if number%2 == 0:
		k += 1
	else:
		k2 += 1
	num = number // 10
	if  num > 0:
		rec(num,k,k2)
	elif num == 0:
		print(f'Четных цифр - {k}, нечетных цифр - {k2}')

k = int()
k2 = int()
rec(279434325634726,k,k2)
rec(123,k,k2)