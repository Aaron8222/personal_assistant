from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selectorlib import Extractor
from credentials.amazon_credentials import email, password, addresses, find_other_address, customer_emails
from send_email import send_message
import time
from bot_setup import driver_setup
from useful_selenium_functions import find_element_and_click, find_element_and_send_keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from google_sheets import get_google_form_data

def login(email, password, driver):
    driver.get('https://www.amazon.com/')
    find_element_and_click(By.LINK_TEXT, 'Sign in', driver)
    find_element_and_send_keys(By.ID, 'ap_email', email + Keys.ENTER, driver)
    find_element_and_send_keys(By.ID, 'ap_password', password + Keys.ENTER, driver)

def checkout(url, address, driver):
    driver.get(url)
    find_element_and_click(By.ID, 'buy-now-button', driver)
    #check_address(By.PARTIAL_LINK_TEXT, address, driver)

def check_address(path_type, address, driver):
    driver.switch_to.frame('turbo-checkout-iframe')
    if address != 'Olin': # Assumes Olin address is default
        current_selected_address = driver.find_element(path_type, addresses[find_other_address[address]])
        ActionChains(driver).move_to_element(current_selected_address).click().perform()
        correct_address = driver.find_element(path_type, addresses[address])
        ActionChains(driver).move_to_element(correct_address).click().perform()

def buy_item(buy_url, email, password, address):
    driver = driver_setup()
    driver.implicitly_wait(10)
    login(email, password, driver)
    checkout(buy_url, address, driver)
    time.sleep(5)
    driver.save_screenshot('temp/comfirmation_order1.png')
    #find_element_and_click(By.ID, 'turbo-checkout-pyo-button', driver)
    time.sleep(5)
    driver.save_screenshot('temp/comfirmation_order2.png')
    driver.switch_to.default_content()
    driver.close()

def check_google_sheet():
    while 1:
        data = get_google_form_data()
        if data is None:
            time.sleep(60)
        else:
            return data
    
def main():
    #while 1:
    date, name, link = check_google_sheet()
    buy_item(link, email, password, 'Home')
    send_message('6172857681@vzwpix.com','Amazon Confirmation',f'{name} has ordered something!',[r'temp\comfirmation_order1.png',r'temp\comfirmation_order2.png'])
    send_message(customer_emails[name],'Amazon Confirmation','Your item has been ordered!',[r'temp\comfirmation_order1.png',r'temp\comfirmation_order2.png'])