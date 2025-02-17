from flask import Blueprint, render_template
from app.candidates.dао.Candidates import Candidates
candidates_blueprint = Blueprint('candidates_blueprint', __name__, template_folder='templates')

candidates = Candidates()


@candidates_blueprint.route('/')
def candidates_page():
    candidates_list = candidates.all_candidates()
    return render_template('candidates.html', candidates_list=candidates_list)


@candidates_blueprint.route('/one/<int:pk>')
def one_candidate(pk):
    candidate = candidates.get_one_candidate(pk)
    return render_template('single_candidate.html', candidate=candidate)


@candidates_blueprint.route('/delete/<int:candidate_id>', methods=['DELETE'])
def candidate_on_delete(candidate_id):
    candidates.candidate_delete(candidate_id)
    return f"Пользователь с id {candidate_id} успешно удалён"


@candidates_blueprint.route('/update/<int:candidate_id>', methods=['PUT'])
def candidate_on_update(candidate_id):
    candidates.candidate_update(candidate_id)
    return f"Пользователь с id {candidate_id} успешно обновлён"


@candidates_blueprint.route('/create', methods=['POST'])
def candidate_on_create():
    candidates.candidate_create()
    return "Пользователь успешно создан"
