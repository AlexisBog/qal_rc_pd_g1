import json
import os

## Завдання 1: Перші кроки — серіалізація вручну

record_dict = {
    "title": "Ой у лузі червона калина",
    "genre": "Пісня",
    "region": "Полтавщина",
    "narrator": "Ганна Остапенко",
    "year": 1932,
    "content": "Ой у лузі червона калина похилилася...",
    "tags": ["козацька", "народна", "сумні пісні"],
    "verified": True
}

raw_json = json.dumps(record_dict)
print(f"1. RAW json: {raw_json}")
print(f"Тип raw_json: {type(raw_json)}\n")

# Форматований json рядок

nice_json = json.dumps(record_dict, indent = 4, ensure_ascii = False)
print(f"Formated json(indent = 4, ensure_ascii = False):")
print(nice_json)
print("-" *50)

# Відновлення об'єкта
restored_dict = json.loads(nice_json)
print(f"\n Restored type: {type(restored_dict)}")
print(f"Назва: {restored_dict['title']}")
print(f"Рік: {restored_dict['year']}")
print(f"Автевтичність перевірено: {restored_dict['verified']}")
print("-" *50)

## Завдання 2: Архів експедиції — запис і читання файлу

archive_data = [
    {
        "title": "Ой у лузі червона калина",
        "genre": "пісня",
        "region": "Полтавщина",
        "narrator": "Ганна Остапенко",
        "year": 1932,
        "content": "Текст пісні...",
        "tags": ["історична", "козацька"],
        "verified": True,
    },
    {
        "title": "Про лисицю та журавля",
        "genre": "казка",
        "region": "Поділля",
        "narrator": "Іван Мельник",
        "year": 1954,
        "content": "Жили собі лисиця та журавель...",
        "tags": ["про тварин", "повчальна"],
        "verified": True,
    },
    {
        "title": "Легенда про дніпровські пороги",
        "genre": "легенда",
        "region": "Запоріжжя",
        "narrator": "Степан Коваль",
        "year": 1961,
        "content": "Колись давно на Дніпрі...",
        "tags": ["природа", "історія"],
        "verified": False,
    },
    {
        "title": "Сім раз відмір — один раз відріж",
        "genre": "прислів'я",
        "region": "Слобожанщина",
        "narrator": "Марія Шевченко",
        "year": 1978,
        "content": "Мудрість про обачність.",
        "tags": ["мудрість", "короткі вислови"],
        "verified": True,
    },
    {
        "title": "Ой ходить сон коло вікон",
        "genre": "пісня",
        "region": "Галичина",
        "narrator": "Олена Бойко",
        "year": 1948,
        "content": "Колискова пісня...",
        "tags": ["колискова", "родино-побутова"],
        "verified": True,
    }
]
# Збереження у файл
with open("folklore_archive.json", "w", encoding="utf-8") as f:
    json.dump(archive_data, f, indent= 4, ensure_ascii=False)

# Читання з файлу
with open("folklore_archive.json", "r", encoding="utf-8") as f:
    loaded_archive = json.load(f)

print(f"Кількість записів: {len(loaded_archive)}")

for ind, rec in enumerate(loaded_archive, 1):
    print(f'{ind}. "{rec["title"]}" ({rec['genre']}, {rec['region']})')
    print("\n")

## Завдання 3: Клас `FolkloreRecord`


class FolkloreRecord:
    def __init__(
        self,
        title: str,
        genre: str,
        region: str,
        narrator: str,
        year: int,
        content: str,
        tags: list, 
        verified: bool
    ) ->None:
        self.title = title
        self.genre = genre
        self.region = region
        self.narrator = narrator
        self.year = year
        self.content = content
        self.tags = tags
        self.verified = verified

    def to_dict(self) -> dict:
        return{
            "title": self.title,
            "genre": self.genre,
            "region": self.region,
            "narrator": self.narrator,
            "year": self.year,
            "content": self.content,
            "tags": self.tags,
            "verified": self.verified
        }
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data.get("title", ""),
            genre=data.get("genre", ""),
            region=data.get("region", ""),
            narrator=data.get("narrator", ""),
            year=data.get("year", 0),
            content=data.get("content", ""),
            tags=data.get("tags", []),
            verified=data.get("verified", False)
        )

    def __str__(self) -> str:
        return f'[{self.genre}] "{self.title}" — {self.region}, {self.year} (оповідач: {self.narrator})'

