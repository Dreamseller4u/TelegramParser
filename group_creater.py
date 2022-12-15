import time
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/home/ds/Projects/TelegramParser/driver/chromedriver')
driver.get("https://web.telegram.org/?legacy=1#/im")

phone_nuber = '+62895416029826'


phone_input = driver.find_element(By.NAME, 'phone_number')
phone_input.send_keys(phone_nuber)
# time.sleep(3)
phone_input.submit()

rdy = input("Input code by ur self then open create group modal and press enter here.")

form = driver.find_element(By.XPATH, '//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/div[1]/input')


with open('users.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
count = 0
for i in data:
    if count >= 800:
        end  = input('Its all comlite crate group and press enter button')
        break
    form.send_keys(i[0])
    time.sleep(2)
    try:
        acc = driver.find_element(By.XPATH, '//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/div[2]/div/div[1]/ul/li/a/div[2]').click()
        count += 1
    except Exception as e:
        pass
    form.clear()

rdy = input("Comlite, create a group by ur self ent push the enter : ")

driver.close()