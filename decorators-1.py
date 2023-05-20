import time


def sleep_one_sec():
    # Запоминаем время перед выполнением исходной функции.
    start_time = time.time()
    # Выполняем код исходной функции:
    time.sleep(1)
    # Вычисляем, округляем и печатаем разницу
    # между временем старта и актуальным временем.
    execution_time = round(time.time() - start_time, 1)
    print(f'Время выполнения функции: {execution_time} сек.')  # 3
    return 'Результат первой функции.'  # 5


def sleep_two_sec():
    start_time = time.time()
    # Теперь выполняем код исходной функции:
    time.sleep(2)
    execution_time = round(time.time() - start_time, 1)
    print(f'Время выполнения функции: {execution_time} сек.')
    return 'Результат второй функции.'


# Функция time_of_function()
# принимает на вход тестируемую функцию
# и возвращает результат измерений:
def time_of_function(func):
    # Запоминаем время перед выполнением тестируемой функции.
    start_time = time.time()
    print('Время пошло.')  # 2
    # Вызываем тестируемую функцию.
    result = func()
    # Печатаем разницу между временем старта и актуальным временем.
    execution_time = round(time.time() - start_time, 1)
    print(f'Время выполнения функции: {execution_time} сек.')  # 4
    # Возвращаем результат выполнения тестируемой функции:
    return result  # 5


# Вызываем time_of_function(),
# передаём в неё объект — функцию sleep_one_sec (без скобок):
print(time_of_function(sleep_one_sec))  # 1

# Будет напечатано:
# Время пошло.
# Время выполнения функции: 1.0 сек.
# Время выполнения функции: 1.0 сек.
# Результат первой функции.
