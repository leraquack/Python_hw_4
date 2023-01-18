import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def open_browser():
    base_url = 'https://google.com'
    browser.open(base_url)

@pytest.mark.desktop
def test_git_on_desktop_first(open_browser):
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.element('[data - hydro - click - hmac = "cd4f672ed9a2fa51ea92c28de162e81edb2d11a2aad6884ec89a6d60b21b1cfb"]').click()

@pytest.mark.desktop
def test_git_on_desktop_second(open_browser):
    browser.config.window_width = 1800
    browser.config.window_height = 900
    browser.element('[data - hydro - click - hmac = "cd4f672ed9a2fa51ea92c28de162e81edb2d11a2aad6884ec89a6d60b21b1cfb"]').click()

@pytest.mark.desktop
def test_git_on_desktop_third(open_browser):
    browser.config.window_width = 1700
    browser.config.window_height = 850
    browser.element('[data - hydro - click - hmac = "cd4f672ed9a2fa51ea92c28de162e81edb2d11a2aad6884ec89a6d60b21b1cfb"]').click()

@pytest.mark.mobile
def test_git_on_mobile_first(open_browser):
    browser.config.window_width = 800
    browser.config.window_height = 600
    browser.element('[data - hydro - click - hmac = "520d87e8f83281e6946b192f0f840552721c7fcba9b9c36d802e898a816314e2"]').click()

@pytest.mark.mobile
def test_git_on_mobile_second(open_browser):
    browser.config.window_width = 640
    browser.config.window_height = 480
    browser.element('[data - hydro - click - hmac = "520d87e8f83281e6946b192f0f840552721c7fcba9b9c36d802e898a816314e2"]').click()

@pytest.mark.mobile
def test_git_on_mobile_third(open_browser):
    browser.config.window_width = 300
    browser.config.window_height = 500
    browser.element('[data - hydro - click - hmac = "520d87e8f83281e6946b192f0f840552721c7fcba9b9c36d802e898a816314e2"]').click()

