# PythonLangingPage.py
"""
    This file contains the PythonLangingPage class
    The class will perform actions on the landing page of "https://python.org
"""
from chrome_driver import *
from selenium.webdriver.common.action_chains import *

class PythonLandingPage(ChromeDriver):
    
    def __init__(self):
        """            Initialize the attributes of the class
            
            Attributes:
                navigation_menu - this attribute is a dictionary containing the elements of the navigation menu of the site
                search_bar - this attribute is a webElement that represents the search bar of the site
        """
        super().__init__()
        self.navigation_menu = {}
        
    def open_page(self):
        """
            This method will open a new browser on the landing page of the python.org website 
        """
        self.load_driver()
        self.open_browser("http:\\python.org")
    
    def click_navigation_menu_item(self, option=''):    
        self.get_navigation_menu_item(option).click() 
    
    def hover_navigation_menu_item(self, option=''):
        action = ActionChains(ChromeDriver.browser).move_to_element(self.get_navigation_menu_item(option))
        action.perform()
    
    def get_navigation_menu_item(self, option=""):
        return self.browser.find_element_by_xpath(f"//div[@class='container']/nav[@id='mainnav']/ul[@class='navigation menu']/li[@id='{option.lower().replace(' ','-')}']")

    def get_search_bar(self):
        return self.browser.find_element_by_xpath("//input[@id='id-search-field']")
        
    def search_on_page(self, search_querry=''):
        self.current_element = self.get_search_bar()
        self.current_element.send_keys(search_querry)
        self.current_element.send_keys(Keys.ENTER)

    def click_navigation_submenu_item(self, menu='', submenu=''):
        self.hover_navigation_menu_item(menu)
        self.current_element = self.browser.find_element_by_xpath(f"//nav[@id='mainnav']/ul[@class='navigation menu']/li[@id='{menu.lower().replace(' ','-')}']/ul[@class='subnav menu']/li/a[contains(text(),'{submenu}')]")
        self.current_element.click()
    
    def close_browser(self):
        ChromeDriver.browser.close()
        ChromeDriver.browser = None
        self.current_element = None
        
        