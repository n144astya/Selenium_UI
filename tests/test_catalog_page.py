def test_title_category(catalog_page):
    catalog_page.open_page()
    catalog_page.check_the_page_title_is('Каталог')

def test_go_to_the_posts_category(catalog_page):
    catalog_page.open_page()
    catalog_page.go_to_pots_category()
    catalog_page.check_the_page_title_is('Кастрюли')
    
