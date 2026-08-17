from pathlib import Path
current_file = Path(__file__)
current_dir = Path(__file__).parent

### Робота з файлами та папками — завдання
"""
1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
# coding here
new_file = current_file.parent / "hello.txt"
new_file.write_text("Hello, Python!", encoding="utf-8")


"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
# coding here
with open(new_file, "r", encoding="utf-8") as f:
    all_text = f.read()
print(all_text)

"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
# coding here


with open(new_file, "a", encoding="utf-8") as f:
    f.write("\nLearning file operations.")


"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
# coding here
with open(new_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines[0].strip())
    print(lines[1].strip())
   


"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
# coding here
with open(new_file, "r", encoding="utf-8") as f:
    all_text = f.read()
print(len(all_text))
"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
# coding here

data_dir = current_dir / "data"
data_dir.mkdir(parents=True, exist_ok=True)
new_file2 = data_dir / "notes.txt"
new_file2.write_text("My first note.", encoding="utf-8")

"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
# coding here
all_files = [d for d in data_dir.iterdir() if d.is_file()]
print(all_files)
"""
8. **Копіювання вмісту**
   Прочитай вміст файline1 = f.redline()лу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
# coding here

with open(new_file2, "r", encoding="utf-8") as f:
    all_text2 = f.read()
    new_file_copy = data_dir / "copy.txt"
new_file_copy.write_text(all_text2, encoding="utf-8")
print(all_text2)
"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
# coding here
new_file_a = data_dir / "a.txt"
new_file_a.write_text("Hello, Python! It`s me!", )
new_file_b = data_dir / "b.txt"
new_file_b.write_text("I`m Happy!", encoding="utf-8")
text_a = new_file_a.read_text(encoding="utf-8")
text_b = new_file_b.read_text(encoding="utf-8")
file_ab = data_dir / "ab.txt"
file_ab.write_text(text_a + "\n" + text_b, encoding="utf-8")

"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `""`.
"""
# coding here
with open(new_file2, "r", encoding="utf-8") as f:
    note_text = f.read()
if "note" in note_text:
   print("Знайдено")
else:
   print("Не знайдено")