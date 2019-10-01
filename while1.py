def ask_user(question):
    while question != 'Хорошо':
        print('Неправильно,давай сначало')
        question=input('Как дела? ')
    else:
        print('Вот это верно')

ask_user(input('Как дела? '))