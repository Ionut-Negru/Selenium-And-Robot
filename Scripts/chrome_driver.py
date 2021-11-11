# chrome_driver.py
"""
    Contains the chrome automatic driving class.
    The class will open an instance of Chrome and take data from the browser
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


class ChromeDriver:
    
    browser = None
    def __init__(self):
        self.current_element = None
        self.driver_path = 'C:\\Users\\INegru\\Desktop\\chromedriver.exe'
        
    def load_driver(self, driver_path= ''):
        if driver_path == '':
            ChromeDriver.browser = Chrome(self.driver_path)
        else:
            ChromeDriver.browser = Chrome(driver_path)
        
    def open_browser(self, site_link=""):
        ChromeDriver.browser.get(site_link)
        
    def close_browser(self):
        ChromeDriver.browser.close()
        ChromeDriver.browser = None
        current_element = None
                
                
                