# Automate whatsapp messaging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/home/cloudtech/Downloads/chromedriver_linux64/chromedriver')
driver.get('https://web.whatsapp.com')
name = input('Enter the name of friend')
message = input('give message')
number = int(input('Enter count of messages'))

elem = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
elem.click()

#msg = driver.find_element_by_class_name('_2S1VP copyable-text selectable-text')
msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
for i in range(number):
    msg.click()
    time.sleep(0.2)
    msg.send_keys(message + Keys.ENTER)
    print('{} iteration'.format(i))
    
driver.close()

