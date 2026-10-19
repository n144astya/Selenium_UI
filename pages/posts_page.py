from pages.base_page import BasePage

class PostsPage(BasePage):
    page_url = '/kastriuli'
    
    def test_check_the_page_title_is(self, text):
        header_title = self.driver.title
        assert text in header_title.text() 