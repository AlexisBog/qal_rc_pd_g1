from functools import reduce

### Завдання 1 — Зарплати

#список зарплат

salaries = [30000, 45000, 28000, 60000, 52000, 33000]

# Одразу множимо, фільтруємо і підсумовуємо
total = sum(s * 1.1 for s in salaries if s * 1.1 > 35000)
print(f"Сума: {total:.2f} грн")



# Порівняння з прикладом. Результат той самий
# 1. Підвищення на 10%
raised = list(map(lambda s: s * 1.1, salaries))

# 2. Тільки більше 35000
high = list(filter(lambda s: s > 35000, raised))

# 3. Сума
total = reduce(lambda acc, s: acc + s, high, 0)

print(f"Сума: {total:.2f} грн")  # Сума: 228700.00 грн


### Завдання 2 — Слова

text = "Python це потужна мова програмування яка підходить для різних задач"

# Розбити на слова
words = text.split()

# Тільки довші за 4 символи, в нижньому регістрі, без дублів
long_unique = sorted(set(filter(lambda w: len(w) > 4, map(str.lower, words))))

print(long_unique)
# ['мова', 'програмування', 'python', 'підходить', 'потужна', 'різних', 'задач']
# (порядок залежить від алфавіту)

long_unique_2 = sorted({w.lower() for w in text.split() if len(w) > 4})
print(long_unique_2)