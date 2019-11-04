def schet():
    schet = 0
    history = {}

    def schet_pop(schet, popolnenie):
        schet += int(popolnenie)
        return schet

    def sum_pok(schet, history, money):
        money = int(money)
        if money <= schet:
            schet -= money
            history[input('Введите название товара:')] = money
        else:
            print('Недостаточно средств')
        return schet, history

    def sum_obsh(history):
        for i, p in history.items():
            print(f'{i} --> {p}')

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            schet = schet_pop(schet, input('Введите сумму, на которую хотите пополнить счёт:'))
            pass
        elif choice == '2':
            schet, history = sum_pok(schet, history, input('Введите сумму, которую планируете потратить на покупки:'))
            pass
        elif choice == '3':
            sum_obsh(history)
            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
