class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, vac_id: int, name: str, town: str, salary_from: float, salary_to: float, currency: str,
                 employment: str, url: str):
        self.vac_id = vac_id
        self.name: str = name
        self.town: str = town
        self.salary_from: float = salary_from
        self.salary_to: float = salary_to
        self.currency = currency
        self.employment: str = employment
        self.url: str = url

    def __str__(self):
        return f'ID: {self.vac_id}\n' \
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
        # return {
        #     'id': self.vac_id,
        #     'name': self.name,
        #     'town': self.town,
        #     'salary_from': self.salary_from,
        #     'salary_to': self.salary_to,
        #     'currency': self.currency,
        #     'employment': self.employment,
        #     'url': self.url
        # }
        return self.__dict__

    @staticmethod
    def from_dict(vacancy_dict):
        """Возвращает вакансию в виде списка"""
        return Vacancy(
            vacancy_dict['vac_id'],
            vacancy_dict['name'],
            vacancy_dict['town'],
            vacancy_dict['salary_from'],
            vacancy_dict['salary_to'],
            vacancy_dict['employment'],
            vacancy_dict['url']
        )


class Vacancies:
    """Обработка списка вакансий"""

    def __init__(self):
        self.__all_vacancies = []

    def add_vacancies(self, new_vacancies):
        self.__all_vacancies += new_vacancies

    def delete_vacancies(self, old_vacancies):
        for i in old_vacancies:
            self.__all_vacancies.remove(i)

    def sort_vacancies_by_salary(self):
        self.__all_vacancies.sort(reverse=True)

    @property
    def all_vacancies(self):
        return self.__all_vacancies

    def to_list_dict(self):
        a = []
        for i in self.__all_vacancies:
            a.append(i.to_dict())
        return a
