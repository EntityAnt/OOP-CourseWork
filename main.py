from src.api import HH_Api
from src.utils import user_interaction


def main():
    user_interaction()


def my_fun():
    hh_api = HH_Api()
    vac_list = hh_api.get_vacancies('повар', 1)
    sort_vac = sorted(vac_list, reverse=True)[0]
    # print(sort_vac)
    print(sort_vac.to_dict())
    # for vac in vac_list:
    #     print(vac)


if __name__ == '__main__':
    main()
    # my_fun()
