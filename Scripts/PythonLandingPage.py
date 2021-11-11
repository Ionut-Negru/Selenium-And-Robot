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
        ChromeDriver.__init__(self)
        self.navigation_menu = {}
        
    def open_page(self):
        """
            This method will open a new browser on the landing page of the python.org website 
        """
        self.load_driver()
        self.open_browser("http:\\python.org")
        self.load_navigation_menu()
        
    def load_navigation_menu(self):
        self.current_element = self.browser.find_elements_by_xpath("//nav[@id='mainnav']/ul[@class='navigation menu']/li")
        for x in self.current_element:
            self.navigation_menu[x.text] = x
    
    def click_navigation_menu_button(self, option=""):
        self.current_element = self.navigation_menu[option]
        self.current_element.click() 
    
    def hover_on_navigation_menu_item(self, option=""):
        self.current_element = self.navigation_menu[option]
        action = ActionChains(self.browser).move_to_element(self.current_element)
        action.perform()
        
    def get_search_bar(self):
        return self.browser.find_element_by_xpath("//input[@id='id-search-field']")
        
    def search_on_page(self, search_querry=''):
        self.current_element = self.get_search_bar()
        self.current_element.send_keys(search_querry)
        self.current_element.send_keys(Keys.ENTER)

    def click_navigation_submenu_button(self, menu='', submenu=''):
        self.hover_on_navigation_menu_item(menu)
        self.current_element = self.browser.find_elements_by_xpath(f"//nav[@id='mainnav']/ul[@class='navigation menu']/li[@id='{menu.lower().replace(' ','-')}']/ul[@class='subnav menu']/li")
        
        for item in self.current_element:
            if item.text == submenu:
                item.click()
                break
    
    def close_landing_page(self):
        self.close_browser()
        