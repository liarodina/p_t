# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class test_add_groupp(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "https://github.com/")
        self.selenium.start()
    
    def test_test_add_groupp(self):
        sel = self.selenium
        sel.select_window("null")
        sel.type("name=user", "admin")
        sel.type("name=pass", "secret")
        sel.click("css=input[type=\"submit\"]")
        sel.wait_for_page_to_load("30000")
        sel.click("link=groups")
        sel.wait_for_page_to_load("30000")
        sel.click("name=new")
        sel.wait_for_page_to_load("30000")
        sel.type("name=group_name", "tre")
        sel.type("name=group_header", "tret")
        sel.type("name=group_footer", "tret")
        sel.click("name=submit")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Logout")
        sel.wait_for_page_to_load("30000")
        sel.open("/SeleniumHQ/selenium/wiki/SeIDEReleaseNotes")
        sel.click("link=exact:https://github.com/SeleniumHQ/selenium/wiki/SeIDE-Release-Notes")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
