from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver = webdriver.Chrome(executable_path=r"c:\users\daniel.malka\downloads\chromedriver_win32\chromedriver.exe")
firefox_driver = webdriver.Firefox(executable_path=r"c:\users\daniel.malka\downloads\geckodriver-v0.30.0-win64\geckodriver.exe")
chrome_driver.get("https://www.walla.co.il/")
firefox_driver.get("https://www.ynet.co.il/")
print("url: "+chrome_driver.current_url)
print("url: "+firefox_driver.current_url)
title = chrome_driver.title
print(title)
chrome_driver.refresh()
site_name = chrome_driver.current_url
if site_name == title:
    print("site name and title are identical.")
else:
    print("the names are not equals.")
chrome_driver.close()
firefox_driver.close()
