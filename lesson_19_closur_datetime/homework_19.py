## Завдання 1. Фабрика перетворювачів напруги

def make_voltage_converter(factor: float):
    def converter(voltage: float):
        return voltage * factor
    return converter

step_up   = make_voltage_converter(10.0)   # підвищувальний
step_down = make_voltage_converter(0.5)    # знижувальний

print(step_up(22.0))     # 220.0
print(step_down(220.0))  # 110.0
print(step_up(11.0))     # 110.0
print('*' *80)

## Завдання 2. Лічильник електроенергії

def make_electricity_meter(address: str, initial_kwh: float = 0.0):
    current_kwh = initial_kwh

    def add(kwh: float) -> float:
        nonlocal current_kwh
        current_kwh += kwh
        return current_kwh
    
    def reset() -> float:
        nonlocal current_kwh
        current_kwh = initial_kwh
        return current_kwh
    
    def report() -> str:
        return f"Адреса: {address} | Спожито: {current_kwh} кВт·год"

    return add, reset, report

add, reset, report = make_electricity_meter("вул. Франка, 12", 150.0)

print(add(30.5))    # 180.5
print(add(14.0))    # 194.5
print(report())     # Адреса: вул. Франка, 12 | Спожито: 194.5 кВт·год
print(reset())      # 150.0
print(report())     # Адреса: вул. Франка, 12 | Спожито: 150.0 кВт·год
print('*' *80)


## Завдання 3. Диспетчер аварійних подій

def make_dispatcher(station_name: str):
    def dispatch(event: str, callback):
        messege = f"[{station_name}] {event}"
        callback(messege)
    return dispatch

def log_to_console(message: str):
    print(message)

def log_to_file(message: str):
    with open("dispatch_log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

dispatch = make_dispatcher("Підстанція №7 Івано-Франківськ")

dispatch("Перевищення напруги", log_to_console)
# [Підстанція №7 Івано-Франківськ] Перевищення напруги

dispatch("Коротке замикання", log_to_console)
# [Підстанція №7 Івано-Франківськ] Коротке замикання


dispatch("Відновлення живлення", log_to_file)
# (повідомлення записується у dispatch_log.txt)

print('*' *80)


## Завдання 4. Сортування підстанцій
substations = [
    {"name": "Підстанція №3", "region": "Коломия",          "load_kw": 4500},
    {"name": "Підстанція №7", "region": "Івано-Франківськ", "load_kw": 8200},
    {"name": "Підстанція №1", "region": "Калуш",            "load_kw": 3100},
    {"name": "Підстанція №9", "region": "Надвірна",         "load_kw": 6700},
]

def make_sorter(field: str, reverse: bool = False):
    def sorter(substations_list: list) -> list:
        return sorted(substations_list, key=lambda s: s[field], reverse=reverse)
    return sorter

sort_by_load = make_sorter("load_kw", reverse=True)
for s in sort_by_load(substations):
    print(s["name"], s["load_kw"])
print("=" *20)

# Підстанція №7  8200
# Підстанція №9  6700
# Підстанція №3  4500
# Підстанція №1  3100

sort_by_name = make_sorter("name")
for s in sort_by_name(substations):
    print(s["name"])
print('*' *80)

# Підстанція №1
# Підстанція №3
# Підстанція №7
# Підстанція №9


