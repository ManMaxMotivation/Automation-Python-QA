# Импорт модуля requests для отправки HTTP-запросов
import requests
# Импорт конфигурационного файла, который содержит настройки URL
import configuration
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body)

# Вывод HTTP-статус кода ответа на запрос
# Код состояния указывает на результат обработки запроса сервером
print(response.status_code)
print(response.json())

# Определение функции для отправки POST-запроса создания нового набора. Два параметра: kit_body — тело запроса, auth_token — токен авторизации.
def post_new_client_kit(kit_body,auth_token):
    # Отправка POST-запроса с использованием URL из конфигурации, данных о наборах и токене авторизации
    auth_headers = data.headers.copy()
    auth_headers["Authorization"] = "Bearer " + auth_token
    # Возвращается объект ответа, полученный от сервера
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KITS_PATH,
                         json=kit_body,
                         headers=auth_headers)

# Вызов функции с передачей списка kit_body продуктов из файла data.py и токена авторизации
response = post_new_client_kit(data.kit_body,data.headers["Authorization"])

# Вывод HTTP-статус кода ответа и тела ответа в формате JSON
# Это позволяет проверить успешность выполнения запроса и посмотреть результаты поиска наборов
print(response.status_code)
print(response.json())