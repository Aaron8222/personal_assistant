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
import urllib


def get_url(url, driver, wait_time=10):
    driver.get(url)
    driver.implicitly_wait(wait_time)

def login_shen(email, password, driver, wait_time=10):
    get_url('https://www.shenghuonet.com/phpBB2/index.php', driver)
    driver.find_element(By.XPATH, '/html/body/center/div[1]/div[2]/a[2]/font/font').click()
    driver.find_element(By.XPATH, '/html/body/center/div[4]/div[1]/section[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').click()
    driver.find_element(By.XPATH, '/html/body/center/div[4]/div[1]/section[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').send_keys(email)
    driver.implicitly_wait(wait_time)
    driver.find_element(By.ID, '/html/body/center/div[4]/div[1]/section[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').click()
    driver.find_element(By.ID, '/html/body/center/div[4]/div[1]/section[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').send_keys(password + Keys.ENTER)
    driver.implicitly_wait(wait_time)

def rent_shen(ad_title, ad_message, driver)
    get_url('https://www.shenghuonet.com/phpBB2/topicclass.php?tc=3&showdate=1', driver)
    driver.find_element(By.XPATH, '//*[@id="leftcontent"]/div[1]/font/a/font/font').click()
    driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/section[2]/div/form/section/div[2]/div[2]/input').send_keys(ad_title)
    driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/section[2]/div/form/section/div[4]/div[2]/textarea').send_keys(ad_message)
    #Uncomment when ready
    #driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/section[2]/div/form/section/div[5]/button[1]/font/font').click()


def login_bbs(email, password, driver, wait_time=10):
    get_url('http://bbs.bostonstudents.org/forum-40-1.html', driver)
    driver.find_element(By.XPATH, '//*[@id="headnav"]/div/div[2]/ul/li[1]/a').click()
    driver.find_element(By.XPATH, '//*[@id="username_LbZ85"]').click()
    driver.find_element(By.XPATH, '//*[@id="username_LbZ85"]').send_keys(email)
    driver.implicitly_wait(wait_time)
    driver.find_element(By.XPATH, '//*[@id="password3_LbZ85"]').click()
    driver.find_element(By.XPATH, '//*[@id="password3_LbZ85"]').send_keys(password + Keys.ENTER)
    driver.implicitly_wait(wait_time)

def verify_code(driver):
    # get the image source
    img = driver.find_element_by_xpath('//div[@id="recaptcha_image"]/img')
    src = img.get_attribute('src')

    # download the image
    urllib.urlretrieve(src, "captcha.png")


def main():
    s = Service('chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s, options=options)
    login_shen()