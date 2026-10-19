from selenium.webdriver.common.by import By


quantity_filtres_category_soft_toys_loc = (By.XPATH, '//div[contains(text(), "Мягкие игрушки")]/span')
PRODUCT_CARDS = (By.XPATH, '//div[@class="products-grid"]//div[@class="product-image-wrapper"]')
filtres_category_soft_toys_locator = (By.XPATH, '//div[contains(text(), "Мягкие игрушки")]')
dropdowns_category_locator = (By.XPATH, '//div[@class="filter-pill-wrapper"][1]')