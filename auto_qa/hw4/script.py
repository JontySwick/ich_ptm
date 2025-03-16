from selenium import webdriver
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


def test_change_button(driver):
    driver.get("http://uitestingplayground.com/textinput")
    wait_driver = WebDriverWait(driver, 20)
    new_button_name = 'ITCH'
    input_element = wait_driver.until(EC.presence_of_element_located((By.ID, 'newButtonName')))
    input_element.send_keys(new_button_name)

    button_element = driver.find_element(By.ID, 'updatingButton')
    button_element.click()

    assert button_element.text == new_button_name


def test_load_img(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    wait_driver = WebDriverWait(driver, 20)
    wait_driver.until(EC.presence_of_element_located((By.ID, 'spinner')))
    wait_driver.until_not(EC.presence_of_element_located((By.ID, 'spinner')))

    assert driver.find_element(By.CSS_SELECTOR, '#image-container img:nth-child(3)').get_attribute('alt') == 'award'
