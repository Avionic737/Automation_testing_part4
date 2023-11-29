import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose the language: es, fr, en, etc.")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    print(f"\nstart browser for test with language: {language}..")

    # Browser options for language settings
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # options.add_argument('headless')  # for headless
    # options.add_argument('window-size=1920x935')  # window size

    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
