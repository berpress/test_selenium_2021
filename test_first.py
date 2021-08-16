from pages.main_page import MainPage


def test_1():
    main_page = MainPage()
    main_page.open_main_page()
    assert "Python" in main_page.get_title()
    main_page.search("pycon")
    assert "No results found." not in main_page.get_page_source()
    main_page.quit()


test_1()
