# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-04
 @Author:       吴润泽 
'''

import pytest
from selenium import webdriver


# @pytest.fixture('class')
# def init_driver():
#     driver = webdriver.Chrome()
#     driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
#     cookies = {
#                 "wwrtx.vst": "nkpa9GMRJb6IXY6QocvU2OCjBFr7PI5sz3zuvHK0pZ8s7wbAiDq-N1cnID5Yk0_Mf"
#                              "NV0tDDf1WKce2HpKYXvNrRCq-QjITOhvc51vTnUEqtKOXiMHg72N2iVw3daxMQuaauueGic_L"
#                              "W-pSDyJok7UBVoV-AVXSxEqpsdQY4PCpVP420niA3-ch8a-kuWrTcHK4EHelLXzqBOVbifiS2Lc8"
#                              "QxRGEp0KGK5G1DkplM7-OnQgXKnLAYUWEDHB18C9yQKorJ5Hr1iT8FTQ_-Dr4hmg",
#                 "wwrtx.d2st": "a529674",
#                 "wwrtx.sid": "iAu-Z4L3xTLbZ5elezl0ob3iKrITG1_B-kEmKk-t_jXqIXEDcOM0WOGfH03WdFKb",
#                 "wwrtx.ltype": "1",
#                 "wxpay.corpid": "1688852500754167",
#                 "wxpay.vid": "1688852500754167",
#             }
#
#     for k, v in cookies.items():
#         driver.add_cookie({"name":k, "value":v})
#     driver.get("https://work.weixin.qq.com/wework_admin/frame")
#     driver.refresh()
#     yield driver
    # driver.close()