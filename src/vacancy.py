from abc import ABC, abstractmethod


class BaseVacancy(ABC):

    """ Базовый класс для вакансии"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass


class BaseVacancies(ABC):
    """ Базовый класс для списка вакансий """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_vacancy(self, new_vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vac_id: int):
        pass


class Vacancy(BaseVacancy):
    """ Класс для работы с вакансиями """

    def __init__(self, vac_id: int, name: str, town: str, salary_from: float, salary_to: float, currency: str,
                 employment: str, url: str):
        self.id = vac_id
        self.name: str = name
        self.town: str = town
        self.salary_from: float = salary_from
        self.salary_to: float = salary_to
        self.currency = currency
        self.employment: str = employment
        self.url: str = url

    def __str__(self):
        return f'id: {self.id}\n' \
               f'Название вакансии: {self.name}\n' \
               f'Город: {self.town}\n' \
               f'Зарплата\nот: {self.salary_from} {self.currency}\nдо: {self.salary_to} {self.currency}\n' \
               f'Тип занятости: {self.employment}\n' \
               f'Ссылка на вакансию: {self.url}\n'

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией!")
        return (self.salary_from, self.salary_to) == (other.salary_from, other.salary_to)

    def __ne__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией!")
        return (self.salary_from, self.salary_to) != (other.salary_from, other.salary_to)

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией!")
        return (self.salary_from, self.salary_to) < (other.salary_from, other.salary_to)

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией!")
        return (self.salary_from, self.salary_to) > (other.salary_from, other.salary_to)

    def to_dict(self):
        """
        Возвращает вакансию в виде словаря
        """
        return self.__dict__

    @staticmethod
    def to_list(vacancy_dict):
        """Возвращает вакансию в виде списка"""
        return Vacancy(
            vacancy_dict['id'],
            vacancy_dict['name'],
            vacancy_dict['town'],
            vacancy_dict['salary_from'],
            vacancy_dict['salary_to'],
            vacancy_dict['currency'],
            vacancy_dict['employment'],
            vacancy_dict['url']
        )


class Vacancies(BaseVacancies):
    """ Класс для работы со списком вакансий"""

    def __init__(self):
        self.__all_vacancies = []

    def add_vacancy(self, new_vacancy):
        self.__all_vacancies += new_vacancy

    def delete_vacancy(self, vac_id: int):
        for vac in self.__all_vacancies:
            if vac['id'] == vac_id:
                self.__all_vacancies.remove(vac)

    def sort_vacancies_by_salary(self):
        self.__all_vacancies.sort(reverse=True)

    @property
    def all_vacancies(self):
        return self.__all_vacancies

    def to_list_dict(self):
        my_list = []
        for vac in self.__all_vacancies:
            my_list.append(vac.to_dict())
        return my_list
