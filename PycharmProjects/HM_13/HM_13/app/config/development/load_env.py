import os
import dotenv

dotenv.load_dotenv()

vacancies_patch = os.getenv('VACANCIES_PATH')
candidates_patch = os.getenv('CANDIDATES_PATH')


print(f"Vacancies path: {vacancies_patch}")
print(f"Candidates path: {candidates_patch}")
