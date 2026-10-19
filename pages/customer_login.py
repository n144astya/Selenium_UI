from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException

from pages.base_page import BasePage
from pages.locators import login_loc as loc

class CustomerLogin(BasePage):
    page_url = '/login'

    def _safe_send_keys(self, locator, text):
        for attempt in range(5):
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.clear()
                element.send_keys(text)
                return
            except (StaleElementReferenceException, ElementNotInteractableException) as e:
                 print(f"\n[Safe Input] Элемент {locator} не готов (Stale/NotInteractable). Пробуем снова, попытка {attempt + 1}...")
                 continue
        raise AssertionError(f"Не удалось ввести текст в элемент {locator} за 5 попыток из-за агрессивного обновления DOM")

    def fill_login_form(self, login, password):
        self._safe_send_keys(loc.email_fild_locator, login)
        self._safe_send_keys(loc.password_fild_locator, password)
        
        button_log_in = self.wait.until(EC.element_to_be_clickable(loc.button_log_in_locator))
        button_log_in.click()
        return self

    def check_error_alert_is(self, text):
        alert_field = self.wait.until(EC.visibility_of_element_located(loc.allert_fild_locator))
        self.wait.until(EC.text_to_be_present_in_element(loc.allert_fild_locator, text))
        assert alert_field.text == text, f"Ожидали ошибку '{text}', но на сайте написано: '{alert_field.text}'"
        return self

    def check_successful_login(self):
        self.wait.until(lambda d: "/login" not in d.current_url)
        print(f"\n[Успешный вход] Авторизация прошла успешно! Текущий URL: {self.driver.current_url}")
        return self