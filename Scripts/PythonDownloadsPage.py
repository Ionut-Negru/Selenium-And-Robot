# PythonDownloadPage.py

from chrome_driver import ChromeDriver
import datetime


class PythonDownloadsPage(ChromeDriver):
    
    def __init__(self):
        super().__init__()
        self.browser = ChromeDriver.browser
        
    def find_entry_in_releases_table(self, row=0, column_name='', to_be_found=''):
        """
            For row the value 0 represents the first row of the table
            Options for column_name:
                - Release number - the python version
                - Release date   - the date of the release
                - Release enhancements - button to see the release notes of the specified release
        """
        self.current_element = self.browser.find_elements_by_xpath("//section[@class='main-content ']/div[@class='row download-list-widget']" \
                                                                   +"/ol[@class='list-row-container menu']/" \
                                                                   +f"li[{row+1}]/span[@class='{column_name.lower().replace(' ','-')}']" \
                                                                   +f"/a[contains(text(),'{to_be_found}')]")
        if len(self.current_element) > 0:
            return True
        else:
            return False
        
    def get_data_from_releases_table(self, row=0, column_name=''):
        """
            This method will return the value present at the given row and column name 
            For row the value 0 represents the first row of the table
            Options for column_name:
                - Release number - the python version
                - Release date   - the date of the release
                - Release enhancements - button to see the release notes of the specified release
        """
        self.current_element = self.browser.find_element_by_xpath("//section[@class='main-content ']/div[@class='row download-list-widget']" \
                                                                   +"/ol[@class='list-row-container menu']/" \
                                                                   +f"li[{row+1}]/span[@class='{column_name.lower().replace(' ','-')}']/a")
        return self.current_element.text
               
    def get_data_from_versions_table(self, row=0, column_name=''):
        """
            For row the value 0 represents the first row of the table
            Options for column_name:
                - Release version - the python version of the row
                - Release status - the current status of the python version (bugfix, end-of-life, security , etc)
                - Release start - the release date of the version
                - Release end - the support end date of the version
                - Release PEP - the PEP released with the version
                
        """  
        self.current_element = self.browser.find_element_by_xpath("//section[@class='main-content ']/div[@class='row active-release-list-widget']/ol[@class='list-row-container menu']" \
                                                                  +f"/li[{row+1}]/span[@class='{column_name.lower().replace(' ','-')}']")
        return self.current_element.text
    
    def find_entry_in_versions_table(self, row=0, column_name='', to_be_found=''):
        """
            For row the value 0 represents the first row of the table
            Options for column_name:
                - Release version - the python version of the row
                - Release status - the current status of the python version (bugfix, end-of-life, security , etc)
                - Release start - the release date of the version
                - Release end - the support end date of the version
                - Release PEP - the PEP released with the version
            
            to_be_found - the string we are looking for in a specific column    
        """  
        self.current_element = self.browser.find_elements_by_xpath("//section[@class='main-content']/div[@class='row active-release-list-widget']/ol[@class='list-row-container menu']" \
                                                                   +f"/li[{row+1}]" \
                                                                   +f"/span[@class='{column_name.lower().replace(' ','-')}' and contains(text(),'{to_be_found}')]")
        if len(self.current_element) > 0:
            return True
        else:
            return False
    
    def find_entry_in_column_in_releases_table(self, column_name, to_be_found):
        """
            
            Options for column_name:
                - Release number - the python version
                - Release date   - the date of the release
                - Release enhancements - button to see the release notes of the specified release
            
            to_be_found - the string searched inside the column
        """
        self.current_element = self.browser.find_elements_by_xpath("//section[@class='main-content ']/div[@class='row download-list-widget']/ol[@class='list-row-container menu']/li"\
                                                                   +f"/span[@class='{column_name.lower().replace(' ','-')}']/a[contains(text(),'{to_be_found}')]")
        if len(self.current_element) > 0:
            return True
        else:
            return False
        
    def get_row_from_versions_table(self, row=0):
        """
            Return a list of strings of the specified row of the versions table. 0 is the first row of the table
            The list will have the format : [Release version, Release status, Release start, Release end, Release PEP]
        """
        self.current_element = self.browser.find_elements_by_xpath("//section[@class='main-content ']/div[@class='row active-release-list-widget']/ol[@class='list-row-container menu']" \
                                                                  +f"/li[{row+1}]/span")
        aux = []
        
        for data in self.current_element:
            aux.append(data.text)
        
        return aux
    
    def get_row_from_releases_table(self, row=0):
        self.current_element = self.browser.find_elements_by_xpath("//section[@class='main-content ']/div[@class='row download-list-widget']"\
                                                                   +f"/ol[@class='list-row-container menu']/li[{row+1}]/span")
        
        aux = []
        
        for data in self.current_element:
            aux.append(data.text)
        
        return aux
    
    def get_latest_release_date(self):
        return datetime.datetime.strptime(self.get_row_from_releases_table(0)[1],"%b. %d, %Y")
    
    def get_latest_version_date(self):
        return datetime.datetime.strptime(self.get_row_from_versions_table(0)[2],"%Y-%m-%d")
    
    def get_latest_version(self):
        return self.get_row_from_versions_table(0)[0]
    
    def get_latest_release(self):
        return self.get_row_from_releases_table(0)[0]
        