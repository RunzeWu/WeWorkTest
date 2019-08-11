# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-04
 @Author:       吴润泽 
'''
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ManageToolsPage(BasePage):
    _menu_manageTools_loc = (By.ID, "menu_manageTools")
    _img_manager_loc = (By.XPATH, "//div[contains(text(), '素材库')]")
    _img_loc = (By.XPATH, "//a[contains(text(), '图片')]")

    def goto_manager_img(self):
        ele = self.get_visible_element(self._menu_manageTools_loc)
        ele.click()
        self.get_visible_element(self._img_manager_loc).click()
        self.get_visible_element(self._img_loc).click()