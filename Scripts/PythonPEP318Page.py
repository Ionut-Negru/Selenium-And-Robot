from chrome_driver import ChromeDriver

class PythonPEP318Page(ChromeDriver):
    
    def __init__(self):
        super().__init__()
        self.browser = ChromeDriver.browser
        
    def get_number_of_examples(self):
        self.current_element = self.browser.find_elements_by_xpath("//div[@id='examples']/ol[@class='arabic']/li")
        return str(len(self.current_element))
    
