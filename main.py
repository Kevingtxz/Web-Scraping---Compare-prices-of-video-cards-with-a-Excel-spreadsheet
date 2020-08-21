from selenium import webdriver
from time import sleep
import pandas as pd
from xlsxwriter import Workbook
import datetime

# Reading a file with pandas
list_links_americanas = pd.read_excel(r"C:\ws\Web Scraping - Compare prices of video cards\list_links_americanas.xlsx")
# Index count
index = 1

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
            # I used replace() to handle text data, because in Brazil, we use don't use dot and the Excel can't understand R$ as a number
            prices.append(self.driver.find_element_by_xpath("//span[contains(text(), 'R$')]").text.replace("R$","").replace(".",""))
            count += 1
        return pd.DataFrame({datetime.datetime.now(): prices})

driver = driver_handler(list_links_americanas)
df_americanas = driver.find_prices_americanas()
list_links_americanas = list_links_americanas.join(df_americanas)

writer = pd.ExcelWriter(r"C:\ws\Web Scraping - Compare prices of video cards\list_links_americanas.xlsx", engine='xlsxwriter') # pylint: disable=abstract-class-instantiated
list_links_americanas.to_excel(writer, sheet_name='Sheet1',index=False)
workbook  = writer.book
worksheet = writer.sheets['Sheet1']
print(list_links_americanas)
print(df_americanas)
workbook  = Workbook('list_links_americanas.xlsx')
worksheet = workbook.add_worksheet()
writer.save()