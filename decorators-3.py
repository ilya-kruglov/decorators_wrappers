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


result = time_of_function(sleep_one_sec)
print(result)
# python decorators-3.py
# <function time_of_function.<locals>.wrapper at 0x7fca6a68a430>
print('======')

print(result())
# Время пошло
# Через 1.0 сек. функция вернула «Результат первой функции»
# Результат первой функции
