# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-04
 @Author:       吴润泽 
'''
import time
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import mylog
from common import contants


logger = mylog.get_logger("basepage")


class BasePage:

    def __init__(self, driver=None):
        if driver is None:
            self.driver = Chrome()
            self.driver.maximize_window()
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
            cookies = {
                "wwrtx.vst": "zenYAe4CxGbueq5ASVGKquiAk5PdPagPGzKHdLCVqT2i-M2L68XlyLV_-2tP7InD4kOpcBm"
                             "_stcX8b9Y9z6ec1BgEMdhR-FASZD-wSBX7D37_L7OFcsEYXUePdKC8sPqQBza3KieYk7TE9De"
                             "2a2AaILp3vEZTlaJMLwFDrOFjOBcFLvhY-k-VmX1gl-BGUklaeVgd8MBeY1ky3t4-2M0yiQlnA"
                             "7VWwRByLyJxlGrHgCrxZhOhs_BhvyJzLmJOoFNQvhrVSvzAXXoFdHs51gdxA",
                "wwrtx.d2st": "a4861364",
                "wwrtx.sid": "iAu-Z4L3xTLbZ5elezl0oXsd6Y-SXiveFjergOybpzZeb_7vPhAIpt8yVlOv0Ki1",
                "wwrtx.ltype": "1",
                "wxpay.corpid": "1688852500754167",
                "wxpay.vid": "1688852500754167",
            }

            for k, v in cookies.items():
                self.driver.add_cookie({"name": k, "value": v})
            self.driver.refresh()
        else:
            self.driver = driver

    def get_visible_element(self, locator, eqc=20) -> WebElement:
        '''
        定位元素，参数locator为元祖类型
        :param locator:
        :param eqc:
        :return:
        '''
        try:
            ele = WebDriverWait(self.driver, timeout=eqc).until(
                EC.visibility_of_element_located(locator))
            logger.info('获取{}元素成功'.format(locator))
            return ele
        except:
            logger.error("相对时间内没有定位到{}元素".format(locator))
            allure.attach(self.get_windows_img())

    def get_presence_element(self, locator, eqc=10):
        """
        定位一组元素
        :param locator:
        :param eqc:
        :return:
        """
        try:
            ele = WebDriverWait(self.driver, timeout=eqc).until(
                EC.presence_of_element_located(locator))
            logger.info('获取{}元素成功'.format(locator))
            return ele
        except:
            logger.error("相对时间内没有定位到{}元素".format(locator))
            allure.attach(self.get_windows_img())

    def get_clickable_element(self, locator, eqc=20):
        try:
            ele = WebDriverWait(self.driver, timeout=eqc).until(
            EC.element_to_be_clickable(locator))
            logger.info('获取{}元素成功'.format(locator))
            return ele
        except:
            logger.error("相对时间内没有定位到{}元素".format(locator))
            allure.attach(self.get_windows_img())

    def send_keys(self, locator, text):
        '''
        发送文本，清空后输入
        locator = ('id','xxx')
        element.send_keys(locator,text)
        '''

        element = self.get_visible_element(locator)
        element.clear()
        element.send_keys(text)
        logger.info('SendKeys %s in %s success.' % (text, locator))

    def is_text_in_element(self, locator, text, timeout=10):
        '''
        判断文本在元素里，没有元素返回false打印日志，定位到返回判断结果的布尔值
        result = driver.text_in_element(locator,text)
        '''

        try:
            result = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            logger.info('No location to the element.')
            allure.attach(self.get_windows_img())
            return False
        else:
            return result

    def is_text_in_value(self, locator, value, timeout=10):
        '''
        判断元素的value值，没定位到元素返回false，定位到返回判断结果布尔值
        result = dirver.text_to_be_present_in_element_value(locator,text)
        '''

        try:
            result = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            logger.info('No location to the element.')
            allure.attach(self.get_windows_img())
            return False
        else:
            return result

    def is_title(self, title, timeout=10):
        '''
        判断元素的title是否完全等于
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        '''
        判断元素的title是否包含
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.title_contains(title))
        return result

    def is_selected(self, locator, timeout=10):
        '''
        判断元素是否被选中
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self, locator, selected=True, timeout=10):
        '''
        判断元素的状态是不是符合期望的状态，selected是期望的状态
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.element_located_selection_state_to_be(locator, selected))
        return result

    def is_alert_present(self, timeout=10):
        '''
        判断页面是否有alert,有的话返回alert，没有返回False
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.alert_is_present())
        return result

    def is_visibility(self, locator, timeout=10):
        '''
        元素可见，返回本身，不可见返回False
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.visibility_of_element_located(locator))
        return result

    def is_invisibility(self, locator, timeout=10):
        '''
        元素可见返回本身，不可见返回Ture,没有找到元素也返回Ture
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.invisibility_of_element_located(locator))
        return result

    def is_clickable(self, locator, timeout=10):
        '''
        元素可以点击is_enabled返回本身，不可点击返回False
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self, locator, timeout=10):
        '''
        判断元素有没有被定位到(并不意味着可见),定位到返回element，没有定位到返回False
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.presence_of_all_elements_located(locator))
        return result

    def move_to_element(self, locator):
        '''
        鼠标悬停操作
        locator=('id','xxx')
        driver.move_to_element(locator)
        '''

        element = self.get_visible_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        # logger.info('ActionChins move to %s' % locator)

    def back(self):
        self.driver.back()

        logger.info('back driver!')

    def forward(self):
        self.driver.forward()

        logger.info('forward driver!')

    def close(self):
        self.driver.close()

        logger.info('close driver!')

    def refresh(self):
        return self.driver.refresh()

    def get_title(self):
        '''
        获取title
        '''

        logger.info('git dirver title.')
        return self.driver.title()

    def get_text(self, locator):
        '''
        获取文本
        '''

        element = self.get_visible_element(locator)
        # logger.info('get text in %s' % locator)
        text = element.text

        WebDriverWait(self.driver,10).until(EC.invisibility_of_element(locator))
        return text

    def get_attribute(self, locator, name):
        '''
        获取属性
        '''

        element = self.get_visible_element(locator)
        logger.info('get attribute in %s' % locator)
        return element.get_attribute(name)

    def js_execute(self, js):
        '''
        执行js
        '''

        try:
            logger.info('Execute js.%s' % js)
            return self.driver.execute_script(js)
        except:
            allure.attach(self.get_windows_img())
            logger.info('failed to excute js')

    def js_focus_element(self, locator):
        '''
        聚焦元素
        '''

        target = self.get_visible_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''
        滚动到顶部
        '''

        js = 'window.scrollTo(0,0)'
        self.js_execute(js)
        logger.info('Roll to the top!')

    def js_scroll_end(self):
        '''
        滚动到底部
        '''

        js = "window.scrollTo(0,document.body.scrollHight)"
        self.js_execute(js)
        logger.info('Roll to the end!')

    def get_windows_img(self):
        try:
            file_name = contants.screenshot_img
            self.driver.get_screenshot_as_file(file_name)
            logger.info('Had take screenshot and save to folder:output/screenshots')
        except NameError as e:
            logger.info('Failed to take the screenshot!%s' % e)
            self.get_windows_img()
        return file_name

    def switch_window(self, name=None, fqc=20):
        """
        切换窗口，有name切换至该name的窗口，没有则切换最新
        :param name:
        :param fqc:
        :return:
        """
        if name is None:
            current_handle = self.driver.current_window_handle
            WebDriverWait(self.driver, fqc).until(EC.new_window_is_opened(current_handle))
            handles = self.driver.window_handles
            return self.driver.switch_to.window(handles[-1])
        return self.driver.switch_to.window()