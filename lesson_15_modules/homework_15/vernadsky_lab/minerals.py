MINERAL_CATALOG = {
    "Алмаз": {
        "formula": "C",
        "hardness": 10,
        "origin": "Якутія",
        "discovered": 1800
    },
    "Топаз": {
        "formula": "Al2SiO4(F,OH)2",
        "hardness": 8,
        "origin": "Волинь",
        "discovered": 1820
    },
    "Корунд": {
        "formula": "Al2O3",
        "hardness": 9,
        "origin": "Урал",
        "discovered": 1815
    },
    "Гіпс": {
        "formula": "CaSO4·2H2O",
        "hardness": 2,
        "origin": "Поділля",
        "discovered": 1780
    },
    "Тальк": {
        "formula": "Mg3Si4O10(OH)2",
        "hardness": 1,
        "origin": "Кривий Ріг",
        "discovered": 1835
    }
}

def get_mineral(name):
    return MINERAL_CATALOG.get(name)

def register_mineral(name, formula, hardness, origin, discovered):
    if name in MINERAL_CATALOG:
        return f"Мінерал '{name}' вже зареєстровано в каталозі"

    if not (1 <= hardness <= 10):
        return "Некоректна твердість: має бути від 1 до 10"

    MINERAL_CATALOG[name] = {
        "formula": formula,
        "hardness": hardness,
        "origin": origin,
        "discovered": discovered,
    }
    return f"Мінерал '{name}' додано до каталогу"
