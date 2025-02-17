from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route('/')  # Список всех кандидатов
def all_candidates():
    list_of_candidates = utils.load_candidates_from_json()
    return render_template('list.html', list_of_candidates=list_of_candidates)


@app.route('/candidate/<int:candidate_id>')  # Поиск кандидата по его айди
def page_of_candidate(candidate_id):
    candidate = utils.get_candidate(candidate_id)
    return render_template('single.html', candidate=candidate)


@app.route("/search/<candidate_name>")  # Поиск кандидата по его имени
def search_candidate(candidate_name):
    return render_template("search.html", candidate_name=candidate_name, list_of_person=utils.get_candidates_by_name(candidate_name))


@app.route("/skill/<skillname>")  # Поиск кандидата по его скиллу
def search_skillname(skillname):
    return render_template("skill.html", skillname=skillname, list_of_skills=utils.get_candidates_by_skill(skillname))


app.run(host='127.0.0.1', port=80)
