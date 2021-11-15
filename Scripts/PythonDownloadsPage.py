# PythonDownloadPage.py

from chrome_driver import ChromeDriver
import datetime

class PythonDownloadsPage(ChromeDriver):
    
    def __init__(self):
        super().__init__()
        self.browser = ChromeDriver.browser
    
    def get_releases_table(self):
        table_head = self.get_releases_table_head()
        table_rows = self.get_releases_table_rows()
        self.releases_table = []
        for row in table_rows:
            aux = {}
            for i in range(len(row)):
                aux[table_head[i]] = row[i]
            self.releases_table.append(aux)
          
    def get_releases_table_head(self):
        self.current_element = self.browser.find_elements_by_xpath("//section[@class='main-content ']/div[@class='row download-list-widget']/div[@class='list-row-headings']/span")
        self.releases_table_head = []
        for head in self.current_element:
            self.releases_table_head.append(head.text)
        return self.releases_table_head
    
    def get_releases_table_rows(self):
        self.current_element = self.browser.find_elements_by_xpath("//section[@class='main-content ']/div[@class='row download-list-widget']/ol[@class='list-row-container menu']/li/span")
        self.releases_table_rows = []
        i=0
        while i < len(self.current_element):
            aux = []
            for j in range(len(self.releases_table_head)):
                if(i > len(self.current_element)):
                    break
                else:
                    aux.append(self.current_element[i].text)
                    i += 1
            self.releases_table_rows.append(aux)
            
        return self.releases_table_rows
    
    
    def get_versions_table(self):
        table_head = self.get_versions_table_head()
        table_data = self.get_versions_table_rows()
        self.version_table = []
        for row in table_data:
            aux = {}
            for i in range(len(row)):
                aux[table_head[i]] = row[i]
            self.version_table.append(aux)
            
    def get_versions_table_head(self):
        self.current_element = self.browser.find_elements_by_xpath("//section[@class='main-content ']/div[@class='row active-release-list-widget']/div[@class='list-row-headings']/span")
        self.versions_table_head = []
        
        for i in self.current_element:
            self.versions_table_head.append(i.text)
        
        return self.versions_table_head
        
    def get_versions_table_rows(self):
        self.current_element = self.browser.find_elements_by_xpath("//section[@class='main-content ']/div[@class='row active-release-list-widget']/ol[@class='list-row-container menu']/li/span")
        self.versions_table_rows = []
        i=0
        while i < len(self.current_element):
            aux = []
            for j in range(len(self.versions_table_head)):
                if(i > len(self.current_element)):
                    break
                else:
                    aux.append(self.current_element[i].text)
                    i += 1
            self.versions_table_rows.append(aux)
        return self.versions_table_rows
          
    def get_versions_table_row(self, row=0):
        return self.version_table[row]
    
    def get_releases_table_row(self, row=0):
        return self.releases_table[row]
    
    def get_versions_table_column(self, column_name=''):
        aux = []
        
        for x in self.version_table:
            aux.append(x[column_name])
        
        return aux
    
    def get_releases_table_column(self,column_name=''):
        aux = []
        
        for x in self.releases_table:
            aux.append(x[column_name])
            
        return aux
    
    def get_latest_version(self):
        return self.get_versions_table_row(0)['Python version']
    
    def get_latest_release(self):
        return self.get_releases_table_row(0)['Release version']

    def get_latest_release_date(self):
        aux = self.get_releases_table_row(0)['Release date']
        return datetime.datetime.strptime(aux,"%b. %d, %Y")
    
    def get_latest_version_date(self):
        aux = self.get_versions_table_row(0)['First released']
        return datetime.datetime.strptime(aux,"%Y-%m-%d")
        
    def has_entry_inside_releases_table_column(self, column_name='', entry=''):
        for aux in self.get_releases_table_column(column_name):
            if aux.find(entry):
                return True
        return False
    
    def has_entry_inside_versions_table_column(self, column_name='', entry=''):
        for aux in self.get_versions_table_column(column_name):
            if aux.find(entry):
                return True
        return False
        
    
    