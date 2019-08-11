# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-04
 @Author:       吴润泽 
'''
import time

import pytest, allure
from common.mylog import get_logger
from common.contants import img

logger = get_logger("test_img_manager")


@pytest.mark.usefixtures("hook4test_upload_img")
@allure.feature('企业微信测试')
class TestManagerImg():

    @allure.story('测试上传图片')
    def test_upload_img(self,hook4test_upload_img):

        with allure.step("进入管理页面"):
            img_manager_page = hook4test_upload_img

        with allure.step("获取当前页面图片张数"):
            time.sleep(2)
            before = img_manager_page.get_img_amount()

        with allure.step("上传图片"):
            img_manager_page.upload_file(img)

        with allure.step("再次获取页面图片张数"):
            time.sleep(2)
            after = img_manager_page.get_img_amount()

        with allure.step("断言开始"):
            try:
                assert int(before) + 1 == int(after)
                logger.info("上传图片用例执行成功")
            except AssertionError as e:
                logger.error("用例执行失败")
                allure.attach(img_manager_page.get_windows_img())
                raise e


if __name__ == '__main__':
    pytest.main()