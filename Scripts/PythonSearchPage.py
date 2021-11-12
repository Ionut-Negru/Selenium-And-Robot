from chrome_driver import ChromeDriver


class PythonSearchPage(ChromeDriver):
    
    def __init__(self):
        super().__init__()
        self.browser = ChromeDriver.browser
        self.search_results = {}
        
    def get_search_results(self):
        self.current_element = self.browser.find_elements_by_xpath("//section[@class='main-content ']/form/ul[@class='list-recent-events menu']/li/h3/a")
        
        for result in self.current_element:
            self.search_results[result.text] = result
    
    def select_result(self, index=0):
        i = 0
        for result in self.search_results:
            if i == index:
                self.search_results[result].click()
                break
            else:
                i = i + 1
                
    
    