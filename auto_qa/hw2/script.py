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


def test_payment_methods_section(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(2)
    payment_methods_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_methods_link.click()
    sleep(2)
    driver.save_screenshot("./payment_methods_section_screenshot.png")
