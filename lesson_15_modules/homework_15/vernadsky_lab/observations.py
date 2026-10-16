import datetime
from .minerals import get_mineral

_journal = []

def record(researcher, mineral_name, note):

    mineral = get_mineral(mineral_name)

    if not mineral:
        return f"Мінерал '{mineral_name}' не зареєстровано. Спочатку додайте його до каталогу"

    entry = {
        "researcher": researcher,
        "mineral": mineral_name,
        "note": note,
        "date": datetime.date.today()
    }
    _journal.append(entry)
    return f"Спостереження записано: {researcher} → {mineral_name}"

def get_observations(mineral_name=None):
    if not mineral_name:
        return _journal.copy()

    return[entry for entry in _journal if entry["mineral"] == mineral_name]