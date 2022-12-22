from undetected_chromedriver import Chrome
from undetected_chromedriver import ChromeOptions
from time import sleep
from os import system
#import requests
#from random import choice
options=ChromeOptions()
options.headless=True
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=Chrome(options=options)
def remove_data(data):
    data=str(data)
    for i in range(0,100):
        if f"[{i}]" in data:
            data=data.replace(f"[{i}]","")
    print(data)

def website(data):
    driver.get("https://www.wikipedia.org/")
    driver.implicitly_wait(100)
    driver.find_element(by="xpath",value='//*[@id="searchInput"]').send_keys(data)
    driver.implicitly_wait(100)
    driver.find_element(by="xpath",value='//*[@id="search-form"]/fieldset/button').click()
    other_location=driver.find_elements(by="xpath",value='//div[@class="gallerytext"]/p')
    # system("cls")
    print(f"\t\t\t\t\t\tAbout {data}\n")
    for i in range(2,4):
        new_data=driver.find_element(by='xpath',value=f'//*[@id="mw-content-text"]/div[1]/p[{i}]')
        remove_data(new_data.text)
    driver.implicitly_wait(10)
    print("\n")
    print(f"\t\t\t\t\t\tPlaces to vist in {data}\n\n")
    for j in other_location:
        print("==>",j.text)

