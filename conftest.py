# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-04
 @Author:       吴润泽 
'''

import pytest
from selenium import webdriver


@pytest.fixture('class')
def init_driver():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    cookies = {
                "wwrtx.vst": "vYBqdcvXYVduy7fJ6JfHYDPdgLlonrvyDwLwvcrn5JDhlR"
                             "53RH2DqQ2SsTuxyVv7GH1Ltiq09EDy_2MQ9dyR8j1AHKjdgKgoUlP"
                             "0_z7xBeupOCNCOc-2t_CfHeAFSrz9m9Rz8eS73HNBHiyO9kobqc"
                             "jk5D6t0xdxfx-BMlkCheEdDXd8qLT3neohv0n6oghLKoO_2V9UD18fOrgmuqZvbMIV"
                             "KAc7nxN5H6OE26wTx8ozWmo_l-I7N8tFXdiEcSi0QwOXUiuq3FduOqDOU4nI_w",
                "wwrtx.d2st": "a351283",
                "wwrtx.sid": "iAu-Z4L3xTLbZ5elezl0oUHVzVXFUSTLVvKWG_yn3OeIPevhS5M7xv0Cqv9pSQku",
                "wwrtx.ltype": "1",
                "wxpay.corpid": "1688852500754167",
                "wxpay.vid": "1688852500754167",
            }

    for k, v in cookies.items():
        driver.add_cookie({"name":k, "value":v})
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    driver.refresh()
    yield driver
    driver.close()

init_driver()