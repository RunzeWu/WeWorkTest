# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-04
 @Author:       吴润泽 
'''
import os
import time
# from common.config import ReadConfig

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根路径

data_dir = os.path.join(base_dir, "data")  # data文件夹路径

conf_dir = os.path.join(base_dir, "conf")
conf_file = os.path.join(conf_dir, "conf.ini")  # 环境配置文件路径

# 日志路径
output_dir = os.path.join(base_dir, "output")
allure_dir = os.path.join(base_dir,"output","allure")
log_time = time.strftime('%Y-%m-%d')
logs_log = os.path.join(output_dir, log_time + ".log")

# 截图路径
screenshot_img = os.path.join(output_dir, "screenshots", str(int(time.time()))+".png")

# case 路径
case_dir = os.path.join(base_dir, "testcase")

# 图片路径
img = os.path.join(base_dir, "images", "timg.jpeg")
print(img)

