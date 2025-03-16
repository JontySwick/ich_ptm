from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC

import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.close()


def test_iframe(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    iframe = driver.find_element(By.ID, 'my-iframe')
    driver.switch_to.frame(iframe)

    assert WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((
            By.XPATH,
            "//p[contains(normalize-space(), 'semper posuere integer et senectus justo curabitur.')]"
        ))
    ).is_displayed()


def test_drag_and_drop(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    iframe = driver.find_element(By.CSS_SELECTOR, '[data-src="../../demoSite/practice/droppable/photo-manager.html"]')
    driver.switch_to.frame(iframe)

    drag = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#gallery li:nth-child(1)")))
    drop = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "trash")))

    ActionChains(driver).drag_and_drop(drag, drop).perform()

    sleep(1)

    assert len(driver.find_elements(By.CSS_SELECTOR, '#gallery li')) == 3
    assert len(driver.find_elements(By.CSS_SELECTOR, '#trash li')) == 1
