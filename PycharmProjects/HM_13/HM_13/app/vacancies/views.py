from flask import Blueprint, render_template
from app.vacancies.dао.Vacancies import Vacancies
vacancies_blueprint = Blueprint('vacancies_blueprint', __name__, template_folder='templates')


vacancies = Vacancies()


@vacancies_blueprint.route('/')
def vacancies_page():
    vacancies_list = vacancies.all_vacancies()
    return render_template('vacancies.html', vacancies_list=vacancies_list)


@vacancies_blueprint.route('/one/<int:pk>')
def one_candidate(pk):
    vacancie = vacancies.get_one_vacancie(pk)
    return render_template('single_vacancie.html', vacancie=vacancie)