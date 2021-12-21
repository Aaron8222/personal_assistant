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
import cv2
import pytesseract
import numpy as np
from credentials.rent_credentials import shen_username, shen_password, bbs_username, bbs_password


def get_url(url, driver, wait_time=10):
    driver.get(url)
    driver.implicitly_wait(wait_time)

def login_shen(username, password, driver, wait_time=10):
    get_url('https://www.shenghuonet.com/phpBB2/index.php', driver)
    driver.find_element(By.LINK_TEXT, r'登陆').click()
    driver.find_element(By.XPATH, '/html/body/center/div[4]/div[1]/section[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').click()
    driver.find_element(By.XPATH, '/html/body/center/div[4]/div[1]/section[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').send_keys(username)
    driver.implicitly_wait(wait_time)
    driver.find_element(By.XPATH, '/html/body/center/div[4]/div[1]/section[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').click()
    driver.find_element(By.XPATH, '/html/body/center/div[4]/div[1]/section[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').send_keys(password + Keys.ENTER)
    driver.implicitly_wait(wait_time)

def rent_shen(ad_title, ad_message, driver):
    get_url('https://www.shenghuonet.com/phpBB2/topicclass.php?tc=3&showdate=1', driver)
    driver.find_element(By.LINK_TEXT, '发表新帖').click()
    driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/section[2]/div/form/section/div[2]/div[2]/input').send_keys(ad_title)
    driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/section[2]/div/form/section/div[4]/div[2]/textarea').send_keys(ad_message)
    #Uncomment when ready
    #driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/section[2]/div/form/section/div[5]/button[1]/font/font').click()


def login_bbs(username, password, driver, wait_time=10):
    get_url('http://bbs.bostonstudents.org/forum-40-1.html', driver)
    driver.find_element(By.LINK_TEXT, r'登录').click()
    driver.implicitly_wait(wait_time)
    list = driver.find_elements(By.CLASS_NAME, 'p_fre')
    list[0].send_keys(username) # username
    list[1].send_keys(password) # password

    #verification_code = verify_code(driver)
    verification_code = verify_code(driver)
    driver.find_element(By.NAME, 'seccodeverify').click()
    driver.find_element(By.NAME, 'seccodeverify').send_keys(verification_code)    
    driver.implicitly_wait(wait_time)

def verify_code(driver):
    screenshot(driver)
    time.sleep(3)
    return image_to_text('human_verification.png')

def screenshot(driver):
    driver.save_screenshot('human_verification.png')

"""
def verify_code(driver):
    # get the image source
    list = driver.find_elements(By.CLASS_NAME, 'vm')
    print(list)
    src = list[2].get_attribute('src')
    print(src)
    urllib.request.urlretrieve(src, "captcha.png")
    image_to_text('captcha.png')
"""

def image_to_text(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    gray = cv2.bitwise_not(img_bin)
    kernel = np.ones((2, 1), np.uint8)
    img = cv2.erode(gray, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)
    return pytesseract.image_to_string(img)

def main():
    s = Service('chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s, options=options)
    ad_title = 'test'
    ad_message = 'test2'
    """
    login_shen(shen_username, shen_password, driver)
    rent_shen(ad_title, ad_message, driver)
    """

    #login_bbs(bbs_username, bbs_password, driver)
    time.sleep(999)

main()