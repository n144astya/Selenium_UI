from selenium.webdriver.common.by import By

allert_fild_locator = (By.XPATH, "//div[@class ='auth-alert auth-alert-error']")
email_fild_locator = (By.ID, 'email')
password_fild_locator = (By.ID, 'password')
button_log_in_locator = (By.CSS_SELECTOR, 'button.auth-submit-btn')
