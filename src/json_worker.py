import json
import os
from abc import ABC, abstractmethod

from config import DATA_DIR
from src.vacancy import Vacancy, Vacancies


class BaseSaver(ABC):
    """
    Базовый класс для записи и чтения полученных вакансий в файл json
    """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def write_to_file(self, vacs: Vacancies):
        pass

    @abstractmethod
    def read_from_file(self):
        pass


class JSONSaver(Vacancies, BaseSaver):
    """
    Запись и чтение json - файла
    """

    def __init__(self, filename: str):
        super().__init__()
        self.__filename = filename
        self.__check_path_or_create()
        self.__filepath = os.path.join(DATA_DIR, self.__filename)

    @staticmethod
    def __check_path_or_create():
        if not os.path.isdir(DATA_DIR):
            os.makedirs(DATA_DIR)

    def write_to_file(self, vacs: Vacancies):
        with open(self.__filepath, 'w', encoding='utf-8') as file:
            if isinstance(vacs, Vacancies):
                json.dump(vacs.to_list_dict(), file, indent=4, ensure_ascii=False)
            elif isinstance(vacs, list):
                json.dump(vacs, file, indent=4, ensure_ascii=False)

    def read_from_file(self):
        with open(self.__filepath, 'r', encoding='UTF-8') as file:
            list_dict = json.load(file)
            self.__all_vacancies = []
            for i in list_dict:
                self.all_vacancies.append(Vacancy.to_list(i))
