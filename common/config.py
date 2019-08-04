# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-04
 @Author:       吴润泽
'''
import configparser
from common import contants


class ReadConfig:
    def __init__(self):

        self.cf = configparser.ConfigParser()
        self.cf.read(contants.conf_file, encoding="utf-8")

    def get_value(self, section, option):
        return self.cf.get(section, option)

    def get_int(self, section, option):
        return self.cf.getint(section, option)

    def get_float(self, section, option):
        return self.cf.getfloat(section, option)

    def get_boolen(self, section, option):
        return self.cf.getfloat(section, option)


if __name__ == '__main__':
    A = ReadConfig()
    print(A.get_value('log', "formatter"))
