# вспомогательные методы логин и логаут
import self as self


class SessionHelper:

    # конструктор для доступа к драйверу
    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.driver
        wd.find_element_by_link_text("Logout").click()

    def login(self, username, password):
        self.app.open_home_page()
        wd = self.app.driver
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def ensure_logout(self):
        wd = self.app.driver
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.driver
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def ensure_login(self, username, password):
        wd = self.app.driver
        if self.is