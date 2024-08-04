from src.api import HH_Api
from src.json_worker import JSONSaver


def user_interaction():
    print('Здравствуйте! \nЭта программа по поиску и сравнению вакансий на HeadHunter. \n')
    keyword = input('Напишите название профессии: \n').strip()
    hh_api = HH_Api()
    pages = int(input('Сколько вывести страниц? \n'))
    from_hh = hh_api.get_vacancies(keyword, pages)
    print('*' * 50)
    print('Список вакансий с сайта "HeadHunter": \n')
    print('-' * 50)
    for i in from_hh:
        print(i)
    print('Записать отсортированные по зарплате данные в JSON файл? \n')
    user_answer = input('Да\Нет \n').lower().strip()
    if user_answer != 'да':
        print('Спасибо за использование программы!')
    else:
        jsonfile = JSONSaver('vacancies.json')
        jsonfile.add_vacancies(from_hh)
        jsonfile.sort_vacancies_by_salary()
        jsonfile.file_write()
        return jsonfile
