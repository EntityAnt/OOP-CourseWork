from src.api import HH_Api
from src.json_worker import JSONSaver
from src.vacancy import Vacancy, Vacancies


def write_or_dont_write(vac_list: Vacancies):
    print('Записать полученные данные в JSON файл?')
    user_answer = input('Да/Нет ').lower().strip()
    if user_answer != 'да':
        print('Спасибо за использование программы!')
    else:
        jsonfile = JSONSaver('vacancies.json')
        jsonfile.write_to_file(vac_list)
        print('Данные успешно записаны.\nСпасибо за использование программы!')


def user_interaction():
    print('Здравствуйте! \nЭта программа по поиску и сравнению вакансий на HeadHunter. \n')
    keyword = input('Введите ключевые слова для поиска вакансий: ').strip().split()
    hh_api = HH_Api()
    while True:
        pages = input('Введите количество страниц для вывода: ').strip()
        if pages.isdigit():
            pages = int(pages)
            break
        else:
            print('Можно ввести только число!')

    vac_list = hh_api.get_vacancies(keyword, pages)

    print('*' * 50)
    print('Список вакансий с сайта "HeadHunter":')
    print('-' * 50)
    print(f'Найдено {len(vac_list)} вакансий: \n')
    print(
        '1 - Вывести все вакансии.\n'
        '2 - Вывести топ-n вакансий по зарплате.\n'
        '3 - Выборка по городу.\n'
        '4 - Выборка по зарплате.\n'
        '5 - Записать результаты в файл.'
    )

    while True:
        answer = input('Выберите действие: ').strip()
        if answer.isdigit():
            answer = int(answer)
            if 1 <= answer <= 5:
                break
            else:
                print('Можно ввести только число от 1 до 5!')
        else:
            print('Можно ввести только целое число')
    print('*' * 50)
    if answer == 1:
        for vac in vac_list:
            print(vac)
        write_or_dont_write(vac_list)
    elif answer == 2:
        while True:
            top_n = input('Введите количество вакансий: ').strip()
            if top_n.isdigit():
                top_n = int(top_n)
                break
            else:
                print('Можно ввести только целое число')
        top_n_vac = vac_list.get_top_n_vacancy(top_n)
        print('*' * 50, f'\nТоп {top_n} - вакансий:\n')
        for vac in top_n_vac:
            print(vac)
        write_or_dont_write(top_n_vac)
    elif answer == 3:
        city = input('Введите название города: ').strip().lower()

        for vac in vac_list.filtered_by_city(city):
            print(vac)


