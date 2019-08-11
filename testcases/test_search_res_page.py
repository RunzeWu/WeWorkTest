# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-04
 @Author:       吴润泽 
'''
import logging
import pytest, allure
from common.mylog import get_logger

logger = get_logger("test_add_member")


@allure.feature("企业微信测试")
@pytest.mark.usefixtures("hook4test_search_edit")
class TestWeworkSearchMember():

    @allure.story("测试编辑成名员")
    def test_edit_member(self,hook4test_search_edit):
        search_page = hook4test_search_edit
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

    @allure.story("测试禁用成员")
    def test_disable_member(self,hook4test_search_edit):
        search_page = hook4test_search_edit
        with allure.step("搜索成员"):
            search_page.search_member('雷浩')
        logging.info("搜索成员操作成功")

        with allure.step("判断成员状态"):
            text = search_page.get_text(search_page._disable_loc)
            if text == "禁用":
                flag = True
            else:
                flag = False

        if flag:
            with allure.step("点击禁用"):
                search_page.click_disable()
            logging.info("{}操作成功".format(search_page._disable_loc))

            with allure.step("点击确认按钮"):
                search_page.click_confirm()
            logging.info("{}操作成功".format(search_page._confirm_btn_loc))

            with allure.step("断言判断"):
                try:
                    assert search_page.get_toast() == "禁用成功"
                    logging.info("编辑成员用例测试成功")
                except AssertionError as e:
                    logging.error("添加成员用例测试失败")
                    allure.attach(search_page.get_windows_img())
                    raise e
        else:
            logger.info("已经是禁用状态")

    @allure.story("测试启用成员")
    def test_able_member(self,hook4test_search_edit):
        search_page = hook4test_search_edit
        with allure.step("搜索成员"):
            search_page.search_member('雷浩')
        logging.info("搜索成员操作成功")

        with allure.step("判断成员状态"):
            text = search_page.get_text(search_page._disable_loc)
            if text == "启用":
                flag = True
            else:
                flag = False

        if flag:
            with allure.step("点击启用"):
                search_page.click_disable()
            logging.info("{}操作成功".format(search_page._disable_loc))

            with allure.step("断言判断"):
                try:
                    assert search_page.get_toast() == "启用成功"
                    logging.info("编辑成员用例测试成功")
                except AssertionError as e:
                    logging.error("添加成员用例测试失败")
                    allure.attach(search_page.get_windows_img())
                    raise e
        else:
            logger.info("已经是启用状态")


if __name__ == '__main__':
    pytest.main()