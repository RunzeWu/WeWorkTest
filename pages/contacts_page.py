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
    _add_member_btn_locator = (By.LINK_TEXT, "添加成员")
    _user_input_locator = (By.ID, "username")
    _userid_input_locator = (By.ID, "memberAdd_acctid")
    _memberAdd_phone_locator = (By.ID, "memberAdd_phone")
    _save_btn_locator = (By.LINK_TEXT, "保存")

    def click_contacts(self):
        ele = self.get_presence_element(self._contacts_locator)
        return ele.click()

    def click_add_btn(self):
        ele = self.get_presence_element(self._add_member_btn_locator)
        logger.info(self.driver.page_source)
        return ele.click()

    def input_info(self, username,userid,mobile):
        user_input = self.get_presence_element(self._user_input_locator)
        userid_input = self.get_presence_element(self._userid_input_locator)
        mobile_input = self.get_presence_element(self._memberAdd_phone_locator)
        self.send_keys(user_input,username)
        self.send_keys(userid_input,userid)
        self.send_keys(mobile_input,mobile)

    def submit_info(self):
        return self.get_presence_element(self._save_btn_locator).click()