import requests
from src.vacancy import Vacancy
from src.abs_classes import GetVacancies


class HH_API(GetVacancies):
    """Класс для получения вакансий с HH.ru"""
    def get_vacancies(self, name: str, pages: int = 5):
        hh_list = []

        for page in range(pages):
            params = {
                'text': name,
                'per_page': '5',
                'page': page
            }

            response = requests.get('https://api.hh.ru/vacancies', params=params)
            response_json = response.json()

            for vac in response_json['items']:
                title = vac['name']
                if not (vac['area'] is None):
                    town = vac['area']['name']
                else:
                    town = None
                if not ((vac['salary'] is None) or (vac['salary']['from'] is None)):
                    salary_from = vac['salary']['from']
                    salary_to = vac['salary']['to']
                else:
                    salary_from = 0
                    salary_to = 0
                employment = vac['employment']['name']
                url = vac['alternate_url']

                vacancy = Vacancy(title, town, salary_from, salary_to, employment, url)
                hh_list.append(vacancy)
        return hh_list