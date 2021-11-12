from PythonLandingPage import PythonLandingPage
from PythonDownloadsPage import PythonDownloadsPage


if __name__ == '__main__':
    browser = PythonLandingPage()
    browser.open_page()
    browser.click_navigation_submenu_item('Downloads','All releases')
    browser = PythonDownloadsPage()
    browser.get_table_from_elements()
    print(browser.get_data_from_table(0,"Python version"))
    
