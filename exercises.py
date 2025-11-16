import os
from datetime import datetime
import math
import itertools
import collections
import json
import re
import requests

def file_exists(path):
    """ Проверяет существует ли файл

    Аргументы:
        - path:str имя файла, включающее путь

    Возвращает:
        - bool: True, если файл существует и False в противном случае

    Указания:
        - используйте функию isfile или exists из модуля os.path
        - авторское решение занимает 27 символов
    """
    return True if os.path.isfile(path) else False

def combinations(colors, k):
    """ Вернуть список всех сочетаний из списка colors по k

    Аргументы:
        - colors:list - список объетов
        - k:int - количество объектов в сочетании

    Возвращает:
        - list

    Пример:
    >>> combinations(['white', 'green', 'blue', 'red'], 3)
    [('white', 'green', 'blue'), ('white', 'green', 'red'), ('white', 'blue', 'red'), ('green', 'blue', 'red')]

    Указания:
        - использовать библиотеку itertools
        - авторское решение занимает 53 символа
    """
    return list(itertools.combinations(colors, k))
    #вернет список всех возможных комбинаций из k элементов

def days_between(dstr1, dstr2):
    """ Вычисляет количество дней между двумя датами

    Аргументы:
        - dstr1:str - дата в формате yyyy-mm-dd
        - dstr2:str - дата в формате yyyy-mm-dd

    Возвращает:
        - int: количество дней между dstr2 и dstr1

    Указания:
        - используйте модуль datetime
        - авторское решение занимает 67 символов
    """
    return abs((datetime.fromisoformat(dstr2)-datetime.fromisoformat(dstr1)).days)
    # datetime.fromisoformat преобразует строку в объект datetime, 
    

def get_current_week(day, month, year):
    """ Получить номер недели в году для заданной даты в ISO-формате

    Аргументы:
        - day:int - день
        - month:int - месяц
        - year:int - год

    Возвращает:
        - int: номер недели

    Указания:
        - используйте библиотеку datetime (функции datetime, isocalendar)
        - подробнее про ISO-формат даты можно прочитать здесь https://en.wikipedia.org/wiki/ISO_week_date
          (обратите внимание, что в этом формате номер недели для 1 января 2006 равен 52)
        - авторское решение занимает 74 символа
    """
    return datetime(year, month, day).isocalendar()[1]
    # datetime() создает объект даты из компонентов, .isocalendar() возвращает кортеж (год, номер недели, день недели) в ISO-формате, второй элемент будет номером недели

def deg2rad(degree):
    """ Перевести градусы в радианы

    Аргументы:
        - degree:float - градусы

    Возвращает:
        - float: радианы

    Указания:
        - в библиотеке math есть число pi
        - авторское решение занимает 20 символов

    """
    return math.radians(degree)

def discriminant_sqrt(a, b, c):
    """ Вычислить корень из дискриминанта квадратного уравнения.
    Если корень извлекается из отрицательной величины, вывести `math.nan`, что означает not a number

    Аргументы:
        - a, b, c: float, коэффициенты квадратного уравнения ax^2 + bx + c = 0

    Возвращает:
        - float: корень из дискриминанта
    
    Пример:
    >>> discriminant_sqrt(4, 5, 1)
    3.0
    >>> discriminant_sqrt(40, 5, 1)
    nan

    Указания:
        - воспользоваться библиотекой math
        - авторское решение занимает 65 символов

    """
    D = b*b - 4*a*c
    return math.sqrt(D) if D >= 0 else math.nan

def popular_letters(s):
    """ В заданной строке `s` определить три самых используемых символа. Вернуть список из символов в порядке убывания

    Аргументы:
        - s:str

    Возвращает:
        - list: список трех самых используемых символов в строке

    Пример:
    >>> popular_letters("baaaaccddd")
    ['a', 'd', 'c']

    Указания:
        - гарантируется, что в строке такие символы существуют
        - воспользоваться библиотекой collections.Counter
        - авторское решение занимает 49 символов
    """
    return [x for x, _ in collections.Counter(s).most_common(3)]
    # Counter(s) подсчитывает частоту каждого символа, .most_common(3) возвращает 3 самых частых символа с их частотами

def json_write(dictionary, file):
    """ Записать в файл file словарь dictionary с отсортированными в алфавитном порядке ключами

    Аргументы:
        - dictionary:dict - неотсортированный словарь
        - file:str - путь к файлу

    Указания:
        - обратить внимание на аргументы метода json.dumps
        - авторское решение занимает 3 строки
    """
    with open(file, 'w') as f:
        f.write(json.dumps(dictionary, sort_keys=True))
    # json.dumps() преобразует словарь в JSON-строку, sort_keys=True сортирует ключи в алфавитном(!) порядке

def replacer(text, pattern):
    """ Заменить все слова в строке `text`, которые содержат паттерн `pattern` на `***`, и вернуть результат.
    Гарантируется, что в словах нет дефисов и других небуквенных символов.

    Аргументы:
        - text:str
        - pattern:str

    Возвращает:
        - str
    
    Пример:
    >>> replacer("Hello, world. I am working on a task. Work, work, work", "wor")
    Hello, ***. I am *** on a task. Work, ***, ***
    >>> replacer("Regular expressions are beautiful", "u")
    *** expressions are ***

    Указания:
        - обратить внимание библиотеку `re`
        - обратить внимание на r- и f-строки
        - авторское решение занимает 47 символов
    """
    return re.sub(rf'\b\w*{re.escape(pattern)}\w*\b', '***', text)
    # r убирает escape-последовательности, f позволяет работать с паттерном
    # re.sub() заменяет все совпадения на ***
    # re.escape(pattern) выделяет специальные символы в шаблоне
    # \b обозначает границы слов

def is_holiday(date, countrycode='RU'):
    """ Проверить, является ли день `date` в стране `countrycode` праздничным с помощью api

    Аргументы:
        - date:str - дата в формате yyyy-mm-dd
        - countrycode:str - код страны (по умолчанию 'RU'), список доступных стран можно найти здесь https://date.nager.at/api/v3/AvailableCountries

    Возвращает:
        - bool
    
    Пример:
    >>> is_holiday('2017-06-12')
    True
    >>> is_holiday('2020-07-13')
    False
    >>> is_holiday('2022-04-18', 'GB')
    True

    Указания:
        - гарантируется, что введённая дата и код страны корректны
        - запрос `https://date.nager.at/api/v3/PublicHolidays/2020/RU` выдаёт ответ в json со всеми праздничными датами в России в 2020 году
        - получить ответ на запрос можно с помощью requests.get
        - обработать ответ можно с помощью json
        - авторское решение составляет 2 строки
    """
    year = date.split('-')[0] #извлекаем год из даты
    response = requests.get(f'https://date.nager.at/api/v3/PublicHolidays/{year}/{countrycode}') #запрос к api праздников, преобразует ответ в список словарей
    holidays = response.json()
    return bool(any(holiday['date'] == date for holiday in holidays)) #проверяет есть ли указанная дата в списке праздников