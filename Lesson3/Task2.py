def profile(name: str, surname: str, birth_year: str, city: str, email: str, phone: str):
    """
    Функция принимает данные о пользователе и выводит их в одну строку

    :param name: str
    :param surname: str
    :param birth_year: str
    :param city: str
    :param email: str
    :param phone: str
    :return:
    """

    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {birth_year}, Город проживания: {city}, Электронная почта: {email}, Телефон: {phone}')

profile(
    name=input('Имя: '),
    surname=input('Фамилия: '),
    birth_year=input('Год рождения: '),
    city=input('Город проживания:'),
    email=input('email: '),
    phone=input('Телефон: ')
)

