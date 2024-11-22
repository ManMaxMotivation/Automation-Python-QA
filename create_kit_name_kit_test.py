# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request
# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

#Тестовые значения для проверок №2 и №4
kit_body511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
kit_body512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"

# функция получения токена
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token

# эта функция меняет значения в параметре name
def get_kit_body(name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_kit_body = data.kit_body.copy()
    # изменение значения в поле name
    current_kit_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return current_kit_body


# Функция для позитивной проверки код 200
def positive_assert(name):
    # В переменную kit_body и auth_token сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    # В переменную kit_response сохраняется результат запроса на создание пользователя:
    kit_response = sender_stand_request.post_new_client_kit(kit_body,auth_token)

    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверка текста в теле ответа в атрибуте "name"
    assert kit_response.json()["name"] == name

 # Функция для негативной проверки код 400
def negative_assert_code_400(name):
    # В переменную kit_body и auth_token сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    # В переменную kit_response сохраняется результат запроса
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Проверка, что код ответа равен 400
    assert kit_response.status_code == 400
    # Проверка, что в теле ответа атрибут "code" равен 400
    assert kit_response.json()["code"] == 400
    # Проверка текста в теле ответа в атрибуте "message"
    assert kit_response.json()["message"] == "Не все необходимые параметры были переданы"

    # Функция для негативной проверки
    # В ответе ошибка: "Не все необходимые параметры были переданы"
def negative_assert_no_name(kit_body):
    auth_token = get_new_user_token()
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Проверь, что код ответа — 400
    assert kit_response.status_code == 400
    # Проверь, что в теле ответа атрибут "code" — 400
    assert kit_response.json()["code"] == 400
    # Проверь текст в теле ответа в атрибуте "message"
    assert kit_response.json()["message"] == "Не все необходимые параметры были переданы"

# Тест 1. Допустимое количество символов (1): PASSED
# kit_body = {"name": "a"}
def test_create_kit_1_letter_name_get_success_response():
    positive_assert("a")
# Тест 2. Допустимое количество символов (511): PASSED
# kit_body = {"name": "kit_body511"}
def test_create_kit_511_letter_name_get_success_response():
    positive_assert(kit_body511)
# Тест 3. Количество символов меньше допустимого (0): FAILED
# kit_body = {"name": ""}
def test_create_kit_0_letter_name_get_error_response():
    negative_assert_code_400("")
# Тест 4. Количество символов больше допустимого (512): FAILED
# kit_body = {"name": "kit_body512"}
def test_create_kit_512_letter_name_get_error_response():
    negative_assert_code_400(kit_body512)
# Тест 5. Разрешены английские буквы (QWErty): PASSED
# kit_body = {"name": "QWErty"}
def test_create_kit_english_letter_name_get_success_response():
    positive_assert("QWErty")
# Тест 6. Разрешены русские буквы (Мария): PASSED
# kit_body = {"name": "Мария"}
def test_create_kit_rus_letter_name_get_success_response():
    positive_assert("Мария")
# Тест 7. Разрешены спецсимволы (""№%@","): PASSED
# kit_body = {"name": ""№%@","}
def test_create_kit_symbol_letter_name_get_success_response():
    positive_assert("\"№%@\",")
# Тест 8. Разрешены пробелы (Человек и КО): PASSED
# kit_body = {"name": "Человек и КО"}
def test_create_kit_space_letter_name_get_success_response():
    positive_assert("Человек и КО")
# Тест 9. Разрешены цифры (123): PASSED
# kit_body = {"name": "123"}
def test_create_kit_digit_letter_name_get_success_response():
    positive_assert("123")
# Тест 10. Параметр не передан в запросе (): FAILED
# kit_body = {}
def test_create_kit_no_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную kit_body
    # Иначе можно потерять данные из исходного словаря
    kit_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert_no_name(kit_body)
# Тест 11. Передан другой тип параметра (число): FAILED
# kit_body = {"name": 123}
def test_create_kit_type_digit_letter_name_get_error_response():
    negative_assert_code_400(123)