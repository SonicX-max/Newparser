import requests

# URL API для получения постов
url = "https://jsonplaceholder.typicode.com/posts"

# Параметры запроса
params = {
    "userId": 1  # Фильтрация постов по userId, равному 1
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Проверка успешности запроса
if response.status_code == 200:
    try:
        # Преобразование ответа в формат JSON
        posts = response.json()

        # Вывод полученных записей
        print("Полученные записи:")
        for post in posts:
            print(f"ID: {post['id']}, Title: {post['title']}")
    except ValueError:
        print("Ответ не в формате JSON")
else:
    print(f"Ошибка: статус-код {response.status_code}")