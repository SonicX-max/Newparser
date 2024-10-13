import requests

# URL для отправки POST-запроса
url = 'https://jsonplaceholder.typicode.com/posts'

# Словарь с данными для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Вывод статус-кода и содержимого ответа
print(f'Status Code: {response.status_code}')
print('Response Content:', response.json())