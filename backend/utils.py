from dataclasses import dataclass
from typing import NamedTuple
from django.urls import reverse_lazy


@dataclass
class NestedField:
    url: str
    label: str
    active: bool = False


class Field(NamedTuple):
    label: str
    nested_fields: tuple


class Navbar:

    def __init__(self, request):
        self.__request = request
        self.__nav = []

    def __off_current(self):
        for menu_item in self.__nav:
            if isinstance(menu_item, NestedField):
                menu_item.active = self.__request.path != reverse_lazy(menu_item.url)
                continue
            for field in menu_item.nested_fields:
                field.active = self.__request.path != reverse_lazy(field.url)

    def __static_point(self):
        self.__nav += [
            NestedField(url='index', label='Главная')
        ]

    def __auth_point(self):
        if self.__request.user.is_authenticated:
            self.__nav += [
                Field(label='Голосования', nested_fields=(
                    NestedField(url='votings', label='Список'),
                    NestedField(url='create_voting', label='Создать'),
                )),
                Field(label='Профиль', nested_fields=(
                    NestedField(url='logout', label="Выйти"), ))]
        else:
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
        self.__off_current()
        return self.__nav
