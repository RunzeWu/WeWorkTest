# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-04
 @Author:       吴润泽 
'''

import pytest
from pages.contacts_page import ContactsPage
from pages.search_res_page import SearchResultPage
from pages.manage_tools_page import ManageToolsPage
from pages.manage_photo_page import ImageManagerPage


@pytest.fixture(scope='class')
def hook4test_contact():
    contact_page = ContactsPage()
    yield contact_page
    contact_page.close()


@pytest.fixture(scope='class')
def hook4test_search_edit():
    search_page = SearchResultPage()
    yield search_page
    search_page.close()


@pytest.fixture(scope="class")
def hook4test_upload_img():
    manager_page = ManageToolsPage()
    manager_page.goto_manager_img()
    driver = manager_page.driver
    img_manager_page = ImageManagerPage(driver=driver)
    yield img_manager_page
    img_manager_page.close()