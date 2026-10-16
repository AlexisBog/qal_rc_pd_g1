from .minerals import MINERAL_CATALOG


def hardest_minerals(n=3):
    sorted_minerals = sorted(
        MINERAL_CATALOG.items(),
        key=lambda item: item[1]["hardness"],
        reverse=True
    )
    return [name for name, _ in sorted_minerals[:n]]


def search_by_origin(origin_keyword):
    keyword = origin_keyword.lower()
    return [
        name for name, data in MINERAL_CATALOG.items()
        if keyword in data["origin"].lower()
    ]