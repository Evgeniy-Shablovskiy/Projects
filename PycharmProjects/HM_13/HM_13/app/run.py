from flask import Flask
from main.views import main_blueprint
from candidates.views import candidates_blueprint
from vacancies.views import vacancies_blueprint


app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(candidates_blueprint, url_prefix="/candidates")
app.register_blueprint(vacancies_blueprint, url_prefix="/vacancies")


app.run()
