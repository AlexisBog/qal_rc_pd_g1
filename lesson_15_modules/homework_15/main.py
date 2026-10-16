from vernadsky_lab import (
    register_mineral,
    record,
    summary,
    mineral_report,
    to_csv
)

print("=== Лабораторія Вернадського ===\n")

print("Реєстрація мінералів:")
print(register_mineral("Берил", "Be3Al2Si6O18", 8, "Урал", 1828))
print(register_mineral("Кварц", "SiO₂", 7, "Урал", 1845))
print(register_mineral("Кварц", "SiO₂", 7, "Урал", 1845))
print()

print("Запис спостережень:")
print(record("Вернадський", "Берил", "прозорий кристал зеленуватого відтінку"))
print(record("Ферсман", "Кварц", "прозорий, без включень"))
print(record("Вернадський", "Кварц", "виражена кристалічна решітка"))
print(record("Вернадський", "Малахіт", "темно-зелений з візерунком"))  # Спроба записати відсутній мінерал
print()

print(summary())
print()

print(mineral_report("Кварц"))
print()

# Експорт у CSV
print(to_csv("vernadsky_journal.csv"))