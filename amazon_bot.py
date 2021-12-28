from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selectorlib import Extractor
from credentials.amazon_credentials import email, password
import requests
import json
import time
from bot_setup import driver_setup


def get_url(url, driver, wait_time=10):
    driver.get(url)
    driver.implicitly_wait(wait_time)

def login(email, password, driver, wait_time=10):
    get_url('https://www.amazon.com/', driver)
    driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[3]/div[10]/div[2]/a/span').click()
    driver.find_element(By.ID, 'ap_email').click()
    driver.find_element(By.ID, 'ap_email').send_keys(email + Keys.ENTER)
    driver.implicitly_wait(wait_time)
    driver.find_element(By.ID, 'ap_password').click()
    driver.find_element(By.ID, 'ap_password').send_keys(password + Keys.ENTER)
    #driver.implicitly_wait(wait_time)
    time.sleep(10)

def buy_now_button(url, driver, wait_time=10):
    get_url(url, driver)
    driver.implicitly_wait(wait_time)
    driver.find_element(By.ID, 'buy-now-button').click()
    driver.implicitly_wait(wait_time)
    # make sure address is right
    # Only uncomment when ready to put into production!
    # driver.find_element_by_id('turbo-checkout-pyo-button')

def buy_item(buy_url, email, password):
    driver = driver_setup()
    login(email, password, driver)
    buy_now_button(buy_url, driver)


url = r'https://www.amazon.com/Alexander-Del-Rossa-Bathrobe-A0125STLXL/dp/B00CHQ5LCM?ref_=Oct_DLandingS_D_a94574e1_61&smid=A1G65SAYOU9XNS&th=1&psc=1'
buy_item(url, email, password)