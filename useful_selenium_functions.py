from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
import time

def find_element_and_send_keys(path_type, path, keys, driver, wait_time=10):
    #WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((path_type, path)))
    driver.find_element(path_type, path).send_keys(keys)
    random_wait_time()

def find_element_and_click(path_type, path, driver, wait_time=10):
    #WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((path_type, path)))
    driver.find_element(path_type, path).click()
    random_wait_time()

def random_wait_time(min_value=1, max_value=5):
    value = randint(min_value, max_value)
    time.sleep(value)


