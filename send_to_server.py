import requests
# Создаем сообщение

username = input('Твое имя: ')
text = input('Введи текст сообщения: ')

# Запаковываем сообщение в Get запрос
requests.get(
    'http://127.0.0.1:5000/send_messages',
    json={'username': username, 'text': text}
)