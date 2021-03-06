from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import csv
import string



def remove_punc(string_):
    exclude = set(string.punctuation)
    s =  ''.join(ch for ch in string_ if ch not in exclude)
    return s

def remove_new_line(input_string):
    return input_string.replace('\n','')


MAX_PAGE_NUM = 406
profile = webdriver.FirefoxProfile('/home/devin/Scripts/Bike Value Analysis/firefoxprofile')

driver = webdriver.Firefox(firefox_profile=profile)


f = open('results.csv','w')
f.write("Title,Condition,Material,Frame Size,Wheel Size,Front Travel,Rear Travel,Price,City,State/Prov,Country,Description,Date Posted\n")

for i in range(1, MAX_PAGE_NUM + 1):
     
    url = f"https://www.pinkbike.com/buysell/list/?region=3&page={i}&category=2"
    
    
    driver.get(url)
    
    titles = driver.find_elements_by_xpath('//div[@class="bsitem"]')#

    css_sel_list = [
        '.hboxr-c3-h > h1:nth-child(1)', # title
        '.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2)', # condition
        '.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(2)', # Frame Material
        '.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(9) > td:nth-child(2)', # Frame Size
        '.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(10) > td:nth-child(2)', # Wheel Size
        '.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(2)', # Front Travel
        '.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(12) > td:nth-child(2)', # Rear Travel
        '.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(13) > td:nth-child(2)', # Price
        '.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)', # Location
        '.hbox-c3-m > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1)',  # Description 
        '.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2)' # Date

    ]
    if i %10 == 0:
        sleep(60)
    for i in range(20):
        
        elems = driver.find_elements_by_xpath("(//b[contains(.,'[Read More]')])")
        elems[i].click()
        bike_data = ''
        for key, selector in enumerate(css_sel_list):
            try:
                if key == 8:
                    bike_data += driver.find_element_by_css_selector(selector).text + ','
                    bike_data.replace('\n', '')
                elif key == 9:
                    bike_data += remove_punc(driver.find_element_by_css_selector(selector).text) + ','
                    bike_data.replace('\n','')
                elif key == 10:
                    bike_data += driver.find_element_by_css_selector(selector).text + ','
                else:
                    bike_data += remove_punc(driver.find_element_by_css_selector(selector).text) + ','
                    bike_data.replace('\n','')
                 
            except:
                bike_data = ''
                break
       
        bike_data.rstrip()
        
        if len(bike_data)>1:
            f.write(remove_new_line(bike_data))
            f.write('\n')
        print("-------------------------------------------------------")
        bike_data = ''
        driver.back()
f.close()
driver.close()