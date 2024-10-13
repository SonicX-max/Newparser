import requests

# URL API GitHub для поиска репозиториев
url = "https://api.github.com/search/repositories"

# Параметры запроса
params = {
    "q": "language:html"  # Поиск репозиториев с кодом HTML
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Вывод статус-кода ответа
print("Статус-код:", response.status_code)

# Вывод содержимого ответа в формате JSON
try:
    # Преобразование ответа в формат JSON и вывод
    json_response = response.json()
    print("Ответ в формате JSON:", json_response)
except ValueError:
    print("Ответ не в формате JSON")