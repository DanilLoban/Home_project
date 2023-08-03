import json
from datetime import datetime

# Функция для чтения заметок из файла
def read_notes():
    try:
        with open('home_memo.json', 'r') as file:
            notes = json.load(file)
        return notes
    except FileNotFoundError:
        return []

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open('home_memo.json', 'w') as file:
        json.dump(notes, file)

# Функция для добавления заметки
def add_note():
    notes = read_notes()
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {'id': len(notes)+1, 'title': title, 'body': body, 'timestamp': timestamp}
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена.")

# Функция для показа всех заметок
def show_notes():
    notes = read_notes()
    if len(notes) == 0:
        print("У вас нет заметок.")
    else:
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Текст: {note['body']}, Дата/время: {note['timestamp']}")

# Функция для редактирования заметки
def edit_note():
    notes = read_notes()
    note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
    for note in notes:
        if note['id'] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note['title'] = title
            note['body'] = body
            note['timestamp'] = timestamp
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

# Функция для удаления заметки
def delete_note():
    notes = read_notes()
    note_id = int(input("Введите ID заметки, которую хотите удалить: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")

# Интерфейс командного интерпретатора
while True:
    print("\nВыберите действие:")
    print("1 - Добавить заметку")
    print("2 - Показать все заметки")
    print("3 - Редактировать заметку")
    print("4 - Удалить заметку")
    print("5 - Выход")
    choice = input("Введите номер действия: ")

    if choice == '1':
        add_note()
    elif choice == '2':
        show_notes()
    elif choice == '3':
        edit_note()
    elif choice == '4':
        delete_note()
    elif choice == '5':
        break
    else:
        print("Неправильный выбор. Попробуйте снова.")