from tkinter import Tk, Canvas

# Конфигурация окна
root = tk.Tk()
root.title("The Binding of Isaac Map")
root.geometry("800x600")  # Размер окна

# Карта комнат (для примера)
room_map = {
    "Room 1": (100, 100),
    "Room 2": (300, 100),
    "Room 3": (500, 100),
    "Room 4": (200, 300),
    "Room 5": (400, 300)
}

# Соединения между комнатами
room_connections = [("Room 1", "Room 2"), ("Room 2", "Room 3"), ("Room 2", "Room 4"), ("Room 3", "Room 5")]

# Отобразить комнаты на карте
for room, pos in room_map.items():
    label = tk.Label(root, text=room, bg="lightgray")
    label.place(x=pos[0], y=pos[1], width=100, height=50)

# Отобразить соединения между комнатами
for connection in room_connections:
    room1_pos = room_map[connection[0]]
    room2_pos = room_map[connection[1]]
    root.canvas.create_line(room1_pos[0] + 50, room1_pos[1] + 25, room2_pos[0] + 50, room2_pos[1] + 25, fill="black", width=2)

# Позиция игрока (начальная позиция Room 1)
player_position = (100, 100)
player_label = tk.Label(root, text="Игрок", bg="red")
player_label.place(x=player_position[0], y=player_position[1], width=50, height=50)


# Функция для перемещения игрока
def move_player(room):
    global player_position
    player_position = room_map[room]
    player_label.place(x=player_position[0], y=player_position[1], width=50, height=50)


# Кнопки для перемещения между комнатами
btn_room1 = tk.Button(root, text="Room 1", command=lambda: move_player("Room 1"))
btn_room1.place(x=10, y=10, width=80, height=30)

btn_room2 = tk.Button(root, text="Room 2", command=lambda: move_player("Room 2"))
btn_room2.place(x=10, y=50, width=80, height=30)

# Добавьте аналогичные кнопки и функции для других комнат

root.mainloop()
