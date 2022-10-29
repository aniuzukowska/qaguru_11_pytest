import pytest
from selene.support.conditions import have
from selene.support.shared import browser
import settings


@pytest.fixture(params=[(1280, 1024), (360, 740)], ids=['desktop', 'mobile'])
def browser_set(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield browser
    browser.quit()


def test_github_desktop(browser_set):
    if (browser.config.window_width, browser.config.window_height) not in settings.desktop:
        pytest.skip('Пропущен тест, не относящийся к тестированию desktop')
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))


def test_github_mobile(browser_set):
    if (browser.config.window_width, browser.config.window_height) not in settings.mobile:
        pytest.skip('Пропущен тест, не относящийся к тестированию mobile')
    browser.open('https://github.com')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))




