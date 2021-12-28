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
from bot_setup import driver_setup
import pyautogui
from PIL import Image, ImageEnhance


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
    #driver.find_element(By.LINK_TEXT, r'登录').click()
    time.sleep(3)
    screenshot(driver)
    verification_code = verify_code(driver)
    #driver.find_element(By.NAME, 'seccodeverify').click()
    driver.find_element(By.NAME, 'seccodeverify').send_keys(verification_code)    
    driver.implicitly_wait(wait_time)

def verify_code(driver):
    screenshot(driver)
    crop_image(r'temp\bot_verify.png')
    return image_to_text(r'temp\bot_verify_processed.png')

def screenshot(driver):
    driver.save_screenshot(r'temp\bot_verify.png')
    #myScreenshot = pyautogui.screenshot()
    #myScreenshot.save(r'temp\bot_verify.png')

def crop_image(image):
    im = Image.open(image)
    
    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size
    
    # Setting the points for cropped image
    left = 776
    top = 526
    right = 926
    bottom = 571
    
    return im.crop((left, top, right, bottom))

    imt.save(r'temp\bot_verify_processed.png')


def increase_contrast(image):
    im1 = image.crop((left, top, right, bottom))
    enhancer = ImageEnhance.Contrast(im1)
    factor = 3 #increase contrast
    return enhancer.enhance(factor)

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
    pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image = cv2.imread(img)	
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('hi',gray)
    #cv2.waitKey(0)
    return pytesseract.image_to_string(image)


def main():
    driver = driver_setup()
    ad_title = 'test'
    ad_message = 'test2'
    """
    login_shen(shen_username, shen_password, driver)
    rent_shen(ad_title, ad_message, driver)
    """

    login_bbs(bbs_username, bbs_password, driver)
    time.sleep(999)

#main()
crop_image(r'temp\bot_verify.png')
print(image_to_text(r'temp\bot_verify_processed.png'))