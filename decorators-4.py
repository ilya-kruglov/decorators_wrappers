import time


def sleep_one_sec():
    time.sleep(1)
    return 'Результат первой функции'  # 3


def time_of_function(func):
    def wrapper():
        start_time = time.time()
        print('Время пошло')  # 1
        result = func()
        execution_time = round(time.time() - start_time, 1)
        print(f'Через {execution_time} сек. функция вернула «{result}»')  # 2
        return result
    return wrapper


print('1 start')
sleep_one_sec
#
print('-1 end-')
print()
print('2 start')
print(sleep_one_sec)
# <function sleep_one_sec at 0x7fbedf8a00d0>
print('-2 end-')
print()
print('3 start')
sleep_one_sec()
#
print('-3 end-')
print()
print('4 start')
print(sleep_one_sec())
# Результат первой функции
print('-4 end-')
print()
print('5 start')
time_of_function(sleep_one_sec)
#
print('-5 end-')
print()
print('6 start')
print(time_of_function(sleep_one_sec))
# <function time_of_function.<locals>.wrapper at 0x7faefc28a430>
print('-6 end-')
print()
print('7 start')
time_of_function(sleep_one_sec)()
# Время пошло
# Через 1.0 сек. функция вернула «Результат первой функции»
print('-7 end-')
print()
print('8 start')
print(time_of_function(sleep_one_sec)())
# Время пошло
# Через 1.0 сек. функция вернула «Результат первой функции»
# Результат первой функции
print('-8 end-')
print()
