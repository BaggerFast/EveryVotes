from typing import NamedTuple


class NestedField(NamedTuple):
    url: str
    label: str


class Field(NamedTuple):
    label: str
    nested_fields: tuple


class Navbar:

    def __init__(self, request):
        self.__request = request
        self.__nav = []

    def __static_point(self):
        self.__nav.append(NestedField(url='index', label='Главная'))

    def __auth_point(self):
        if self.__request.user.is_authenticated:
            self.__nav += [
                Field(label='Голосования', nested_fields=(
                    NestedField(url='votings', label='Список'),
                    NestedField(url='create_voting', label='Создать'),
                )),
                Field(label='Профиль', nested_fields=(
                    NestedField(url='logout', label="Выйти"), ))]
            return
        self.__nav += [
            Field(label='Авторизация', nested_fields=(
                NestedField(url='login', label='Войти'),
                NestedField(url='register', label='Зарегистрироваться')))
        ]

    def get(self) -> list:
        """
        Возвращает аттрибуты для меню
        """
        self.__static_point()
        self.__auth_point()
        return self.__nav
