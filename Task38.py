# Создаем пустой словарь для хранения записей телефонного справочника
phonebook = {}

# Функция для добавления записи в телефонный справочник
def add_contact(name, phone):
    phonebook[name] = phone
    print("Запись успешно добавлена!")

# Функция для изменения записи в телефонном справочнике
def edit_contact(name, new_phone):
    if name in phonebook:
        phonebook[name] = new_phone
        print("Запись успешно изменена!")
    else:
        print("Такой записи не существует!")

# Функция для удаления записи из телефонного справочника
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print("Запись успешно удалена!")
    else:
        print("Такой записи не существует!")

# Функция для вывода всех записей в телефонном справочнике
def print_phonebook():
    print("Телефонный справочник:")
    for name, phone in phonebook.items():
        print(name + ": " + phone)

# Добавляем несколько записей в телефонный справочник
add_contact("Иванов Иван", "123-45-67")
add_contact("Петров Петр", "987-65-43")
add_contact("Сидоров Сидор", "555-55-55")

# Выводим все записи в телефонном справочнике
print_phonebook()

# Изменяем запись в телефонном справочнике
edit_contact("Иванов Иван", "111-11-11")

# Выводим все записи в телефонном справочнике
print_phonebook()

# Удаляем запись из телефонного справочника
delete_contact("Петров Петр")

# Выводим все записи в телефонном справочнике
print_phonebook()