# Перевірка повного циклу

rec1 = FolkloreRecord(
    "Ой у лузі червона калина",
    "пісня",
    "Полтавщина",
    "Ганна Остапенко",
    1932,
    "...",
    ["історична"],
    True,
)
rec2 = FolkloreRecord(
    "Про лисицю та журавля",
    "казка",
    "Поділля",
    "Іван Мельник",
    1954,
    "...",
    ["казка"],
    True,
)
rec3 = FolkloreRecord(
    "Засвіт встали козаченьки",
    "пісня",
    "Харківщина",
    "Петро Бондар",
    1928,
    "...",
    ["козацька"],
    True,
)

initial_record = [rec1, rec2, rec3]

# Збереження

with open("records.json", "w", encoding="utf-8") as f:
    json.dump([r.to_dict() for r in initial_record], f, indent= 4, ensure_ascii=False)

# завантаження та відновлення

with open("records.json", "r", encoding="utf-8") as d:
    raw_records_data = json.load(d)
    restored_records = [FolkloreRecord.from_dict(d) for d in raw_records_data]

print("Відновлені об'єкти FolkloreRecord:")
for r in restored_records:
    print(r)
print("\n")


## Завдання 4: Клас `FieldExpedition`

class FieldExpedition:
    def __init__(
        self,
        expedition_id: str,
        researcher: str,
        location: str,
        date: str,
        records = None
    ):
        self.expedition_id = expedition_id
        self.researcher = researcher
        self.location = location
        self.date = date
        self.records = records if records is not None else []

    def add_record(self, record: FolkloreRecord):
        for r in self.records:
            if r.title.strip().lower() == record.title.strip().lower():
                return f"Запис '{record.title}' вже є в експедиції"
        self.records.append(record)
        return f"Запис '{record.title}' успішно додано"

    def remove_record(self, title: str):
        for r in self.records:
            if r.title.strip().lower() == title.strip().lower():
                self.records.remove(r)
                return f"Запис '{title}' видалено"
        return f"Запис '{title}' не знайдено"

    def find_by_genre(self, genre: str) -> list:
        return [
            r for r in self.records if r.genre.lower() == genre.strip().lower()
        ]

    def to_dict(self) -> dict:
        return {
            "expedition_id": self.expedition_id,
            "researcher": self.researcher,
            "location": self.location,
            "date": self.date,
            "records": [r.to_dict() for r in self.records],
        }

    @classmethod
    def from_dict(cls, data: dict):
        exp = cls(
            expedition_id=data.get("expedition_id", ""),
            researcher=data.get("researcher", ""),
            location=data.get("location", ""),
            date=data.get("date", ""),
        )
        records_raw = data.get("records", [])
        exp.records = [FolkloreRecord.from_dict(r) for r in records_raw]
        return exp

    def save(self, filepath: str):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4, ensure_ascii=False)

    @classmethod
    def load(cls, filepath: str):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                return cls.from_dict(data)
        except FileNotFoundError:
            print(f"[Помилка] Файл '{filepath}' не знайдено.")
            return None
        except json.JSONDecodeError:
            print(f"[Помилка] Файл '{filepath}' містить пошкоджений JSON.")
            return None

# Перевірка

exp1 = FieldExpedition(
    "EXP-001", "Дмитро Яворницький", "Диканька", "2024-05-12"
)
exp1.add_record(
    FolkloreRecord(
        "Ой у лузі червона калина",
        "пісня",
        "Полтавщина",
        "Ганна Остапенко",
        1932,
        "...",
        [],
        True,
    )
)
exp1.add_record(
    FolkloreRecord(
        "Котигорошко",
        "казка",
        "Полтавщина",
        "Василь Ткаченко",
        1940,
        "...",
        [],
        True,
    )
)
exp1.add_record(
    FolkloreRecord(
        "Цвіте терен",
        "пісня",
        "Полтавщина",
        "Марія Коваль",
        1951,
        "...",
        [],
        True,
    )
)
exp1.add_record(
    FolkloreRecord(
        "Про дівчину-семилітку",
        "казка",
        "Полтавщина",
        "Софія Русова",
        1938,
        "...",
        [],
        False,
    )
)

exp1.save("expedition_1.json")

