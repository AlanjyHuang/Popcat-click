import selenium
import time
from selenium import webdriver
from random import seed
from random import random
times=int(input("Enter times"))
with open("driverPath", "r") as f:
    drivePath = f.read()
print(drivePath)
driver=webdriver.Chrome(executable_path=drivePath)
print(driver.name)
driver.get("https://popcat.click/?fbclid=IwAR17NzSuuafSNt-dsEmA_PTiWk7tRQH-Hd0AAfKy-9_4k58iBvlGDOjTGS0")
cat=driver.find_element_by_class_name('cat-img')

while(times>0):
    seed(times)
    cat.click()
    time.sleep(0.01)
    times-=1
#times=driver.find_element__by_class_name('counter rot')
show=driver.find_element_by_class_name('show')
show.click()
#print(times.get_text())
