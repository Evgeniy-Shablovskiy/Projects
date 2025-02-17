from flask import Flask, jsonify, request
from app.functions import load_from_json, upload_to_json, binary_search
app = Flask(__name__)


@app.route('/tasks', methods=['GET'])
def get_task():
    tasks = load_from_json()
    return jsonify(tasks)


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_one_task(task_id):
    return binary_search(task_id)


@app.route('/tasks', methods=['POST'])
def create_task():
    tasks = load_from_json()
    task = {
        "id": tasks[-1]['id'] + 1,
        "title": request.json.get('title'),
        "description": request.json.get('description', ''),
        "done": False
    }
    tasks.append(task)
    upload_to_json(tasks)
    return jsonify(task)


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = binary_search(task_id)
    tasks = load_from_json()
    tasks['title'] = task.get('title', tasks['title'])
    tasks['description'] = task.get('description', tasks['description'])
    tasks['done'] = task.get('done', tasks['done'])
    return 'Успешно изменено'


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_from_json()
    tasks.pop(task_id - 1)
    upload_to_json(tasks)
    return "Успешно удалено"


if __name__ == '__main__':
    app.run(debug=True)
