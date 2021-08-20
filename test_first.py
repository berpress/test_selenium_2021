def test_1(app):
    app.main_page.open_main_page()
    app.main_page.search("pycon")
    assert "No results found." not in app.main_page.page_source()


def test_2(app):
    app.main_page.open_main_page()
    app.main_page.search("pycon")
    assert "No results found." not in app.main_page.page_source()

