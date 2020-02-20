from selenium import webdriver

class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/addressbook/group.php"
        self.verificationErrors = []
    def logout(self):
        wd = self.driver
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self):
        wd = self.driver
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.driver
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def open_group_page(self):
        wd = self.driver
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        self.open_home_page()
        wd = self.driver
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self):
        wd = self.driver
        wd.get(self.base_url + "/addressbook/group.php")
        return wd

    def destroy(self):
        self.driver.quit()