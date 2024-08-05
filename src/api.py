from abc import ABC, abstractmethod

import requests
from src.vacancy import Vacancy, Vacancies


class GetVacancies(ABC):
    """Абстрактный класс для получения вакансий"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, pages: int):
        pass


class HH_Api(GetVacancies):
    """Класс для получения вакансий с HH.ru"""

    def __init__(self):
        self.__base_url = 'https://api.hh.ru/vacancies'
        self.__params = {
            'text': '',
            'per_page': '100',
            'page': 0,
            'area': 113
        }

    def get_vacancies(self, keyword: str, pages: int):
        hh_list = Vacancies()
        for page in range(pages):
            self.__params['text'] = keyword
            self.__params['page'] = page

            response = requests.get(self.__base_url, params=self.__params)
            response_json = response.json()

            for vac in response_json['items']:
                vac_id = vac.get('id')
                name = vac.get('name', '')
                city = vac.get('area', '').get('name', '')

                if vac['salary']:
                    salary = vac['salary']
                    currency = salary.get('currency', '')

                    if salary['from']:
                        salary_from = salary['from']
                    else:
                        salary_from = 0
                    if salary['to']:
                        salary_to = salary['to']
                    else:
                        salary_to = 0

                else:
                    salary_from = 0
                    salary_to = 0

                employment = vac['employment']['name']
                url = vac['alternate_url']

                new_vac = Vacancy(vac_id, name, city, salary_from, salary_to, currency, employment, url)
                hh_list.add_vacancy(new_vacancy=new_vac)
        return hh_list
