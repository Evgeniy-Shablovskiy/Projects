from app.functions.load_from_json import load_from_json
from app.config.development.load_env import vacancies_patch


class Vacancies:
    def __init__(self):
        pass

    def all_vacancies(self):
        data = load_from_json(vacancies_patch)
        return data

    def get_one_vacancie(self, pk):
        data = load_from_json(vacancies_patch)
        low = 0
        high = len(data) - 1

        while low <= high:
            mid = (low + high) // 2
            if data[mid]['pk'] == pk:
                return data[mid]
            elif data[mid]['pk'] < pk:
                low = mid + 1
            else:
                high = mid - 1

        return 'Значение не найдено'  # Если значение не найдено