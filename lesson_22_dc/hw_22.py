from functools import reduce


### Завдання 1. Охоронці воріт

passwords = [
    "Cossack1",
    "sich",
    "ZAPORIZHZHIA2024",
    "Sich Gate 5",
    "Mazepa99",
    "короткий1",
    "BohunTheBrave",
    "D0br0nich!",
    "аааааааА1",
    "Valid1Pass",
]

def is_strong(password):
    return (
        8 <= len(password) <= 20
        and any(c.isdigit() for c in password)
        and any(c.isupper() for c in password)
        and " " not in password
    )

strong_passwords = list(filter(lambda p: is_strong(p), passwords))
for p in strong_passwords:
    print(f"✅ {p} — надійний.")

weak_passwords = list(filter(lambda p: not is_strong(p), passwords))
for p in weak_passwords:
    print(f"❌ {p} — відхилено.")


### Завдання 2. Перепис козацького реєстру

raw_registry = [
    "  іван сірко  | полковник | 150",
    "БОГДАН ХМЕЛЬНИЦЬКИЙ | гетьман | 10000",
    "петро дорошенко|сотник|75",
    "  Іван Мазепа | гетьман | 30000 ",
    "семен палій  |  полковник  | 500",
    "  Григорій Сковорода | філософ | 0",
]

parsed_registry = list(
    map(
        lambda row: {
            "name": row.split("|")[0].strip().title(),
            "rank": row.split("|")[1].strip().capitalize(),
            "warriors": int(row.split("|")[2].strip()),
        },
        raw_registry,
    )
)

active_registry = list(filter(lambda x: x["warriors"] > 0, parsed_registry))

total_warriors = reduce(lambda acc, x: acc + x["warriors"], active_registry, 0)

sorted_registry = sorted(active_registry, key=lambda x: x["warriors"], reverse=True)

print(f"Козацький реєстр ({len(sorted_registry)} записи):")
print("────────────────────────────────────────")
print(" №  Ім'я                  Посада      Воїни")
print("────────────────────────────────────────")
for i, item in enumerate(sorted_registry, 1):
    print(f" {i:<2} {item['name']:<21} {item['rank']:<11} {item['warriors']}")
print("────────────────────────────────────────")
print(f"Разом воїнів: {total_warriors}")


### Завдання 3. Пошук козацьких шифрів

messages = [
    "А роза упала на лапу азора",
    "Козак",
    "Зараз",
    "level",
    "Python",
    "А баба",
    "racecar",
    "Запоріжжя",
    "noon",
    "Мазепа",
]

def is_palindrome(s):
    cleaned = "".join(s.lower().split())
    return cleaned == cleaned[::-1]

ciphers = list(filter(lambda m: is_palindrome(m), messages))

formatted_ciphers = list(
    map(
        lambda m: f"🔐 {m} → {''.join(m.lower().split())}",
        ciphers
    )
)

for item in formatted_ciphers:
    print(item)