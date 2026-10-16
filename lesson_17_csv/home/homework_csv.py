import csv
from pathlib import Path


def read_file(filepath: Path) -> list:
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
    

def write_csv(filepath: Path, content:list):
    if not content:
        print(f"Немає даних для запису у {filepath.name}")
        return
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=content[0].keys())
        writer.writeheader()
        writer.writerows(content)

def to_tuples(rows: list) -> list:
    return[tuple(row.items()) for row in rows]

def find_duplicates(data_1: list, data_2: list) -> tuple[list, int]:
    rows_1 = to_tuples(data_1)
    rows_2 = to_tuples(data_2)

    l1, l2 = len(rows_1), len(rows_2)

    set_1 = set(rows_1)
    set_2 = set(rows_2)

    s1, s2 = len(set_1), len(set_2)

    internal_duplicates = 0
    if l1 != s1:
        internal_duplicates += l1 - s1
        print(f"Дублікати всередині users_1.csv: {l1 - s1}")
    if l2 != s2:
        internal_duplicates += l2 - s2
        print(f"Дублікати всередині users_1.csv: {l2 - s2}")

    cross_duplicates = set_1 & set_2 # Спільні рядки
    unique_tuples = set_1 | set_2    # Об'єднання без повторів

    total_duplicates = internal_duplicates + len(cross_duplicates)

    # Назад у dict для запису csv
    unique_rows = [dict(row) for row in unique_tuples]

    return unique_rows, total_duplicates


def main(data_1, data_2):
    unique_rows, duplicates_count = find_duplicates(data_1, data_2)

    output_path = Path(__file__).parent/"clean_users_3.csv"
    write_csv(output_path, unique_rows)

    print(f"Знайдено дублікатів: {duplicates_count}")
    print(f"Унікальних записів збережено: {len(unique_rows)}")
    print(f"Файл: {output_path.name}")



if __name__ == "__main__":
    my_csv_1 = Path(__file__).parent / "users_1.csv"
    my_csv_2 = Path(__file__).parent / "users_2.csv"
    content_1 = read_file(my_csv_1)
    content_2 = read_file(my_csv_2)

    main(content_1, content_2)