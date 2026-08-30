"""
Реалізувати функцію `sum_numbers_in_list(input_list)`, яка приймає список рядків, 
де кожен рядок містить числа, розділені комами. Функція повинна повертати список 
із сум чисел для кожного рядка або відповідне повідомлення про помилку у 
випадку некоректних даних.

#### **Приклади виклику функції:**
```python
sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
sum_numbers_in_list([])  # ValueError
sum_numbers_in_list("21")  # ValueError
```
"""


def sum_numbers_in_list(string_list: list) ->list:
    """Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою."""
    #Валідація списка: повинен буди список і не повинен бути порожнім
    if not isinstance(string_list, list) or len(string_list) == 0:
        raise ValueError("Вхідні дані повинні бути не порожнім списком!")
    
    result = []
    #Обробка кожного елемента
    for item in string_list:
        try:
            # Якщо item не рядок (наприклад, int чи dict), виклик .split() викине AttributeError
            numbers = [int(num.strip()) for num in item.split(",")]
            result.append(sum(numbers))

        except AttributeError as e:
            #Виникає якщо не має методу .split
            result.append("Не можу це зробити! AttributeError")

        except ValueError as e:
            #Виникає якща не вдається перетворити на int
            result.append("Не можу це зробити!")
        
    
    return result


if __name__ == "__main__":
    output = sum_numbers_in_list(["1,2,3", "4,0,6"])
    print(output)

    output = sum_numbers_in_list(["1,2,3", "4/0,6", "asas7,8,9"])
    print(output)
    """
    sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
    sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
    sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
    sum_numbers_in_list([])  # ValueError
    sum_numbers_in_list("21")  # ValueError
    """
