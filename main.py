from selenium import webdriver
from time import sleep
import pandas as pd
from xlsxwriter import Workbook

# Reading a file with pandas
list_links_americanas = pd.read_excel(r"C:\Users\Developer\Desktop\Web Scraping - Compare prices of video cards\list_links_americanas.xlsx")

# Class to handle the web driver
class driver_handler:
    def __init__(self, list_links_americanas):
        self.driver = webdriver.Firefox()
        sleep(2)
    
    def find_prices_americanas(self):
        count = 0
        prices = []
        while(isinstance(list_links_americanas['GTX 1650'][count], str)):        
            self.driver.get(list_links_americanas['GTX 1650'][count])
            sleep(2)
            prices.append(self.driver.find_element_by_xpath("//span[contains(text(), 'R$')]").text.replace("R$","").replace(".",""))
            count += 1
        return pd.DataFrame({'Prices': prices})

driver = driver_handler(list_links_americanas)

df = driver.find_prices_americanas()

writer = pd.ExcelWriter(r"C:\Users\Developer\Desktop\Web Scraping - Compare prices of video cards\list_links_americanas.xlsx", engine='xlsxwriter') # pylint: disable=abstract-class-instantiated
df.to_excel(writer, sheet_name='Sheet1',index=False)
workbook  = writer.book
worksheet = writer.sheets['Sheet1']
print(list_links_americanas)
workbook  = Workbook('list_links_americanas.xlsx')
worksheet = workbook.add_worksheet()
writer.save()