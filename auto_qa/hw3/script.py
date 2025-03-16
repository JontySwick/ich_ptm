from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.close()


def test_index_page(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(2)
    header = driver.find_element(By.ID, 'rec717843722')

    logo = header.find_element(
        By.CSS_SELECTOR,
        '[data-original="https://static.tildacdn.net/tild3333-3534-4535-a465-643634653734/Group_3793.svg"]'
    )
    assert logo.is_displayed()

    assert header.find_element(By.LINK_TEXT, "Программы")
    assert header.find_element(By.LINK_TEXT, "Способы оплаты")
    assert header.find_element(By.LINK_TEXT, "Новости")
    assert header.find_element(By.LINK_TEXT, "О нас")
    assert header.find_element(By.LINK_TEXT, "Отзывы")

    assert header.find_element(By.LINK_TEXT, "ru")
    assert header.find_element(By.LINK_TEXT, "de")

    header.find_element(By.CSS_SELECTOR, '[href="#popup:form-tr3"] img').click()

    popup_text = driver.find_element(By.CSS_SELECTOR, '.t-popup_show [data-elem-type="text"] div')

    assert popup_text.is_displayed() and popup_text.text == "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"