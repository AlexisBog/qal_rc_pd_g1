adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# УВАГА! Перезаписуйте вміст змінної adwentures_of_tom_sawer у завданнях 01-03

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n"," ")

# task 02 ==
""" Замініть .... на пробіл

"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("...."," ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer.split())

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print(adwentures_of_tom_sawer.count("h"))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру напр, .count("A") і їх сумму
"""
cap_letters = (adwentures_of_tom_sawer.count("A") + adwentures_of_tom_sawer.count("B") + adwentures_of_tom_sawer.count("C")
                + adwentures_of_tom_sawer.count("D") + adwentures_of_tom_sawer.count("E") + adwentures_of_tom_sawer.count("F") 
                + adwentures_of_tom_sawer.count("G") + adwentures_of_tom_sawer.count("H") + adwentures_of_tom_sawer.count("I") 
                + adwentures_of_tom_sawer.count("J") + adwentures_of_tom_sawer.count("K") + adwentures_of_tom_sawer.count("L") 
                + adwentures_of_tom_sawer.count("M") + adwentures_of_tom_sawer.count("N") + adwentures_of_tom_sawer.count("O") 
                + adwentures_of_tom_sawer.count("P") + adwentures_of_tom_sawer.count("Q") + adwentures_of_tom_sawer.count("R") 
                + adwentures_of_tom_sawer.count("S") + adwentures_of_tom_sawer.count("T") + adwentures_of_tom_sawer.count("U") 
                + adwentures_of_tom_sawer.count("V") + adwentures_of_tom_sawer.count("W") + adwentures_of_tom_sawer.count("X") 
                + adwentures_of_tom_sawer.count("Y") + adwentures_of_tom_sawer.count("Z"))
print(cap_letters)

'''Інший метод'''
count = 0

for word in adwentures_of_tom_sawer.split():
    for letter in word:
        if letter.isalpha():
            if letter.isupper():
                count +=1
            break

print(count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
tom_first = adwentures_of_tom_sawer.find("Tom")
tom_second = adwentures_of_tom_sawer.find("Tom", tom_first + 1)
print(tom_second)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.replace(".", "\n")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
sentences = adwentures_of_tom_sawer_sentences.strip().split("\n")
sentences[3] = sentences[3].lower()

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for line in sentences:
    if line.strip().startswith("By the time"):
        print('Починається з "By the time"')
else:
    print('Нічого не знайдено')
# У попередньому завданні ми змінили всі букви на маленькі тому речення з таким початком немає

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

print(len(sentences[-1].split()))