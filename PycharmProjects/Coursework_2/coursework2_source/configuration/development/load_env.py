import os
import dotenv

dotenv.load_dotenv()

posts_patch = os.getenv('POSTS_PATH')
comments_patch = os.getenv('COMMENTS_PATH')


print(f"Vacancies path: {posts_patch}")
print(f"Candidates path: {comments_patch}")
