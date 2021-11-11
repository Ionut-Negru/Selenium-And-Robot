# PythonDownloadPage.py

from chrome_driver import ChromeDriver

class PythonDownloadsPage(ChromeDriver):
    
    def __init__(self):
        ChromeDriver.__init__(self)
        self.table_data = None
        self.browser = ChromeDriver.browser
        
    def get_table_head_from_element(self):
        self.current_element = self.browser.find_elements_by_xpath("//section[@class='main-content ']/div[@class='row active-release-list-widget']/div[@class='list-row-headings']/span")
        table_head = []
        
        for head in self.current_element:
            table_head.append(head.text)
        
        return table_head
        
    def get_table_rows_from_element(self):
        self.current_element = self.browser.find_elements_by_xpath("//section[@class='main-content ']/div[@class='row active-release-list-widget']/ol[@class='list-row-container menu']/li")
        table_data = []
        
        for row in self.current_element:
            aux = []
            for data in row.text.split():
                aux.append(data)
                
            table_data.append(aux)
        
        return table_data
        
    def get_table_from_elements(self):
        table = []
        table_head = self.get_table_head_from_element()
        table_data = self.get_table_rows_from_element()
        
        for row in table_data:
            aux = {}
            
            for i in range(len(table_head)):
                aux[table_head[i]] = row[i]
            

            table.append(aux)
        
        self.table_data = table
        
    def get_table_row(self, index=0):
        return self.table_data[index]
    
    def get_data_from_table(self, row=0, column_name=""):
        return self.table_data[row][column_name]
    
    def close_downloads_page(self):
        self.close_browser()
        
        