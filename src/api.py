from abc import ABC, abstractmethod

import requests
from src.vacancy import Vacancy


class GetVacancies(ABC):
    """Абстрактный класс для получения вакансий"""

    @abstractmethod
    def get_vacancies(self, name: str, pages: int):
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
        hh_list = []
        for page in range(pages):
            self.__params['text'] = keyword
            self.__params['page'] = page

            response = requests.get(self.__base_url, params=self.__params)
            response_json = response.json()


            for vac in response_json['items']:
                vac_id = vac.get('id')
                name = vac.get('name', '')
                town = vac.get('area', '').get('name', '')

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

                vacancy = Vacancy(vac_id, name, town, salary_from, salary_to, currency, employment, url)
                hh_list.append(vacancy)
        return hh_list
