import inspect


def room_1():
    print("Добро пожаловать в подземелье-лабиринт!\nСможете ли вы из него выбраться?")
    choice = input("Выберите направление:\n 1. Восток\n 2. Запад\nВыбор: ")
    if choice == "1":
        room_2()
    elif choice == "2":
        room_6()
    else:
        print("Неправильный ввод, вы погибли...\nШутка! Попробуйте еще раз.")
        room_1()


def room_2():
    print("Вы находитесь в комнате №2.")
    choice = input("Выберите направление:\n 1. Юг\n 2. Запад\nВыбор: ")
    if choice == "1":
        room_3()
    elif choice == "2":
        room_1()
    else:
        print("Неправильный ввод, вы погибли...\nШутка! Попробуйте еще раз.")
        room_2()


def room_3():
    print("Вы находитесь в комнате №3.")
    choice = input("Выберите направление:\n 1. Север\n 2. Восток\n 3. Юг\nВыбор: ")
    if choice == "1":
        room_2()
    elif choice == "2":
        room_4()
    elif choice == "3":
        room_5()
    else:
        print("Неправильный ввод, вы погибли...\nШутка! Попробуйте еще раз.")
        room_3()


def room_4():
    print("Вы находитесь в комнате №4.")
    choice = input("Хмм... Похоже это тупик, придется развернуться:\n 1. Запад\nВыбор: ")
    if choice == "1":
        room_3()
    else:
        print("Неправильный ввод, вы погибли...\nШутка! Попробуйте еще раз.")
        room_4()


def room_5():
    print("Вы находитесь в комнате №5.")
    choice = input("Хмм... Похоже это тупик, придется развернуться:\n 1. Север\nВыбор: ")
    if choice == "1":
        room_3()
    else:
        print("Неправильный ввод, вы погибли...\nШутка! Попробуйте еще раз.")
        room_5()


def room_6():
    print("Вы находитесь в комнате №6.")
    choice = input("Выберите направление:\n 1. Север\n 2. Восток\n 3. Юг\n 4. Запад\nВыбор: ")
    if choice == "1":
        room_7()
    elif choice == "2":
        room_1()
    elif choice == "3":
        room_8()
    elif choice == "4":
        room_15()
    else:
        print("Неправильный ввод, вы погибли...\nШутка! Попробуйте еще раз.")
        room_6()


def room_7():
    print("Вы находитесь в комнате №7.")
    choice = input("Хмм... Похоже это тупик, придется развернуться:\n 1. Юг\nВыбор: ")
    if choice == "1":
        room_6()
    else:
        print("Неправильный ввод, вы погибли...\nШутка! Попробуйте еще раз.")
        room_7()


def room_8():
    print("Вы находитесь в комнате №8.")
    choice = input("Выберите направление:\n 1. Север\n 2. Юг\nВыбор: ")
    if choice == "1":
        room_6()
    elif choice == "2":
        room_9()
    else:
        print("Неправильный ввод, вы погибли...\nШутка! Попробуйте еще раз.")
        room_8()


def room_9():
    print("Вы находитесь в комнате №9.")
    choice = input("Выберите направление:\n 1. Север\n 2. Запад\nВыбор: ")
    if choice == "1":
        room_8()
    elif choice == "2":
        room_10()
    else:
        print("Неправильный ввод, вы погибли...\nШутка! Попробуйте еще раз.")
        room_9()


def room_10():
    print("Вы находитесь в комнате №10.")
    choice = input("Выберите направление:\n 1. Восток\n 2. Запад\nВыбор: ")
    if choice == "1":
        room_9()
    elif choice == "2":
        room_11()
    else:
        print("Неправильный ввод, вы погибли...\nШутка! Попробуйте еще раз.")
        room_10()


def room_11():
    print("Вы находитесь в комнате №11.")
    choice = input("Выберите направление:\n 1. Север\n 2. Восток\n 3. Юг\nВыбор: ")
    if choice == "1":
        room_12()
    elif choice == "2":
        room_10()
    elif choice == "3":
        room_13()
    else:
        print("Неправильный ввод, вы погибли...\nШутка! Попробуйте еще раз.")
        room_11()


def room_12():
    print("Вы находитесь в комнате №12.")
    choice = input("Выберите направление:\n 1. Север\n 2. Юг\n Выбор: ")
    if choice == "1":
        room_14()
    elif choice == "2":
        room_11()
    else:
        print("Неправильный ввод, вы погибли...\nШутка! Попробуйте еще раз.")
        room_12()


def room_13():
    print("Вы находитесь в комнате №13.\nПоздравляем! Вы достигли финальной комнаты!")


def room_14():
    print("Вы находитесь в комнате №14.")
    choice = input("Выберите направление:\n 1. Восток\n 2. Юг\nВыбор: ")
    if choice == "1":
        room_15()
    elif choice == "2":
        room_12()
    else:
        print("Неправильный ввод, вы погибли...\nШутка! Попробуйте еще раз.")
        room_14()


def room_15():
    print("Вы находитесь в комнате №15.")
    choice = input("Выберите направление:\n 1. Восток\n 2. Запад\nВыбор: ")
    if choice == "1":
        room_6()
    elif choice == "2":
        room_14()
    else:
        print("Неправильный ввод, вы погибли...\nШутка! Попробуйте еще раз.")
        room_15()


def count_conditions(func):
    conditions = 0
    source_lines = inspect.getsourcelines(func)[0]
    for line in source_lines:
        if 'if ' in line or 'elif ' in line:
            conditions += 1
    return conditions


# Символьное представление карты лабиринта
MAP = {
    1: "Room 1",
    2: "Room 2",
    3: "Room 3",
    4: "Room 4",
    5: "Room 5",
    6: "Room 6",
    7: "Room 7",
    8: "Room 8",
    9: "Room 9",
    10: "Room 10",
    11: "Room 11",
    12: "Room 12",
    13: "Room 13",
    14: "Room 14",
    15: "Room 15"
}


# Функция для отображения текущей позиции игрока на карте
def display_map(current_room):
    print("Current Map:")
    for room_num, room_name in MAP.items():
        if room_num == current_room:
            print(f"[X] - {room_name}")  # Позиция игрока отмечена как X
        else:
            print("[ ] - {room_name}")


# Пример использования
current_room = 1  # Начальная позиция игрока
display_map(current_room)

count = 0
rooms = [room_1, room_2, room_3, room_4, room_5, room_6, room_7, room_8, room_9, room_10, room_11, room_12, room_13, room_14, room_15]

for room in rooms:
    if count_conditions(room) == 0:
        count += 1

if count == 0:
    print("Тупиков не обнаружено! Приятной игры!")
else:
    print("Обнаружен тупик!")
room_1()
