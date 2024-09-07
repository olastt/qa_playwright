from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class DataPickerPage:
    def __init__(self, page: Page) -> None:
        self.locator = None
        self.page = page

        """Локаторы страницы: Открытие дата пикера"""
        self.select_calendar = Button(page, locator='//*[@id="datePickerMonthYearInput"]', name='Календарь')
        self.choose_month = Button(page, locator='//*[@class="react-datepicker__month-select"]', name='Месяц')
        self.choose_year = Button(page, locator='//*[@class="react-datepicker__year-select"]', name='Год')
        self.choose_day = Button(page, locator='//*[@class="react-datepicker__day react-datepicker__day--002"]', name='День')

        """Локаторы страницы: Открытие второго дата пикера"""
        self.select_second_calendar = Button(page, locator='//*[@id="dateAndTimePickerInput"]', name='Календарь 2')
        self.choose_second_month = Button(page, locator='//*[@class="react-datepicker__month-read-view"]',
                                          name='Месяц')
        self.choose_second_year = Button(page, locator='//*[@class="react-datepicker__year-read-view"]', name='Год')
        self.click_to_year = Button(page, locator='(//*[@class="react-datepicker__year-option"])[12]', name='Год')
        self.choose_second_day = Button(page, locator='//*[@class="react-datepicker__day react-datepicker__day--015 react-datepicker__day--weekend"]',
                                        name='День')

