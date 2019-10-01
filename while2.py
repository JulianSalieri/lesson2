katalog = {"Как дела?": "Хорошо", "Что делаешь?": "Программирую", "Как ты?": "Неважно", "Чего так?": "Отстань"}

def ask_user():
    you = 'Чего тебе...\n'
    while True:
        ask_user = input(you)
        if ask_user not in katalog:
            print('Чего? Давай поновой, я такого незнаю ', ask_user)
        else:
            you = 'Чего ещё?\n'
            print(katalog[ask_user])
ask_user()