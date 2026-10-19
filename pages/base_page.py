from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class BasePage:
    base_url = 'https://weiwix.by'
    page_url = None

    def __init__(self, driver: WebDriver):
            self.driver = driver
            self.wait = WebDriverWait(
                driver, 
                timeout=10,
                poll_frequency=0.3, # Опрашиваем страницу трижды в секунду
                ignored_exceptions=[StaleElementReferenceException]
            )
    def verify_current_url_is_base_url(self):
          self.wait.until(EC.url_to_be(self.base_url))
          assert self.driver.current_url == self.base_url, (
            f"Ожидали базовый URL '{self.base_url}', "
            f"но сейчас открыт: '{self.driver.current_url}'"
        )
          return self

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
             raise NotImplementedError('Page can not be opened for this page class')
        return self

    def find(self, locator: tuple):
         self.driver.find_element(locator)
         return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator) 