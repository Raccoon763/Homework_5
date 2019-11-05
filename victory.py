def victory():
    # Брюс Уиллис = 1955
    # Арнольд Шварцнеггер = 1947
    # Сильвестр Сталлоне = 1946
    # Чак Норрис = 1940
    # Жан-Клод Ван Дамм = 1960

    brain = 0
    stupid = 0
    desire = 'yes'
    while desire == 'yes':
        question_1 = int(input('Введите год рождения Брюса Уиллиса:'))
        if question_1 == 1955:
            brain += 1
        else:
            stupid += 1
        question_2 = int(input('Введите год рождения Арнольда Шварцнеггера:'))
        if question_2 == 1947:
            brain += 1
        else:
            stupid += 1
        question_3 = int(input('Введите год рождения Сильвестра Сталлоне:'))
        if question_3 == 1946:
            brain += 1
        else:
            stupid += 1
        question_4 = int(input('Введите год рождения Чака Норриса:'))
        if question_4 == 1940:
            brain += 1
        else:
            stupid += 1
        question_5 = int(input('Введите год рождения Жан-Клода Ван Дамма:'))
        if question_5 == 1960:
            brain += 1
        else:
            stupid += 1
        procentP = int(brain * 100 / 5)
        procentN = int(stupid * 100 / 5)
        print('Количество правильных ответов:', brain)
        print('Количество неправильных ответов:', stupid)
        print('Процент правильных ответов:', procentP)
        print('Процент неправильных ответов:', procentN)
        desire = str(input('Хотите начать заново? yes/no:'))