# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-04
 @Author:       吴润泽 
'''
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from common.mylog import get_logger

logger = get_logger("caontacts_page")


class ContactsPage(BasePage):
    _contacts_locator = (By.XPATH, "//*[@id='menu_contacts']/span")
    _add_member_btn_locator = (By.XPATH, "//div[@class='ww_operationBar']//a[@class='qui_btn ww_btn js_add_member']")
    _user_input_locator = (By.NAME, "username")
    _userid_input_locator = (By.NAME, "acctid")
    _memberAdd_phone_locator = (By.NAME, "mobile")
    _save_btn_locator = (By.LINK_TEXT, "保存")

    def click_contacts(self):
        ele = self.get_presence_element(self._contacts_locator)
        return ele.click()

    def click_add_btn(self):
        ele = self.get_visible_element(self._add_member_btn_locator)
        ele.click()

    def input_info(self, username, userid, mobile):
        user_input = self.get_visible_element(self._user_input_locator)
        user_input.send_keys(username)
        userid_input = self.get_visible_element(self._userid_input_locator)
        userid_input.send_keys(userid)
        mobile_input = self.get_visible_element(self._memberAdd_phone_locator)
        mobile_input.send_keys(mobile)

    def submit_info(self):
        return self.get_visible_element(self._save_btn_locator).click()