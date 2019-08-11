# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-04
 @Author:       吴润泽 
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class ImageManagerPage(BasePage):
    _upload_btn_loc = (By.XPATH, "//a[@class='qui_btn ww_btn ww_btn_WithIcon ww_fileInputWrap js_upload_file_selector']")
    _upload_input_loc = (By.ID, 'js_upload_input')
    _confirm_btn_loc = (By.XPATH, "//a[@class='qui_btn ww_btn ww_btn_Blue js_next']")
    _total_number_loc = (By.XPATH, "//span[@class='js_list_total']")

    def click_upload_btn(self):
        return self.get_visible_element(self._upload_btn_loc).click()

    def click_confirm(self):
        return self.get_visible_element(self._confirm_btn_loc).click()

    # def upload_img(self,img_path):
    #     self.click_upload_btn()
    #     self.get_visible_element(self._upload_input_loc).send_keys(img_path)
    #     self.click_confirm()

    def upload_file(self, img_path):
        self.driver.execute_script("arguments[0].click();", self.get_visible_element(self._upload_btn_loc))
        self.get_presence_element(self._upload_input_loc).send_keys(img_path)

        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, ".js_uploadProgress_cancel"))
        )
        self.driver.execute_script("arguments[0].click();",
                                   self.get_visible_element(self._confirm_btn_loc))

    def get_img_amount(self):
        return self.get_visible_element(self._total_number_loc).text
