import pytest
from selene.support.shared import browser

@pytest.fixture()
def open_browser():
    base_url = 'https://google.com'
    browser.open(base_url)


@pytest.fixture(params=[pytest.param(1920, 1800, 1700, 800, 640, 300)])
def width(request):
    assert request.param in [1920, 1800, 1700, 800, 640, 300]


@pytest.mark.parametrize("width", [800, 640, 300], indirect=True)
def test_mobile_with_indirect_parametrization(open_browser, width):
    browser.config.window_width = width
    browser.config.window_height = 300
    browser.element('[aria-label="Toggle navigation"]').click()
    browser.element('[href="/login"]').click()


@pytest.mark.parametrize("width", [1920, 1800, 1700], indirect=True)
def test_desktop_with_indirect_parametrization(open_browser, width):
    browser.config.window_width = width
    browser.config.window_height = 1080
    browser.element('[href="/login"]').click()




