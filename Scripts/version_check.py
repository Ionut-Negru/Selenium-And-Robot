from PythonLandingPage import PythonLandingPage
from PythonDownloadsPage import PythonDownloadsPage
import utils

if __name__ == '__main__':
    browser = PythonLandingPage()
    browser.open_page()
    browser.click_navigation_submenu_item('Downloads','All releases')
    browser = PythonDownloadsPage()
    print(browser.get_latest_version_date())
    print(browser.get_latest_release_date())