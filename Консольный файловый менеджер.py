import first
import victory
import schet

print('Взгляните на меню:')
print('1. Cоздать папку')
print('2. Удалить файл/папку')
print('3. Копировать файл/папку')
print('4. Просмотр содержимого рабочей директории')
print('5. Посмотреть только папки')
print('6. Посмотреть только файлы')
print('7. Просмотр информации об операционной системе')
print('8. Создатель программы')
print('9. Играть в викторину')
print('10. Мой банковский счет')
print('11. Сохранить содержимое рабочей директории в файл')
print('12. Выход')

while True:
    choice = input('Выберите один из пунктов меню:')
    if choice == '1':
        first.create_dir()

    elif choice == '2':
        first.remove_dir()

    elif choice == '3':
        first.copy_dir()

    elif choice == '4':
        first.show_dir()

    elif choice == '5':
        first.show_dir_pap()

    elif choice == '6':
        first.show_dir_file()

    elif choice == '7':
        first.os_inf()

    elif choice == '8':
        first.me()

    elif choice == '9':
        victory.victory()

    elif choice == '10':
        schet.schet()

    elif choice == '11':
        first.create_file()

    elif choice == '12':
        break