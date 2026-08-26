# -*- coding: utf-8 -*-
# Самостійне вивчення - Поглиблені задачі
# Виконайте завдання та збережіть результати у вказаних змінних

print("=== ПОГЛИБЛЕНІ ЗАДАЧІ ===")

# Task 1. Створіть список з парних чисел від 2 до 20
even_numbers = [x for x in range(2, 21) if x %2 == 0]
print(even_numbers)  # Ваш код тут

# Task 2. Відфільтруйте з списку тільки числа більше 10
numbers_list = [5, 12, 8, 15, 3, 18, 7, 20]
filtered_numbers = [x for x in numbers_list if x > 10]
print('Відсортовані числа: ', filtered_numbers)  # Ваш код тут

# Task 3. Створіть список квадратів непарних чисел від 1 до 9
odd_squares = [x**2 for x in range(1, 10) if x % 2 != 0]
print(odd_squares)  # Ваш код тут: [1, 9, 25, 49, 81]

# Task 4. Об'єднайте два списки без дублікатів
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
merged_unique = []
for x in list1 + list2:
    if x not in merged_unique:
        merged_unique.append(x)
print(merged_unique)  # Ваш код тут

# Task 5. Створіть кортеж з координатами точок
points = ((0,0), (1,1), (2,2))  # Ваш код тут: ((0,0), (1,1), (2,2))

# Task 6. Розпакуйте кортеж координат
coordinates = (10, 20, 30)
x, y, z = coordinates  # Ваш код тут

# Task 7. Створіть множину голосних літер
vowels = set('a', 'e', 'i', 'o', 'u')  # Ваш код тут: {'a', 'e', 'i', 'o', 'u'}

# Task 8. Знайдіть унікальні символи у рядку
text = "programming"
unique_chars = set(text) 
print(unique_chars) # Ваш код тут

# Task 9. Створіть множину чисел, які діляться на 3 від 1 до 15
divisible_by_3 = set(x for x in range(1, 16) if x % 3 == 0)  # Ваш код тут

# Task 10. Знайдіть симетричну різницю двох множин
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_diff = set(set1.symmetric_difference(set2))
print(symmetric_diff)  # Ваш код тут

# Task 11. Створіть словник з кількістю символів у кожному слові
words = ["cat", "dog", "elephant", "bee"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # Ваш код тут: {"cat": 3, "dog": 3, ...}

# Task 12. Створіть словник з квадратами та кубами чисел
numbers = [2, 3, 4, 5]
powers_dict = {num: {'Square': num ** 2, 'Cube': num ** 3}for num in numbers}
print(powers_dict)  # Ваш код тут: {2: {"square": 4, "cube": 8}, ...}

# Task 13. Згрупуйте слова за їх довжиною
word_list = ["apple", "cat", "dog", "banana", "car", "elephant"]
grouped_by_length = {}
for x in word_list:
    length = len(x)
    grouped_by_length.setdefault(length, []).append(x)
print(grouped_by_length)  # Ваш код тут

# Task 14. Створіть словник частоти символів у рядку
sentence = "hello world"
char_frequency = {}  # Ваш код тут

# Task 15. Об'єднайте декілька словників
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}
combined_dict = dict1 | dict2 | dict3
print(combined_dict)  # Ваш код тут

# Task 16. Інвертуйте словник (ключі стають значеннями)
original = {"name": "John", "age": 25, "city": "Kyiv"}
inverted = {}  # Ваш код тут
for key, value in original.items():
    inverted[value] = key
print(inverted)  # Ваш код тут

# Task 17. Створіть список кортежів з словника
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
score_tuples = []  # Ваш код тут: [("Alice", 95), ...]

# Task 18. Знайдіть спільні ключі у двох словниках
dict_a = {"x": 1, "y": 2, "z": 3}
dict_b = {"y": 5, "z": 6, "w": 7}
common_keys = set()  # Ваш код тут

# Task 19. Створіть вкладений словник з інформацією про студентів
students_info = {}  # Ваш код тут: {"student1": {"name": ..., "grades": [...]}, ...}

# Task 20. Сплюсніть всі списки у словнику
data = {"list1": [1, 2], "list2": [3, 4], "list3": [5, 6]}
flattened = []  
# Ваш код тут: [1, 2, 3, 4, 5, 6]


if __name__ == "__main__":
    print("\n=== ЗАВЕРШЕННЯ ===")
    print("Поглиблені завдання виконано! Запустіть test_selflearning.py для перевірки.")