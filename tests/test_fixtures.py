import pytest
from selene.support.conditions import have
from selene.support.shared import browser


@pytest.fixture()
def browser_desktop():
    browser.config.window_width = 1280
    browser.config.window_height = 1024
    browser.open('https://github.com')
    yield browser
    browser.quit()


@pytest.fixture()
def browser_mobile():
    browser.config.window_width = 360
    browser.config.window_height = 740
    browser.open('https://github.com')
    yield browser
    browser.quit()


def test_github_desktop(browser_desktop):
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))


def test_github_mobile(browser_mobile):
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))




