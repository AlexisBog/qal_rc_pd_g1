print("Hello word")

print("Добрий ранок, Україна!") # str
print(2 + 2)
a = 2 + 2  # int

age = 18
name = "Stephan"
is_student = True # bool

print(age)

new_age = age + 1

print(new_age)

pi = 3.141595 # float


user_name = "Ivan"
user_age = 10 + 8
user_salary = 10_000_000.23 # хай ця зарплата справді буде у мене

print(user_name, user_age, user_salary)


current_year = 2026

born_year = current_year - user_age
old_year = current_year + user_age
mult = current_year * user_age
div = current_year / user_age
print("Ви народилися:", born_year, "\n", "Ваш вік старості:", old_year,)

a = 10
b = 5

if a % 4 - a // 4 > 0:
    print(1)
else:
    print(a % b)