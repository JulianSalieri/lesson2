years_old = int(input('Введите ваш возраст от 3 до 65 месье:'))


def practice(years_old):
    if 3 <= years_old <= 6:
        return 'Вы учитесь в детском саду'

    elif 7 <= years_old <= 18:
        return 'Вы учитесь в школе'

    elif 18 <= years_old <= 65:
        return 'Вы учитесь в ВУЗЕ или РАБОТАЕТ'

    else:
        return 'Вам меньше трех или вам больше 65 , идите от сюда'

print(practice(years_old))


def string_comparison (name, number):
	if type(name, number) is str:
		if name == number:
			return 1

		if name <> number and len(name) > len(number):
			return 2

		if name <> number and number == 'learn' :
			return 3		
    else:
    	return 0
print(string_comparison(Да, Да))