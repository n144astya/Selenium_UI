from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import pytest
from pages.all_goods_page import AllGoods
from pages.catalog_page import CatalogPage
from pages.customer_login import CustomerLogin
from pages.posts_page import PostsPage

import os
from dotenv import load_dotenv


@pytest.fixture()
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver

@pytest.fixture()
def all_goods(driver):
    return AllGoods(driver)

@pytest.fixture()
def catalog_page(driver):
    return CatalogPage(driver)

@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)

@pytest.fixture()
def post_page(driver):
    return PostsPage(driver)