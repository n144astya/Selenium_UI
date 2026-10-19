from pages.locators import all_goods_locators as loc


def test_navigate_from_all_products_go_to_the_soft_toys_category_via_filtres(all_goods):
    all_goods.open_page()
    
    all_goods.open_dropdown(loc.dropdowns_category_locator)

    expected_quantity = all_goods.find_field_in_dropdown(loc.filtres_category_soft_toys_locator, loc.quantity_filtres_category_soft_toys_loc)
    
    all_product_cards = all_goods.find_all(loc.PRODUCT_CARDS)
    quantity_category_soft_toys = len(all_product_cards)
    assert int(expected_quantity) == quantity_category_soft_toys, (
        f"В фильтре было: {expected_quantity}, а на странице: {quantity_category_soft_toys}"
    )
