print('Hello form repository!')
from dotenv import load_dotenv

import os

load_dotenv()

author = os.getenv('AUTHOR')
def print_author():

    print(f"Автор проекта: {author}")

print_author()