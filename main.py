print('Это тестовый проект для обучения и знакомства с Git и терминалом')
print()
print('Hello from repository!')

# Импорт load_dotenv.
from dotenv import load_dotenv

# Импорт библиотеки для работы с окружением.
import os

load_dotenv()

def print_author():
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

print_author()