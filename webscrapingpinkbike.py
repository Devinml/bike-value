from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import csv

MAX_PAGE_NUM = 1

driver = webdriver.Firefox()

'''
with open('results.csv', 'w') as f:
    f.write("Number of photos, Year and Model , Category, Condition, Material, Frame Size, Wheel Size, Front Travel, Rear Travel, Location,State/Province,Country, Seller, Price \n")
'''
for i in range(1, MAX_PAGE_NUM + 1):
     
    url = f"https://www.pinkbike.com/buysell/list/?region=3&page={i}&category=2"
    #print(url)
    
    driver.get(url)
    
    titles = driver.find_elements_by_xpath('//div[@class="bsitem"]')#
    #read_more_link = driver.find_element_by_css_selector()
    #print(titles[0])
    #elems = driver.find_elements_by_xpath("//a[@href]")
       
    for i in range(4):#range(20):
        elems = driver.find_elements_by_xpath("(//b[contains(.,'[Read More]')])")
        elems[i].click()
        location = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)')
        condition = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2)')
        frame_material = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(2)')
        frame_size = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(9) > td:nth-child(2)')
        wheel_size = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(10) > td:nth-child(2)')
        front_travel = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(2)')
        rear_travel = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(12) > td:nth-child(2)')
        price  = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(13) > td:nth-child(2)')
        description = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1)')

        
        print(frame_material.text)
        print(condition.text.strip())
        print(frame_size.text)
        print(wheel_size.text)
        print(front_travel.text)
        print(rear_travel.text)        
        print(price.text)
        print(description.text)
        driver.back()

       




        
    
    for i in range(len(titles)):
        pass
        #lems = driver.find_element_by_xpath("(//b[contains(.,'[Read More]')])")
        #print(elems)
        #for elem in elems:
         #   print(elem.get_attribute('href'))
        #print(type(titles[i]))   
        #read_more_link[i].click()
        #print('Clicked')
        #driver.back()        
        

    #titles = driver.find_element_by_css_selector('#csid2750780')
    #prices = driver.find_elements_by_xpath('//span[@class="item-price"]')
    #print(title)
    #print(title[19].text)
    
    
    '''
    num_page_items = len(titles)
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
                '''
        

driver.close()