from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/addressbook/group.php"
        self.session = SessionHelper(self)  # в качестве параметра передаем ссылку на фикстуру через обьект класса
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.driver
        wd.get(self.base_url + "/addressbook/group.php")
        return wd

    def destroy(self):
        self.driver.quit()
