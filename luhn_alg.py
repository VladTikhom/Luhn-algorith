#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[2]:


def luhn_help():
    help_string = '''Скрипт для проверки корректности номера карты
    Для проверки номера необходимо ввести его в качестве аргумента командной строки:
    -o 'xxxx xxxx xxxx xxxx' или -s 'xxxx xxxx xxxx xxxx'
    
    -h: вызывает данное сообщение
    -t: вызывает тестовый запуск
    -o: запуск оригинального алгоритма
    -s: запуск упрощенного алгоритма
    '''
    print(help_string)

def luhn_test():
    test = ['4561 2612 1234 5464', '4569 0600 1250 4921']
    expect = [False, True]
    for x, y in zip(test, expect):
        print('input:\t{}'.format(x))
        print('\tSimple: {}; expected: {}'.format(luhn_simple(x), y))
        print('\tOrign: {}; expected: {}'.format(luhn_orig(x), y))


def luhn_orig(code):
    numbers = [int(digit) for digit in code.replace(' ', '')]
    for i in range(len(numbers)):
        if (i+1) % 2 == 0:
            if numbers[i]*2 > 9:
                numbers[i] = (numbers[i]*2) % 10 + (numbers[i]*2) // 10
            else:
                numbers[i] *= 2
    return sum(numbers) % 10 == 0

def luhn_simple(code):
    numbers = [int(digit) for digit in code.replace(' ', '')]
    for i in range(len(numbers)):
        if (i+1) % 2 == 0:
            if numbers[i]*2 > 9:
                numbers[i] -= 9
            else:
                numbers[i] *= 2
    return sum(numbers) % 10 == 0

if __name__ == '__main__':
    if len(sys.argv) == 1:
        luhn_help()
    else:
        mode = sys.argv[1]
        if mode == '-h':
            luhn_help()
        elif mode == '-t':
            luhn_test()
        elif mode == '-o':
            print(luhn_orig(''.join(sys.argv[2:])))
        elif mode == '-s':
            print(luhn_simple(''.join(sys.argv[2:])))
        else:
            print('Неизвестная команда, введите -h')



