from collections import Counter
from .minerals import MINERAL_CATALOG, get_mineral
from .observations import get_observations

def summary():
    obs_list = get_observations()
    total_minerals = len(MINERAL_CATALOG)
    total_obs = len(obs_list)

    if not obs_list:
        most_active_str = "Спостережень ще немає"
    else:
        researchers = [entry.get("researcher") for entry in obs_list if "researcher" in entry]
        counts = Counter(researchers)
        top_researcher, count = counts.most_common(1)[0]

        if count == 1:
            record_word = "запис"
        elif 2 <= count <= 4:
            record_word = "записи"
        else:
            record_word = "записів"

        most_active_str = f"{top_researcher} ({count} {record_word})"

    return (
        f"=== Загальне зведення ===\n"
        f"Мінералів у каталозі: {total_minerals}\n"
        f"Спостережень у журналі: {total_obs}\n"
        f"Найактивніший дослідник: {most_active_str}"
    )

def mineral_report(name):
    mineral = get_mineral(name)
    if not mineral:
        return f"Мінерал '{name}' відсутній у каталозі"

    info = (
        f"=== Звіт: {name} ===\n"
        f"Формула: {mineral['formula']} | "
        f"Твердість: {mineral['hardness']} | "
        f"Походження: {mineral['origin']} | "
        f"Відкрито: {mineral['discovered']}\n"
        f"Спостереження:"
    )

    observations = get_observations(name)
    if not observations:
        info += "\n  [немає записів]"
    else:
        for obs in observations:
            info += f"\n  [{obs['date']}] {obs['researcher']}: {obs['note']}"
            
    return info