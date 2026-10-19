from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


from pages.base_page import BasePage

class AllGoods(BasePage):
    page_url = '/catalog?view=all'
    
    def open_dropdown(self, locator: tuple):
        dropdowns = self.wait.until(
            EC.element_to_be_clickable(locator)
            )
        dropdowns.click()
        
    def find_field_in_dropdown(self, field: tuple, quantity_loc: tuple):
        try:
            filtres_category = self.wait.until(EC.visibility_of_element_located(field))
        except Exception:
            raise NoSuchElementException(f"Не удалось найти строку фильтра с локатором: {field_locator}")
    
        #ActionChains(self.driver).scroll_to_element(filtres_category).perform()
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", filtres_category)
        self.wait.until(EC.visibility_of(filtres_category))
        
        quantity = self.wait.until(
            EC.visibility_of_element_located(quantity_loc)
        )
        new_quantity = quantity.text.replace('(', '').replace(')', '').strip()
        try:
            ActionChains(self.driver).move_to_element(filtres_category).click().perform()
        except Exception:
            filtres_category.click()
        return new_quantity
