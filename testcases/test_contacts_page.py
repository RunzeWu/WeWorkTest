# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-04
 @Author:       吴润泽 
'''
import logging
import pytest, allure
from faker import Faker
from common.mylog import get_logger
from pages.contacts_page import ContactsPage

logger = get_logger("test_add_member")
contact_page = ContactsPage()


@allure.feature("企业微信测试")
class TestWeworkAddMember():

    @allure.story("测试添加成员")
    def test_add_member(self):
        self.f = Faker(locale='zh_CN')
        self.fakename = self.f.name()
        self.fake_id = self.f.ssn()
        self.fake_mobile = self.f.phone_number()
        # 2
        with allure.step("点击添加按钮"):
            contact_page.click_add_btn()
        logging.info("{}操作成功".format(ContactsPage._add_member_btn_locator))
        # 3
        with allure.step("输入用户名"):
            contact_page.input_info(self.fakename,self.fake_id,self.fake_mobile)
        logging.info("{}操作成功".format(ContactsPage._memberAdd_phone_locator))
        # 6
        with allure.step("点击保存按钮"):
            contact_page.submit_info()
        logging.info("{}操作成功".format(ContactsPage._save_btn_locator))

        with allure.step("断言判断"):
            try:
                assert self.fakename,self.fake_mobile in self.driver.page_source
                logging.info("添加成员用例测试成功")
            except AssertionError as e:
                logging.error("添加成员用例测试失败")
                contact_page.get_windows_img()
                raise e


if __name__ == '__main__':
    pytest.main()