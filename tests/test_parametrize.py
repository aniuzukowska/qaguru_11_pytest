import pytest
from selene.support.conditions import have
from selene.support.shared import browser


@pytest.fixture(params=[(1280, 1024), (360, 740)])
def browser_set(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.open('https://github.com')
    yield browser
    browser.quit()


@pytest.mark.parametrize('browser_set', [(1280, 1024)], indirect=True)
def test_github_desktop(browser_set):
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))


@pytest.mark.parametrize('browser_set', [(360, 740)], indirect=True)
def test_github_mobile(browser_set):
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))




