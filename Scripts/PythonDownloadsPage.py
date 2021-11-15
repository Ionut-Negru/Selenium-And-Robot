# PythonDownloadPage.py

from chrome_driver import ChromeDriver
import datetime


class PythonDownloadsPage(ChromeDriver):
    
    def __init__(self):
        super().__init__()
        self.browser = ChromeDriver.browser
        self.current_table = None
    
    def get_tables(self):
        self.releases_table = self.get_table('release')
        self.versions_table = self.get_table('version')
    
    def get_table_from_name(func):
        def wrapper(*args, **kwargs):
            table_option = func(*args, **kwargs)
            table_head = args[0].get_table_head(table_option)
            table_rows = args[0].get_table_rows(len(table_head), table_option)
            args[0].current_table = []
            for row in table_rows:
                aux = {}
                for i in range(len(row)):
                    aux[table_head[i]] = row[i]
                args[0].current_table.append(aux)
                
            return args[0].current_table
        return wrapper
      
    @get_table_from_name
    def get_table(self, table_name=''):
        match table_name.lower():
            case 'version':
                return 'row active-release-list-widget'
            case 'release':
                return 'row download-list-widget'
    
    
    def get_table_head(self, table_option=''):
        self.current_element = self.browser.find_elements_by_xpath(f"//section[@class='main-content ']/div[@class='{table_option}']/div[@class='list-row-headings']/span")
        table_head = []
        for head in self.current_element:
            table_head.append(head.text)
        return table_head
    
    def get_table_rows(self, row_len=0, table_option=''):
        self.current_element = self.browser.find_elements_by_xpath(f"//section[@class='main-content ']/div[@class='{table_option}']/ol[@class='list-row-container menu']/li/span")
        table_rows = []
        i=0
        while i < len(self.current_element):
            aux = []
            for j in range(row_len):
                if(i >= len(self.current_element)):
                    break
                else:
                    aux.append(self.current_element[i].text)
                    i += 1
            table_rows.append(aux)
            
        return table_rows
    
    def data_from_table(func):
        def wrapper(*args, **kwargs):
            if args[1] == 'version':
                args[0].current_table = args[0].versions_table
            elif  args[1] == 'release':
                args[0].current_table = args[0].releases_table
            
            return func(*args, **kwargs)
        return wrapper
    
    @data_from_table
    def get_table_row(self, table_option='', row=0):
        return self.current_table[row]
    
    @data_from_table
    def get_table_column(self,table_option='', column_name=''):
        """
            This method returns a list of the column entries
        """
        aux = []
        
        for x in self.current_table:
            aux.append(x[column_name])
        
        return aux
    
    @data_from_table
    def get_table_entry(self, table_option='', column_name='', row=0):
        return self.current_table[row][column_name]
    
    @data_from_table
    def has_entry_inside_table_column(self, table_option='', column_name='', entry=''):
        """
            Check if an entry is inside the table column
        """
        for i in range(len(self.current_table)):
            if self.current_table[i][column_name].find(entry):
                return True
        return False
    
    def get_latest_version(self):
        return self.versions_table[0]['Python version']
    
    def get_latest_release(self):
        return self.releases_table[0]['Release version']

    def get_latest_release_date(self):
        aux = self.releases_table[0]['Release date']
        return datetime.datetime.strptime(aux,"%b. %d, %Y")
    
    def get_latest_version_date(self):
        aux = self.versions_table[0]['First released']
        return datetime.datetime.strptime(aux,"%Y-%m-%d")
    
    