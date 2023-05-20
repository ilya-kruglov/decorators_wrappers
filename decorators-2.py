import time


def sleep_two_sec():
    start_time = time.time()
    # Теперь выполняем код исходной функции:
    time.sleep(2)
    execution_time = round(time.time() - start_time, 1)
    print(f'Время выполнения функции: {execution_time} сек.')
    return 'Результат второй функции.'


# Принимает на вход функцию:
def time_of_function(func):
    # Объявляем внутреннюю функцию — её-то и вернём, когда опишем.
    def wrapper():
        start_time = time.time()
        print('Время пошло')

        # Вызываем полученную функцию и
        # cохраняем результат её выполнения в переменную.
        result = func()

        execution_time = round(time.time() - start_time, 1)
        # Можем использовать результат выполнения полученной функции:
        print(f'Через {execution_time} сек функция вернула «{result}»')
        # Возвращаем результат выполнения полученной функции.
        return result
    # Возвращаем функцию wrapper, но не вызываем её:
    return wrapper


print(time_of_function(sleep_two_sec))

# python decorators-2.py
# <function time_of_function.<locals>.wrapper at 0x7f48f5c51430>
