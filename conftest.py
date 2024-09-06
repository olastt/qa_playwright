import pytest

from base.pages.button_form.button_page import ButtonPage
from base.pages.checkbox_form.checkbox_page import CheckboxPage
from base.pages.elements_form.elements_page import ElementsPage
from base.pages.practice_form.practice_form_page import PracticeFormPage
from base.pages.radio_button_form.radio_button_page import RadioButtonPage
from py_src.config.playwright import PlaywrightConfig
from playwright.sync_api import Page, sync_playwright, Browser


@pytest.fixture()
def page() -> Page:
    with sync_playwright() as playwright:
        browser = get_browser(playwright)
        page = browser.new_page(viewport=PlaywrightConfig.PAGE_VIEWPORT_SIZE)
        yield page
        browser.close()


def get_browser(playwright) -> Browser:
    browser_type = playwright.chromium if PlaywrightConfig.BROWSER == 'chrome' else playwright.firefox
    return browser_type.launch(
        headless=PlaywrightConfig.IS_HEADLESS,
        slow_mo=PlaywrightConfig.SLOW_MO
    )


@pytest.fixture(scope='function')
def practice_form(page: Page) -> PracticeFormPage:
    return PracticeFormPage(page)


@pytest.fixture(scope='function')
def elements_form(page: Page) -> ElementsPage:
    return ElementsPage(page)


@pytest.fixture(scope='function')
def checkbox_form(page: Page) -> CheckboxPage:
    return CheckboxPage(page)


@pytest.fixture(scope='function')
def radio_button_form(page: Page) -> RadioButtonPage:
    return RadioButtonPage(page)

@pytest.fixture(scope='function')
def button_form(page: Page) -> ButtonPage:
    return ButtonPage(page)

