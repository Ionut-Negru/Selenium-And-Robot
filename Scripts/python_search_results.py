from PythonSearchPage import PythonSearchPage
from PythonPEP318Page import PythonPEP318Page
from PythonLandingPage import PythonLandingPage

if __name__ == '__main__':
    
    browser = PythonLandingPage()
    browser.open_page()
    browser.search_on_page('decorator')
    
    browser = PythonSearchPage()
    browser.get_search_results()
    browser.select_result(0)
    browser = PythonPEP318Page()
    
    print(browser.get_number_of_examples())
    browser.close_browser()