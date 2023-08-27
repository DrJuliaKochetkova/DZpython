def redact_contact(phonebook, search_key):
    search_key = search_key.capitalize()
    for i in range(len(phonebook)):
        if search_key in phonebook[i].values():
            phonebook[i] = search_key


def del_contacts(phonebook, search_key):
    search_key = search_key.capitalize()
    for i in range(len(phonebook) -1, -1, -1):
        if search_key in phonebook[i].values():
            del phonebook[i]
            return


def load_file(filename):
    phonebook = []
    try:
        with open(filename, 'r') as file:
            for contact in file:
                last_name, first_name, middle_name, phone_number = contact.split(',')
                phonebook.append({
                    'last_name': last_name,
                    'first_name': first_name,
                    'middle_name': middle_name,
                    'phone_number': phone_number
                })
            print('Данные успешно загружены')
    except FileNotFoundError:
        print('Файл не найден')
    return phonebook


def search_contacts(phonebook, search_key):
    results = []
    for contact in phonebook:
        if (search_key.lower() in contact['last_name'].lower() or search_key.lower() in contact['first_name'].lower()):
            results.append(contact)
    return results



def views_contacts(phonebook):
    for index, contact in enumerate(phonebook, start=1):
        print(f"{index}. {contact['last_name']}, {contact['first_name']}, {contact['middle_name']}, {contact['phone_number']}\n")


def save_to_file(filename, phonebook):
    with open(filename, 'w') as file:
        for contact in phonebook:
            file.write(f"{contact['last_name']}, {contact['first_name']}, {contact['middle_name']}, {contact['phone_number']}\n")
    print('Данные сохранены в файле')

def add_contact(phonebook, last_name, first_name, middle_name, phone_number):
    contact = {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone_number': phone_number
    }
    phonebook.append(contact)
    print('Контакт добавлен')


def main():
    phonebook = []
    filename = 'contacts.txt'

    while True:
        print("1. Добавить контакт")
        print("2. Сохранить файл")
        print("3. Вывести все контакты")
        print("4. Поиск по имени/фамилии")
        print("5. Загрузить из файла")
        print("6. Удалить контакт")
        print("7. Сменить контакт")
        print("8. Выйти")

        choice = input('Выберите действие: ')
        if choice == '1':
            last_name = input('Фамилия: ')
            first_name = input('Имя: ')
            middle_name = input('Отчество: ')
            phone_number = input('Номер телефона: ')
            add_contact(phonebook, last_name, first_name, middle_name, phone_number)
        elif choice == '2':
            save_to_file(filename, phonebook)
        elif choice == '3':
            views_contacts(phonebook)
        elif choice == '4':
            search_key = input("Введите имя или фамилию для поиска: ")
            results = search_contacts(phonebook, search_key)
            if (results):
                print('Найдены контакты: ')
                print(results)
            else:
                print('Контактов по вашему запросу нет!')
        elif choice == '5':
            phonebook = load_file(filename)
        elif choice == '6':
            search_key = input("Введите имя или фамилию для поиска: ")
            del_contacts(phonebook, search_key)
        elif choice == '7':
            search_key = input("Введите имя или фамилию для поиска: ")
            redact_contact(phonebook, search_key)
        elif choice == '8':
            break
        else:
            print('Некорректный выбор. Попробуйте снова')




if __name__ == "__main__":
    main()

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
потренироваться если нужно кому
            
phonebook = [
    {
        'last_name': 'Dmitriev',
        'first_name': 'Dmitriy'
    },
    {
        'last_name': 'Maximov',
        'first_name': 'Maxim'
    },
{
        'last_name': 'Genadiev',
        'first_name': 'Gennadiy'
    }
]
search_key = 'd'
for contact in phonebook:
    if (search_key.lower() in contact['last_name'].lower() or search_key.lower() in contact['first_name'].lower()):
        print('Такой есть')
    else:
        print('Такого нет')
            
            
            
            
            
            
            
            




if __name__ == "__main__":
    main()