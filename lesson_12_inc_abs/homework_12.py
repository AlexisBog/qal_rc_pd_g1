from abc import ABC, abstractmethod

class MagicCreature(ABC):
    def __init__(self, name, magic_level, health):
        self.name = name
        self.__alive = True
        self.magic_level = magic_level
        self.health = health
    

    @property
    def magic_level(self):
        return self._magic_level

    @magic_level.setter
    def magic_level(self, value: int):
        if not (1 <= value <= 10):
            raise ValueError("Рівень магії має бути від 1 до 10!")
        self._magic_level = value 

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value: int):
        if not (0 <= value <= 100):
            raise ValueError("Здоров'я має бути від 0 до 100!")

        self.__health = value

        if value == 0:
            self.__alive = False

    @property
    def is_alive(self):
        return self.__alive

    @abstractmethod
    def use_ability(self):
        pass

    @abstractmethod
    def describe(self):
        pass

    def take_damage(self, amount):
        if not self.is_alive:
            return f"{self.name} вже переміг смерть... або ні."
        else:
            self.health = max(0, self.health - amount)

    def __str__(self):
        return f"{self.name} | Магія: {self.magic_level} | HP: {self.health} | Живий: {self.is_alive}"

    @abstractmethod
    def weakness(self):
        pass


class Molfar(MagicCreature):
    def __init__(self, name, magic_level, health, element: str, spells: int):
        super().__init__(name, magic_level, health)
        self.element = element
        self.spells = spells
    @property
    def spells(self):
        return self.__spells

    @spells.setter
    def spells(self, value: int):
        if value < 0:
            raise ValueError("Запас заклинань не може бути від'ємним!")
        self.__spells = value

    def use_ability(self):
        if self.spells > 0:
            self.spells -= 1
            return f"Мольфар {self.name} закликає {self.element}! Залишилось заклинань: {self.spells}"
        else:
            return f"Мольфар {self.name} виснажений — сила стихій покинула його!"

    def describe(self):
        return f"Мольфар {self.name}, повелитель стихії {self.element}. Рівень магії: {self.magic_level}"

    def weakness(self):
        return "протилежна стихія"

class Rusalka(MagicCreature):
    def __init__(self, name, magic_level, health, river: str, charm_power):
        super().__init__(name, magic_level, health)
        self.river = river
        self.charm_power = charm_power

    @property
    def charm_power(self):
        return self.__charm_power

    @charm_power.setter
    def charm_power(self, value):
        if not (1 <= value <= 5):
            raise ValueError("Сила чар має бути від 1 до 5!")
        self.__charm_power = value

    def use_ability(self):
        if self.charm_power == 5:
            return f"Русалка {self.name} з річки {self.river} зачаровує мандрівника! Сила чар: {self.charm_power}! Ніхто не встоїть!"
        else:
            return f"Русалка {self.name} з річки {self.river} зачаровує мандрівника! Сила чар: {self.charm_power}!"

    def describe(self):
        return f"Русалка {self.name}, мешканка річки {self.river}. Сила чар: {self.charm_power}/5"

    def weakness(self):
            return "сонячне світло"

class Perelesnyk(MagicCreature):
    def __init__(self, name, magic_level, health, speed: int, form = "вогняна куля"):
        super().__init__(name, magic_level, health)
        self.speed = speed
        self.form = form

    @property
    def speed(self):
            return self.__speed

    @speed.setter
    def speed(self, value):
        if not (1 <= value <= 100):
            raise ValueError("Швидкість повинна бути від 1 до 100")
        self.__speed = value

    def change_form(self):
        if self.form == "вогняна куля":
            self.form = "людська"
        else:
            self.form = "вогняна куля"
        return f"Перелесник перетворився на {self.form}!"

    def use_ability(self):
        result = f"Перелесник {self.name} мчить крізь ніч зі швидкістю {self.speed}! Форма: {self.form}"
        if self.form == "людська":
            result += " Ніхто не здогадається..."
        return result

    def describe(self):
        return f"Перелесник {self.name}. Швидкість: {self.speed}. Зараз у формі: {self.form}"

    def weakness(self):
        return "священна вода"

class EnchantedForest():
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.__creatures = []
        
    @property
    def creatures_count(self):
        return len([x for x in self.__creatures if x.is_alive])

    def add_creature(self, creature: MagicCreature):
        if len(self.__creatures) >= self.capacity:
            return f"Зачарований ліс {self.name} переповнений!"
        if not creature.is_alive:
            return f"Мертві істоти не можуть оселитись у лісі!"
        if any(c.name == creature.name for c in self.__creatures):
            return f"{creature.name} вже мешкає у цьому лісі!"
        self.__creatures.append(creature)
        return f"{creature.name} оселився у лісі {self.name}!"

    def remove_creature(self, name):
        for creature in self.__creatures:
            if creature.name == name:
                self.__creatures.remove(creature)
                return f"Істоту {name} видалено з лісу."
        return f"Істоту {name} не знайдено у лісі!"

    def most_powerful(self):
        if not self.__creatures:
            return "Ліс порожній — нема кому чаклувати!"
        return max(self.__creatures, key = lambda c: c.magic_level)

    def attack_intruder(self, intruder_name):
        attacks = [
            f"{c.use_ability()} (Слабкість: {c.weakness()})"
            for c in self.__creatures if c.is_alive
            ]
        
        if not attacks:
            return f"Ліс беззахисний перед {intruder_name}!"
        
        return attacks

    def census(self):
        if not self.__creatures:
            return "Ліс порожній"
        
        return [c.describe() for c in self.__creatures]

    def heal_all(self, amount):
        alive_creatures = [c for c in self.__creatures if c.is_alive]
    
        if not alive_creatures:
            return "У лісі немає живих істот для лікування!"
        for c in alive_creatures:
            c.health = min(100, c.health + amount)
        return f"Здоров'я всіх живих істот відновлено на {amount} HP!"

