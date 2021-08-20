import pytest as pytest

from app import Application
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://www.python.org",
                     help="Python site url")


@pytest.fixture(scope='session')
def app(request):
    url = request.config.getoption("--url")
    app = Application(webdriver.Chrome(ChromeDriverManager().install()), url)
    yield app
    app.quit()
