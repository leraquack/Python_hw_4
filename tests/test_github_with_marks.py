from selene.support.shared import browser
import pytest


@pytest.fixture()
def open_browser():
    # browser.element('[id="L2AGLb"]').click()
    browser.open('https://github.com/')


@pytest.mark.desktop
def test_git_on_desktop_first(open_browser):
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.element('[href="/login"]').click()


@pytest.mark.desktop
def test_git_on_desktop_second(open_browser):
    browser.config.window_width = 1800
    browser.config.window_height = 1080
    browser.element('[href="/login"]').click()


@pytest.mark.desktop
def test_git_on_desktop_third(open_browser):
    browser.config.window_width = 1700
    browser.config.window_height = 1080
    browser.element('[href="/login"]').click()


@pytest.mark.mobile
def test_git_on_mobile_first(open_browser):
    browser.config.window_width = 800
    browser.config.window_height = 300
    browser.element('[class="Button-label"]').click()
    browser.element('[href="/login"]').click()



@pytest.mark.mobile
def test_git_on_mobile_second(open_browser):
    browser.config.window_width = 640
    browser.config.window_height = 300
    browser.element('[class="Button-label"]').click()
    browser.element('[href="/login"]').click()


@pytest.mark.mobile
def test_git_on_mobile_third(open_browser):
    browser.config.window_width = 300
    browser.config.window_height = 300
    browser.element('[class="Button-label"]').click()
    browser.element('[href="/login"]').click()

