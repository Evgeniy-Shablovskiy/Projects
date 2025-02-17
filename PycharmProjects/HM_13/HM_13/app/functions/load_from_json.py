import json
from app.config.development.load_env import candidates_patch, vacancies_patch


def load_from_json(path):
    if path == candidates_patch:
        with open(f'{candidates_patch}', 'r') as file:
            candidates = json.load(file)
            return candidates
    if path == vacancies_patch:
        with open(f'{vacancies_patch}', 'r') as file:
            vacancies = json.load(file)
            return vacancies
