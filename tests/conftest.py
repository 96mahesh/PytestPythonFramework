import pytest
from selenium import webdriver

from utilities import ReadConfiguration


@pytest.fixture
def setUp_and_teardown(request):
    browser = ReadConfiguration.read_configaration("basic info","browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print('provid the browser name from the list chrome/firefox/edge')

    driver.maximize_window()
    app_url = ReadConfiguration.read_configaration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
