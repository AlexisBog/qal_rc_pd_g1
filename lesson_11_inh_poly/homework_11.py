class Cossack:
    def __init__(self, name, kyrin, weapons = None, victories = 0):
        self.cossack_name = name
        self.cossack_kyrin = kyrin
        self.cossack_weapons = weapons if weapons is not None else []
        self.cossack_victories = victories
        self.rank = "Козак"

    def update_rank(self):
        if self.cossack_victories >= 7:
            self.rank = "Полковник"
        elif self.cossack_victories >= 3:
            self.rank = "Осавул"
        else:
            self.rank = "Козак"
    

    def arm(self, weapon):
        if weapon not in self.cossack_weapons: 
            self.cossack_weapons.append(weapon)
            return f"{weapon} додано!"
        else:
           return f"{self.cossack_name} вже має"
       
       
    def win_battle(self, enemy):
        self.cossack_victories += 1
        self.update_rank()
        return f"{self.cossack_name} переміг {enemy}! Слава козаку!"

    def __str__(self):
        return(f"Козак: {self.cossack_name} | Курінь: {self.cossack_kyrin} | Перемоги: {self.cossack_victories} | Зброя: {', '.join(self.cossack_weapons)}")


class ZaporozhianSich:
    def __init__(self, name, capacity):
        self.sich_name = name
        self.cossacks_list = []
        self.max_capacity = capacity

    def enlist(self, cossack):
        if len(self.cossacks_list) >= self.max_capacity:
            return "Січ переповнена!"
        for c in self.cossacks_list:
            if c.cossack_name == cossack.cossack_name:
                return f"{cossack.cossack_name} вже на Січі"
        self.cossacks_list.append(cossack)

    def dismiss(self, name_coss):
        for c in self.cossacks_list:
            if c.cossack_name == name_coss:
                self.cossacks_list.remove(c)
                return f"Козака {name_coss} виключено з січі!"
        return f"Козака {name_coss} не знайдено!"

    def call_to_battle(self, enemy):
        if not self.cossacks_list:
            return "Нікому боронити Січ!"
        else:
            return f"Військо Запорозьке виступає проти {enemy}! У поході {len(self.cossacks_list)} козаків!"

    def best_warrior(self):
        if not self.cossacks_list:
            return "Січ порожня!"
        best_cossack = self.cossacks_list[0]
        for i in self.cossacks_list:
            if i.cossack_victories > best_cossack.cossack_victories:
                best_cossack = i
        return best_cossack

    def roster(self):
        if not self.cossacks_list:
            return "На Січі нікого немає"
        names = []
        for v in self.cossacks_list:
            names.append(v.cossack_name)
        return names

    
    def promote_all(self):
        for c in self.cossacks_list:
            c.update_rank()

        

     


sich = ZaporozhianSich("Чортомлицька Січ", capacity=3)

ivan = Cossack("Іван Сірко", "Кальміуський")
petro = Cossack("Петро Сагайдачний", "Канівський")

ivan.win_battle("яничари")
ivan.win_battle("татари")
ivan.win_battle("русня")
petro.win_battle("поляки")

sich.enlist(ivan)
sich.enlist(petro)

print(sich.call_to_battle("турки"))
print(sich.best_warrior())
print(sich.roster())
sich.promote_all()
print(ivan.rank)
print(petro.rank)