# Завантаження у новий об'єкт
exp1_loaded = FieldExpedition.load("expedition_1.json")
print(
    f"Завантажено експедицію ID: {exp1_loaded.expedition_id}, Дослідник: {exp1_loaded.researcher}"
)

# Пошук пісень
songs = exp1_loaded.find_by_genre("пісня")
print(f"Знайдено пісень у експедиції ({len(songs)}):")
for s in songs:
    print(f"  - {s.title}")

# Видалення запису та збереження
print(exp1_loaded.remove_record("Котигорошко"))
exp1_loaded.save("expedition_1.json")
print("\n")


## Завдання 5: Центральний архів — робота з колекцією файлів

# Створення додаткових експедицій

exp2 = FieldExpedition("EXP-002", "Филерет Колесса", "Стрий", "2024-06-20")
exp2.add_record(
    FolkloreRecord(
        "Ой у лузі червона калина",
        "пісня",
        "Харківщина",
        "Іван Петренко",
        1925,
        "...",
        [],
        True,
    )
)
exp2.add_record(
    FolkloreRecord(
        "Ой ходить сон коло вікон",
        "пісня",
        "Галичина",
        "Олена Бойко",
        1948,
        "...",
        [],
        True,
    )
)
exp2.save("expedition_2.json")

exp3 = FieldExpedition("EXP-003", "Микола Сумцов", "Охтирка", "2024-07-15")
exp3.add_record(
    FolkloreRecord(
        "Ой у лузі червона калина",
        "пісня",
        "Київщина",
        "Олексій Сидоренко",
        1935,
        "...",
        [],
        True,
    )
)
exp3.add_record(
    FolkloreRecord(
        "Про лисицю та журавля",
        "казка",
        "Поділля",
        "Іван Мельник",
        1954,
        "...",
        [],
        False,
    )
)
exp3.save("expedition_3.json")

def merge_archives(filepaths: list) -> list:
    all_records = []
    for path in filepaths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                exp = FieldExpedition.from_dict(data)
                all_records.extend(exp.records)
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(
                f"[Попередження] Не вдалося завантажити файл '{path}'. Пропущено. Деталі: {e}"
            )
    return all_records

def filter_records(records, genre=None, region=None, verified=None) -> list:
    filtered = []
    for r in records:
        if genre is not None and r.genre.lower() != genre.strip().lower():
            continue
        if region is not None and r.region.lower() != region.strip().lower():
            continue
        if verified is not None and r.verified != verified:
            continue
        filtered.append(r)
    return filtered

def export_summary(records, filepath):
    summary = [
        {
            "title": r.title,
            "genre": r.genre,
            "region": r.region,
            "verified": r.verified,
        }
        for r in records
    ]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4, ensure_ascii=False)




file_list = ["expedition_1.json", "expedition_2.json", "expedition_3.json"]
merged_records = merge_archives(file_list)
print(f"Всього об'єднано записів із {len(file_list)} файлів: {len(merged_records)}")


filtered = filter_records(
    merged_records, genre="пісня", region="Полтавщина", verified=True
)
print(f"Знайдено записів за фільтром: {len(filtered)}")
for item in filtered:
    print(f"  - {item}")

# Експорт зведення
export_summary(filtered, "summary.json")
print("Зведення успішно збережено у 'summary.json'\n")



def find_duplicates(filepaths: list) -> dict:
    title_to_regions = {}

    for path in filepaths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                records = data.get("records", [])
                for r in records:
                    title = r.get("title", "").strip()
                    region = r.get("region", "").strip()
                    if not title:
                        continue

                    matched_key = None
                    for existing_title in title_to_regions.keys():
                        if existing_title.lower() == title.lower():
                            matched_key = existing_title
                            break

                    if matched_key:
                        if region and region not in title_to_regions[matched_key]:
                            title_to_regions[matched_key].append(region)
                    else:
                        title_to_regions[title] = [region] if region else []
        except Exception as e:
            print(f"[Попередження] Помилка обробки файлу '{path}': {e}")

    duplicates = {
        title: regions
        for title, regions in title_to_regions.items()
        if len(regions) > 1
    }

    return duplicates

duplicates_result = find_duplicates(file_list)
print("Виявлені дублікати (варіанти в різних регіонах):")
print(json.dumps(duplicates_result, indent=4, ensure_ascii=False))