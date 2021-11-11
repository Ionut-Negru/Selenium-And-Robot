from PythonLandingPage import PythonLandingPage
from PythonDownloadsPage import PythonDownloadsPage


if __name__ == '__main__':
    browser = PythonLandingPage()
    browser.open_page()
    browser.click_navigation_submenu_button(menu='Downloads',submenu='All releases')
    browser = PythonDownloadsPage()
    browser.get_table_from_elements()
    print(browser.get_data_from_table(row=0,column_name='Python version'))
    browser.close_browser()