from selenium import webdriver
from time import sleep
import csv

MAX_PAGE_NUM = 452

driver = webdriver.Firefox()

with open('results.csv', 'w') as f:
    f.write("Number of photos, Year and Model , Category, Condition, Material, Frame Size, Wheel Size, Front Travel, Rear Travel, Location,State/Province,Country, Seller, Price \n")

for i in range(1, MAX_PAGE_NUM + 1):
     
    url = f"https://www.pinkbike.com/buysell/list/?region=3&page={i}&category=2"
    #print(url)
    
    driver.get(url)
    
    title = driver.find_elements_by_xpath('//div[@class="bsitem"]')#
    #titles = driver.find_element_by_css_selector('#csid2750780')
    #prices = driver.find_elements_by_xpath('//span[@class="item-price"]')
    #print(title)
    #print(title[19].text)
    
    

    num_page_items = len(title)
    with open('results.csv', 'a') as f:
        for i in range(num_page_items):
            bike = title[i].text.split('\n')
            if 'photos' not in bike[0] :#or "All" not in bike[2]
                continue
            else:
                for x in range(0,12):
                    try:
                        f.write(bike[x] + ',')
                    except:
                        continue
                        
                
                f.write('\n')
        

driver.close()