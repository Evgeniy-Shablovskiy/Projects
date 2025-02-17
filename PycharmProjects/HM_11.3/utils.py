import json
import re


def load_candidates_from_json():  # Написать отдельную ф-ию, для передачи прочтенного json-файла
    with open('candidates.json', 'r', encoding='UTF-8') as file:
        leading_to_list = json.load(file)
    return leading_to_list


def get_candidate(candidate_id):  # Возвращает пользователя по его id. Для всех айди справедливо выражение:
    return load_candidates_from_json()[candidate_id - 1]  # id_2 = id_1 + 1 (id_1 = 0)


def get_candidates_by_name(candidate_name):  # Возвращает пользователя по его имени
    list_of_person = []
    for person in load_candidates_from_json():
        if candidate_name in person.get('name').split()[0]:
            list_of_person.append(person)
    return list_of_person


def get_candidates_by_skill(skill_name):  # Возвращает пользователя по его скилу
    list_of_skills = []
    for person in load_candidates_from_json():
        if skill_name in re.split(', | ', person.get('skills').lower()):
            list_of_skills.append(person)
    return list_of_skills
