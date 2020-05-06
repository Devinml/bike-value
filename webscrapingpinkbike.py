from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import csv
import string

def remove_punc(string_):
    exclude = set(string.punctuation)
    s =  ''.join(ch for ch in string_ if ch not in exclude)
    return s


MAX_PAGE_NUM = 1

driver = webdriver.Firefox()


with open('results.csv', 'w') as f:
    f.write("Title,Location,Condition,Material,Frame Size,Wheel Size,Front Travel,Rear Travel,Price,City,State/Prov,Country\n")

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
        print(len(elems))
        elems[i].click()
        try:
            
            title = driver.find_element_by_css_selector('.hboxr-c3-h > h1:nth-child(1)')
            location = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)')
            condition = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2)')
            frame_material = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(2)')
            frame_size = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(9) > td:nth-child(2)')
            wheel_size = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(10) > td:nth-child(2)')
            front_travel = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(2)')
            rear_travel = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(12) > td:nth-child(2)')
            price  = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(13) > td:nth-child(2)')
            location = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)')
            description = driver.find_element_by_css_selector('.hbox-c3-m > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1)')
            print(title.text.strip())
            print(frame_material.text.strip())
            print(condition.text.strip())
            print(frame_size.text)
            print(wheel_size.text)
            print(front_travel.text)
            print(rear_travel.text)        
            print(price.text)
            print(location.text)
            print(remove_punc(description.text.strip()))
            
            with open('results.csv', 'a') as f:
                f.write(title.text.strip() + ',' + location.text.strip() + ',' + condition.text.strip() + ',' + frame_material.text.strip()+','+frame_size.text.strip()+','+wheel_size.text.strip()+','+front_travel.text.strip()+','+rear_travel.text.strip()+','+price.text.strip()+','+location.text()+','+remove_punc(description.text.strip())+'\n')

        except :
            driver.back()
        driver.back()

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