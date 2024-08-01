import json
from src.vacancy import Vacancy, Vacancies
from src.abs_classes import JSONABCSaver


class JSONSaver(Vacancies, JSONABCSaver):
    """
    Запись и чтение json
    """

    def file_writer(self):

        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(self.to_list_dict(), file, indent=4, ensure_ascii=False)

    def file_reader(self):

        with open('vacancies.json', 'r', encoding='UTF-8') as file:
            list_dict = json.load(file)
            self.__all_vacancies = []
            for i in list_dict:
                self.all_vacancies.append(Vacancy.from_dict(i))
