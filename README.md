Задание.
Напишите программу, которая будет получать информацию о вакансиях с платформы hh.ru в России, сохранять ее в файл и позволять удобно работать с ней: добавлять, фильтровать, удалять.

Требования к реализации
Создать абстрактный класс для работы с API сервиса с вакансиями. Реализовать класс, наследующийся от абстрактного класса, для работы с платформой hh.ru. Класс должен уметь подключаться к API и получать вакансии.
Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты, такие как название вакансии, ссылка на вакансию, зарплата, краткое описание или требования и т. п. (всего не менее четырех атрибутов). Класс должен поддерживать методы сравнения вакансий между собой по зарплате и валидировать данные, которыми инициализируются его атрибуты.
Способами валидации данных может быть проверка, указана или нет зарплата. В этом случае выставлять значение зарплаты 0 или «Зарплата не указана» в зависимости от структуры класса.

Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях. Создать класс для сохранения информации о вакансиях в JSON-файл. Дополнительно, по желанию, можно реализовать классы для работы с другими форматами, например с CSV- или Excel-файлом, с TXT-файлом.
Данный класс выступит в роли основы для коннектора, заменяя который (класс-коннектор), можно использовать в качестве хранилища одну из баз данных или удаленное хранилище со своей специфической системой обращений.

В случае если какие-то из методов выглядят не используемыми для работы с файлами, то не стоит их удалять. Они пригодятся для интеграции к БД. Сделайте заглушку в коде.

Создать функцию для взаимодействия с пользователем. Функция должна взаимодействовать с пользователем через консоль. Возможности этой функции должны быть следующими:
ввести поисковый запрос для запроса вакансий из hh.ru;
получить топ N вакансий по зарплате (N запрашивать у пользователя);
получить вакансии с ключевым словом в описании.
Помимо этого функционала, можно придумать дополнительные возможности, которые покажутся удобными.

Объединить все классы и функции в единую программу.
Покрыть описанный функционал тестами.
Требования к реализации в парадигме ООП
Абстрактный класс и классы для работы с API платформ с вакансиями должны быть реализованы в соответствии с принципом наследования.
Класс для работы с вакансиями должен быть реализован в соответствии с принципом инкапсуляции и поддерживать методы сравнения вакансий между собой по зарплате.
Классы и другие сущности в проекте должны удовлетворять минимум первым двум требованиям принципов SOLID.
Документация для сбора вакансий с hh.ru
Ссылка на API: https://github.com/hhru/api/.

Выходные данные
Информация о вакансиях, полученная с разных платформ, сохраненная в JSON-файл.
Отфильтрованные и отсортированные вакансии, выводимые пользователю через консоль.
Пример использования
Данный пример можно использовать как подсказку к началу реализации. Итоговая реализация может иметь любое количество классов, функций и их названий, другой принцип организации.

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies("Python")

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

# Пример работы контструктора класса с одной вакансией
vacancy = Vacancy("Python Developer", "", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
json_saver.delete_vacancy(vacancy)

# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()



