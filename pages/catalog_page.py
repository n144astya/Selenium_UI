from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException 

from pages.base_page import BasePage
from pages.locators import catalog_loc as loc


class CatalogPage(BasePage):
    page_url = '/catalog'
    
    def check_the_page_title_is(self, text):
            header_title = self.driver.title
            assert text in header_title, f"Ожидали '{text}' в тайтле, но там: '{header_title}'"

    def go_to_pots_category(self):
        # Запоминаем тайтл до клика для борьбы с гонкой условий (SPA)
        old_title = self.driver.title
        category_pots =  self.wait.until(EC.visibility_of_element_located(loc.pots_locator))
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', category_pots) #скролл
        self.driver.execute_script('arguments[0].click();', category_pots) #кликаем по выбранной плашке через JS
        self.wait.until(lambda d: d.title != old_title)