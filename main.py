from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
from xlsxwriter import Workbook
import datetime

# List of websites to looking for the best price
stores = ['https://www.americanas.com.br/', 'https://www.kabum.com.br/', 'https://www.pichau.com.br/', 'https://www.terabyteshop.com.br/', 'https://www.shoptime.com.br/', 'https://www.magazineluiza.com.br/']

# Reading a file with pandas
list_products = pd.read_excel(r"C:\ws\WebScrapingComparepricesfromBrazil\list_products.xlsx")
# Index count
index = 0

# List to put prices as a dataframe with Pandas
prices = []

# Class to handle the web driver
class driver_handler:
    def __init__(self, list_products):
        self.driver = webdriver.Firefox()

    def find_prices_americanas(self):
        if(isinstance(list_products['Product'][index], str)):
            self.driver.get(stores[0]+'busca/'+list_products['Product'][index]+"?ordenacao=lowerPrice")
            sleep(2)
            prices.append(self.driver.find_element_by_xpath("//span[contains(text(), 'R$')]").text.replace("R$","").replace(".",""))
        else:
            prices.append('')
    
driver = driver_handler(list_products)
driver.find_prices_americanas()

#             # I used replace() to handle text data, because in Brazil, we use don't use dot and the Excel can't understand R$ as a number
#             prices.append(self.driver.find_element_by_xpath("//span[contains(text(), 'R$')]").text.replace("R$","").replace(".",""))
#             count += 1
#         return pd.DataFrame({datetime.datetime.now(): prices})

# driver = driver_handler(list_products)
# df_americanas = driver.find_prices_americanas()
# list_links_americanas = list_products.join(df_americanas)

# writer = pd.ExcelWriter(r"C:\ws\Web Scraping - Compare prices of video cards\list_products.xlsx", engine='xlsxwriter') # pylint: disable=abstract-class-instantiated
# list_links_americanas.to_excel(writer, sheet_name='Sheet1',index=False)
# workbook  = writer.book
# print(list_products)
# worksheet = writer.sheets['Sheet1']
# workbook  = Workbook('list_products.xlsx')
# worksheet = workbook.add_worksheet()
# writer.save()
#         def find_best_price_americanas(self, product):
#             self.driver.get(stores[index])
            #id="h_search"
# pd.DataFrame({datetime.datetime.now(): prices})
