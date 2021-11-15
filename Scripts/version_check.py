from PythonLandingPage import PythonLandingPage
from PythonDownloadsPage import PythonDownloadsPage
import utils

if __name__ == '__main__':
    browser = PythonLandingPage()
    browser.open_page()
    browser.click_navigation_submenu_item('Downloads','All releases')
    browser = PythonDownloadsPage()
    browser.get_versions_table()
    browser.get_releases_table()
    print(browser.get_latest_version_date())
    print(browser.get_latest_release_date())