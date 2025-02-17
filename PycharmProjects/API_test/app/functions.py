import json
from flask import jsonify


def load_from_json():
    with open('data.json', 'r') as file:
        tasks = json.load(file)
        return tasks


def upload_to_json(tasks):
    with open('data.json', 'w') as file:
        json.dump(tasks, file, ensure_ascii=False)


def binary_search(task_id):
    tasks = load_from_json()
    low = 0
    high = len(tasks) - 1

    while low <= high:
        mid = (low + high) // 2
        if tasks[mid]['id'] == task_id:
            return jsonify(tasks[mid])
        elif tasks[mid]['id'] < task_id:
            low = mid + 1
        else:
            high = mid - 1

    return 'Значение не найдено'

