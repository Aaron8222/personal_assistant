from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth


def driver_setup():
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, \
      like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    s = Service('chromedriver/undetected_chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument(f'user-agent={user_agent}')
    #options.add_argument('headless')
    driver = webdriver.Chrome(service=s, options=options)
    stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
    )
    return driver