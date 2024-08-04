import json
import os
from abc import ABC, abstractmethod

from config import DATA_DIR
from src.vacancy import Vacancy, Vacancies


class BaseSaver(ABC):
    """
    Базовый класс для записи и чтения полученных вакансий в файл json
    """

    def __init__(self):
        pass

    @abstractmethod
    def file_write(self):
        pass

    @abstractmethod
    def file_read(self):
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

    def file_write(self):
        with open(self.__filepath, 'w', encoding='utf-8') as file:
            json.dump(self.to_list_dict(), file, indent=4, ensure_ascii=False)

    def file_read(self):
        with open(self.__filepath, 'r', encoding='UTF-8') as file:
            list_dict = json.load(file)
            self.__all_vacancies = []
            for i in list_dict:
                self.all_vacancies.append(Vacancy.from_dict(i))
