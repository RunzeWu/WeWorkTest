# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-04
 @Author:       吴润泽 
'''
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from common.mylog import get_logger

logger = get_logger(__name__)


class SearchResultPage(BasePage):
    _search_input_loc = (By.ID, "memberSearchInput")
    _edit_loc = (By.XPATH, "//a[@class='qui_btn ww_btn js_edit']")
    # 禁用启用是一个
    _disable_loc = (By.XPATH, "//a[@class='qui_btn ww_btn js_disable']")
    _save_loc = (By.XPATH, "qui_btn ww_btn ww_btn_Blue js_save")
    _confirm_btn_loc = (By.XPATH, "qui_btn ww_btn ww_btn_Blue")
    _tips_loc = (By.ID, "js_tips")

    def search_member(self, name):
        search_input = self.get_visible_element(self._search_input_loc)
        search_input.send_keys(name)

    def click_edit(self):
        ele = self.get_visible_element(self._edit_loc)
        ele.click()

    def click_save(self):
        ele = self.get_visible_element(self._save_loc)
        ele.click()

    def click_disable(self):
        ele = self.get_visible_element(self._disable_loc)
        ele.click()

    def click_confirm(self):
        ele = self.get_visible_element(self._confirm_btn_loc)
        ele.click()

    def get_toast(self):
        return self.get_text(self._tips_loc)
