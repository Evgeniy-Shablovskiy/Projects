from app.functions.load_from_json import load_from_json
from app.config.development.load_env import candidates_patch
import json


class Candidates:
    def __init__(self):
        pass

    def all_candidates(self):
        data = load_from_json(candidates_patch)
        return data

    def get_one_candidate(self, pk):
        data = load_from_json(candidates_patch)
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

    def candidate_delete(self, id_of_candidate_on_delete):
        candidates = Candidates.all_candidates(self)
        candidates.pop(id_of_candidate_on_delete - 1)
        with open("../app/data/candidates.json", 'w') as file:
            json.dump(candidates, file)

    def candidate_update(self, id_of_candidate_on_update):
        candidates = Candidates.all_candidates(self)
        candidates[id_of_candidate_on_update - 1]['name'] = input('имя на латыни')
        with open("../app/data/candidates.json", 'w') as file:
            json.dump(candidates, file)

    def candidate_create(self):
        candidates = Candidates.all_candidates(self)
        candidate = {"pk": None, "name": None, "position": None}
        candidate["pk"] = len(candidates) + 1
        candidate["name"] = input('fe')
        candidate["position"] = input('fe')
        candidates.append(candidate)
        with open("../app/data/candidates.json", 'w') as file:
            json.dump(candidates, file)
