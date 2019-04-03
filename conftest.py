import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver_init(request):

    browser = webdriver.Firefox()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", browser)
    yield
    browser.close()
