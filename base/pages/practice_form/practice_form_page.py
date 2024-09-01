from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class PracticeFormPage:
    def __init__(self, page: Page) -> None:
        self.locator = None
        self.page = page

        """Локаторы страницы: ФИО"""
        self.first_name = Input(page, locator='//*[@id="firstName"]', name='Имя')
        self.last_name = Input(page, locator='//*[@id="lastName"]', name='Фамилия')

        """Локаторы страницы: Почта"""
        self.email = Input(page, locator='//*[@id="userEmail"]', name='Почта')


        # self.gender = Button(page, locator='//*[@id="gender-radio-2"]', name='Пол')

        """Локаторы страницы: Номер телефона"""
        self.number = Input(page, locator='//*[@id="userNumber"]', name='Мобильный')

        """Локаторы страницы: Предметы"""
        self.subject = Input(page, locator='//*[@id="subjectsInput"]', name='Предметы')

        """Локаторы страницы: Датапикер"""
        self.drop_calendar = Button(page, locator='//*[@id="dateOfBirthInput"]', name='Календарь')
        self.choose_month = Button(page, locator='//*[@class="react-datepicker__month-select"]', name='Календарь')
        self.choose_year = Button(page, locator='//*[@class="react-datepicker__year-select"]', name='Календарь')
        self.choose_day = Button(page, locator='//*[@class="react-datepicker__day react-datepicker__day--002"]', name='Календарь')

        """Локаторы страницы: Хобби"""
        self.hobbies = Button(page, locator='//*[@for="hobbies-checkbox-3"]', name='Увлечения')

        """Локаторы страницы: Загрузка файла"""
        self.upload = Button(page, locator='//*[@id="uploadPicture"]', name='Изображение')

        """Локаторы страницы: Адрес"""
        self.address = Input(page, locator='//*[@id="currentAddress"]', name='Адрес')

        """Локаторы страницы: Город"""
        self.city = Button(page, locator='//*[@class=" css-yk16xz-control"]', name='Город')


        #
        # """Ожидания"""
        # self.Wait_first_name = '//*[@id="firstName"]'
        # self.Wait_last_name = '//*[@id="lastName"]'
        # self.Wait_email = '//*[@id="userEmail"]'
        # # self.Wait_gender = '//*[@id="gender-radio-2"]'
        # self.Wait_number = '//*[@id="userNumber"]'
        # self.Wait_subject = '//*[@id="subjectsInput"]'
        # self.Wait_drop_month = '(//*[starts-with(@class, "react-datepicker__month")])[2]'
