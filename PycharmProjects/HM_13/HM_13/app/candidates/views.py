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