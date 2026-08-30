class ChainOfOrders:

    def __init__(self, names):
        self.names = names
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.names or self.index >= len(self.names):
            raise StopIteration

        current_name = self.names[self.index]

        if self.index == len(self.names) - 1:
            self.index += 1
            return f"{current_name} каже: теля прив'язав!"      

        next_name = self.names[self.index + 1]
        self.index += 1
        return f"{current_name} каже {next_name}: передай далі!"

chain = ChainOfOrders(["Дід", "Батько", "Михайлик", "Василько"])
for message in chain:
    print(message)
    

    def village_rumor(start_message, people):
        if not people:
            return

        history = []

        for i, person in enumerate(people):
            if i == 0:
                yield f'{person} каже: "{start_message}"'
                history.append(f"(переказала {person})")
            elif i == len(people) - 1:
                history_str = " ".join(history)
                yield f'{person} переказує: "{start_message} {history_str} (і всі дізналися!)"'
            else:
                history_str = " ".join(history)            
                yield f'{person} переказує: "{start_message} {history_str}"'
                history.append(f"(переказала {person})")

for version in village_rumor("Теля втекло!", ["Горпина", "Параска", "Явдоха", "Оксана"]):
    print(version)


events = [
    "Михайлик передав доручення",
    "Василько відмовився",
    "Грицько передав доручення",
    "Оленка прив'язала теля",
    "Данилко передав доручення",
]

count = sum(1 for event in events if "передав доручення" in event)
print(f"Доручення передавали {count} рази")

import itertools

def toloka_queue(workers):
    if not workers:
        return
    for worker in itertools.cycle(workers):
        yield f"Черга: {worker}"

queue = toloka_queue(["Іван", "Марія", "Степан"])
for turn in itertools.islice(queue, 7):
    print(turn)


def find_calf(log):
    for line in log:
        if "прив'язав" in line or "прив'язала" in line:
            yield line
            return

journal = [
    "Михайлик отримав доручення",
    "Михайлик передав Василькові",
    "Василько загрався",
    "Василько передав Оленці",
    "Оленка прив'язала теля біля хліва",
    "Оленка пішла додому",
    "Дід заспокоївся",
]
result = next(find_calf(journal))
print(result)

