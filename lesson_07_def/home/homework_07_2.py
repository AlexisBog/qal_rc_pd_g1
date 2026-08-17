# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
            result = number * multiplier
            # десь тут помилка, а може не одна
            if  result > 25:
                # Enter the action to take if the result is greater than 25
                break
            print(str(number) + "x" + str(multiplier) + "=" + str(result))
    
            # Increment the appropriate variable
            multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def calc(a, b):
    """складання чисел"""
    return(a + b)


print(calc())

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arifmetic(numbers):
    """Cереднє арифметичне списку чисел"""
    return  (sum(numbers) / len(numbers))


print(arifmetic())
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(rev_s):
    return rev_s[::-1]


print(reverse_string())

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def max_word(m_w):
    return max(m_w, key = len)


print(max_word())

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""
'''#Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
dupl = len(big_list) == len(set(big_list))
print('Наявніть дублікатів - ', dupl)'''

def has_duplicates(lst):
    '''Виявлення дублікатів в списку'''
    return len(lst) != len(set(lst))

print(has_duplicates())


'''# Обчисліть суму елементів двох змінних через sum()
value_1  = [1, 2, 3, 4, 5]
value_2 = (4, 6, 5, 10)'''

def total_sum(lst1, lst2):
    """Обчислення суми двох змінних"""
    return sum(lst1) + sum(lst2)


'''# Лічильник голосних ("=== ВПРАВА 4: Лічильник голосних ===")
print("Підрахуйте кількість голосних у рядку")'''

vowels = "аєеиіїоуюя"
def count_vowels(text):
    """Підрахунок кількості голосних у тексті"""
    count = 0
    for v in vowels:
        count += text.lower().count(v)
    return count


print(count_vowels())


"""
Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо колір прибульця green, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця yellow, надрукуйте, що гравець щойно заробив 10 балів.
Якщо колір прибульця red - надрукуйте, що гравець щойно заробив 15 балів.
Перевірте роботу гри самостійно, змінюючи значення alien_color
"""
def win(color):
    """Міні гра"""

   
    if color == 'green':
        return 'Вітаю! Ви заробили 5 балів!'
    elif color == 'yellow':
        return 'Вітаю! Ви заробили 10 балів!'
    elif color == 'red':
        return 'Вітаю! Ви заробили 15 балів!'
    else:
        return 'Щось пішло не так!'
while True:
        alien_color = input("Введіть колір: red, green або yellow \n").lower().strip()
        if alien_color == 'exit':
            break
        print(win(alien_color))

        