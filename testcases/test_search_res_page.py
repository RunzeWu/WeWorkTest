# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-04
 @Author:       吴润泽 
'''
import logging
import pytest, allure
from common.mylog import get_logger
from pages.search_res_page import SearchResultPage

logger = get_logger("test_add_member")
search_page = SearchResultPage()


@allure.feature("企业微信测试")
class TestWeworkSearchMember():

    @allure.story("测试编辑成名员")
    def test_edit_member(self):
        with allure.step("搜索成员"):
            search_page.search_member('雷浩')
        logging.info("搜索成员操作成功")

        with allure.step("点击编辑"):
            search_page.click_edit()
        logging.info("{}操作成功".format(search_page._edit_loc))

        with allure.step("点击保存按钮"):
            search_page.click_save()
        logging.info("{}操作成功".format(search_page._save_loc))

        with allure.step("断言判断"):
            try:
                assert search_page.get_toast() == "保存成功"
                logging.info("编辑成员用例测试成功")
            except AssertionError as e:
                logging.error("添加成员用例测试失败")
                allure.attach(search_page.get_windows_img())
                raise e


if __name__ == '__main__':
    pytest.main()