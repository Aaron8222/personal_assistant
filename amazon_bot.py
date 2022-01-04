from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selectorlib import Extractor
from credentials.amazon_credentials import email, password
import requests
import json
import time
from bot_setup import driver_setup
from useful_selenium_functions import find_element_and_click, find_element_and_send_keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(email, password, driver):
    driver.get('https://www.amazon.com/')
    find_element_and_click(By.XPATH, '/html/body/div[1]/header/div/div[3]/div[10]/div[2]/a/span', driver)
    find_element_and_send_keys(By.ID, 'ap_email', email + Keys.ENTER, driver)
    find_element_and_send_keys(By.ID, 'ap_password', password + Keys.ENTER, driver)

def checkout(url, address, driver):
    driver.get(url)
    find_element_and_click(By.ID, 'buy-now-button', driver)
    check_address(By.PARTIAL_LINK_TEXT, address, driver)
    time.sleep(999)
    # find_element_and_click(By.ID, 'turbo-checkout-pyo-button', driver)

def check_address(path_type, path, driver):
    try:
        EC.presence_of_element_located((path_type, path))
    except TimeoutException:
        find_element_and_click(By.LINK_TEXT, 'Ship to', driver)
        find_element_and_click(By.PARTIAL_LINK_TEXT, path, driver)

def buy_item(buy_url, email, password, address):
    driver = driver_setup()
    login(email, password, driver)
    checkout(buy_url, address, driver)


url = r'https://www.amazon.com/Waterproof-Electric-Vehicles-Batteries-Excellent/dp/B08JZBZCXN?ref=dlx_deals_gd_dcl_tlt_47_bdd093a3_dt_sl15_c9&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyME9OQzU1VVFGSVNCJmVuY3J5cHRlZElkPUEwNzU1MDMwMUIxUEJEWTcyTzhaQSZlbmNyeXB0ZWRBZElkPUEwOTI0NDA1S1JSWVhPSjdJR083JndpZGdldE5hbWU9c3BfZ2JfbWFpbl9zdXBwbGUmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
buy_item(url, email, password, '69 APPLETON STREET')