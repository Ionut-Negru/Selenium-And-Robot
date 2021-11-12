from PythonLandingPage import PythonLandingPage
from PythonDownloadsPage import PythonDownloadsPage
import utils

if __name__ == '__main__':
    browser = PythonLandingPage()
    browser.open_page()
    browser.click_navigation_submenu_item('Downloads','All releases')
    browser = PythonDownloadsPage()
    last_version = browser.get_row_from_versions_table(0)[0]
    print(last_version)
    found = browser.find_entry_in_column_in_releases_table('Release number',last_version)
    print(found)
    print(f'Latest release date : {browser.get_latest_release_date()}')
    print(f'Latest version date : {browser.get_latest_version_date()}')
    print(utils.compare_date(browser.get_latest_release_date(),browser.get_latest_version_date()))