import os
from random import*

clear = lambda: os.system('cls')


kindpet = randint(1,10)
if kindpet == 1:
    yourpet = "хомяка"
    petkind = "хомяк"
if kindpet == 2:
    yourpet = "кошку"
    petkind = "кошка"
if kindpet == 3:
    yourpet = "собаку"
    petkind = "собака"
if kindpet == 4:
    yourpet = "попугая"
    petkind = "попугай"
if kindpet == 5:
    yourpet = "черепаху"
    petkind = "черепаха"
if kindpet == 6:
    yourpet = "обезьянку"
    petkind = "обезьянка"
if kindpet == 7:
    yourpet = "Титяна"
    petkind = "Титян"
if kindpet == 8:
    yourpet = "свинку"
    petkind = "свинка"
if kindpet == 9:
    yourpet = "змею"
    petkind = "змея"
if kindpet == 10:
    yourpet = "зайчика"
    petkind = "зайчик"

print("Дарова, перед тобой наша игра про симулятор питомца! И так, начнём.")
print("   /\_/\ ")
print("  ( o.o )")
print("   > ^ < ")
print("")
print(f"Вы отправились в приют для животных и взяли себе домой {yourpet}!")
print("Вам нужно назвать вашего нового друга, придумайте кличку!")
name = str(input("Введите имя вашего питомца: "))
if name == "":
    print ("Тогда вашего питомца будут звать Титян")
    name = "Титян"
print ()




energy = randint(1,5)
food = randint(1,5)
clean = randint(1,5)
fun = randint(1,5)
chores = randint(1,5)
play = True
happy = True


total_step = 0

while play:
    total_step += 1
    print(f"        ➴ {name}({petkind})➶ ")
    print(f" Ход номер {total_step}")
    print(f"Энергия                        {'♥' * energy}{'♡' * (5 - energy)}")
    print(f"Сытость                        {'♥' * food}{'♡' * (5 - food)}")
    print(f"Чистота                        {'♥' * clean}{'♡' * (5 - clean)}")
    print(f"Настроение                     {'♥' * fun}{'♡' * (5 - fun)}")
    print(f"Успеваемость                   {'♥' * chores}{'♡' * (5 - chores)}")
    print()
    
    print ("Сейчас тебе нужно выбрать, что ты хочешь сделать со своим питомцев: ")
    print ("  1. Уложить спать")
    print ("  2. Покормить")
    print ("  3. Помыть")
    print ("  4. Поиграться")
    print ("  5. Заняться домашним заданием")
    print ("  0. Выйти из игры")
    
    choice = int(input("Ваш выбор: "))
    print()
    clear()
    print()
    
    if choice == 1:
        if energy > 2:
            print(f"{name} не хочет спать!")
            fun -= 1
            if fun >= 5:
                fun = 5
        else:
            print(f"{name} с удовольствием поспал!")
            energy += 3
            if food < 2:
                food = 0
            else:
                food -= 2
                clean -= 1

    elif choice == 2:
        if food > 3:
            print(f"{name} не хочет есть!")
            fun -= 1
            energy -= 1
            if fun >= 5:
                fun = 5
        else:
            print(f"{name} с удовольствием поел!")
            print("Nom nom nom...")
            food += 3
            if food >= 5:
                food = 5
            clean -= 1
            if clean >= 5:
                clean = 5
            fun += 1
            if fun >= 5:
                fun = 5
            chores -= 2

    elif choice == 3:
        if clean > 3:
            print(f"{name} не грязный!")
            fun-=1
            if fun >= 5:
                fun = 5
        else:
            print("Вы помыли вашего питомца!")
            clean += 3
            energy -= 2
            if clean >= 5:
                clean = 5
            fun += 1
            if fun >= 5:
                fun = 5
            if chores >= 3:
                chores -= 1
            food -= 1

    elif choice == 4:
        if fun > 3:
            print(f"{name} не хочет играть")
            fun -= 1
            energy -= 1
            if fun >= 5:
                fun = 5
        else:
            print(f"{name} с радостью поиграл!")
            fun += 3
            energy -= 1
            if fun >= 5:
                fun = 5
            clean -= 1
            if clean >= 5:
                clean = 5
            food -= 1
            chores -= 1

    elif choice == 5:
        if chores < 3:
            print(f"{name} сделал все свои дела")
            chores = 5
            food -= 2
            fun -= 1
            if fun >= 5:
                fun = 5
        else:
            print(f"Вы сделали домашнее задание")
            chores += 2
            if chores >= 5:
                chores = 5
            food -= 1
            clean -= 1
            if clean >= 5:
                clean = 5
            fun -= 1
            if fun >= 5:
                fun = 5

    elif choice == 0:
        play = False
    else:
        print ("Увы, нет такого варианта")
        print()
        
    if energy <= -1:
        play = False
        print (f"{name} не спал очень долго и погиб... Rest in peace.")
    if food <= -1:
        play = False
        print (f"{name} погиб с голоду... земля ему пухом..")
    if clean <= -1:
        play = False
        print ("Вашего питомца увезли в питомник...")
    if fun <= -1:
        play = False
        print (f"{name} умер от скуки...")
    if chores <= -1:
        play = False
        print ("Вы начали получать плохие оценки в школе и ваша мама сдала питомца в питомник..")



print ("Спасибо за игру!")
print (f"{name} будет сильно грустить без вас...")
print ("Нажмите ENTER для завершения программы.")