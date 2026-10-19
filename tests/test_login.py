#  python -m pytest test_login.py - всю папку
#  python -m pytest tests/test_login.py::<имя теста>

import pytest 
from pages.customer_login import CustomerLogin
from config import Config

def test_successful_login(login_page: CustomerLogin):
    login_page.open_page()
    login_page.fill_login_form(Config.USER_EMAIL, Config.USER_PASSWORD)
    login_page.check_successful_login()

@pytest.mark.parametrize("email, password, expected_error", [
    ('wrong@mail.ru', 'wrong_pass', 'Неверный адрес электронной почты или пароль.'),
    ('', 'any_pass', 'Пожалуйста, заполните все поля.'), 
    ('wrong@mail.ru', '', 'Пожалуйста, заполните все поля.')
])

def test_incorrect_login(login_page: CustomerLogin, email, password, expected_error):
    login_page.open_page()
    login_page.fill_login_form(email, password)
    login_page.check_error_alert_is(expected_error)




