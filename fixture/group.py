class GroupHelper:
    # конструкт в которую идет ссылка на application(main class fixture)
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.driver
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.driver
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def fill_group_form(self, group):
        wd = self.app.driver
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.driver
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.driver
        self.open_group_page()
        self.selectf_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def selectf_first_group(self):
        wd = self.app.driver
        wd.find_element_by_name("selected[]").click()

    def open_group_page(self):
        wd = self.app.driver
        wd.find_element_by_link_text("groups").click()


    def modify_first_group(self, new_group_data):
        wd = self.app.driver
        self.open_group_page()
        self.selectf_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
