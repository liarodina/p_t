class GroupHelper:
    #конструкт в которую идет ссылка на application(main class fixture)
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
        wd = self.app.driver
        wd.find_element_by_link_text("groups").click()